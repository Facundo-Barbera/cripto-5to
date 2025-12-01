#!/usr/bin/env python3

import dns.resolver
import dns.rdatatype
import dns.exception
import dns.message
import dns.query
import dns.rcode
import dns.flags
import time
import uuid
import json
import os
import sys
import re
from datetime import datetime
from typing import Dict, List, Any, Optional


def sanitize_domain(input_str: str) -> str:
    """
    Sanitize user input to extract clean domain.
    - Strip protocol (http://, https://)
    - Strip www. prefix
    - Strip trailing slashes and paths
    - Convert to lowercase
    """
    if not input_str:
        return ''

    domain = input_str.strip().lower()
    # Remove protocol
    domain = re.sub(r'^https?://', '', domain)
    # Remove www. prefix
    domain = re.sub(r'^www\.', '', domain)
    # Remove path/query/fragment
    domain = domain.split('/')[0].split('?')[0].split('#')[0]
    # Remove any trailing dots
    domain = domain.rstrip('.')
    return domain


class DNSSECAnalyzer:

    def __init__(self, nameserver: str = '8.8.8.8', delay_seconds: float = 1.0, timeout: int = 10):
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = [nameserver]
        self.resolver.timeout = timeout
        self.resolver.lifetime = timeout
        self.delay = delay_seconds
        self.cache = {}
        self.results = {}

    def check_domain_status(self, domain: str) -> Dict[str, Any]:
        """
        Pre-flight check to detect domain status before full analysis.
        Returns status: OK, NXDOMAIN, SERVFAIL, TIMEOUT, NO_NS, NO_ADDRESS
        """
        try:
            # Try to resolve NS records first
            try:
                ns_answer = self.resolver.resolve(domain, 'NS')
            except dns.resolver.NoAnswer:
                # Domain exists but has no NS records
                return {
                    'status': 'NO_NS',
                    'message': 'Domain exists but has no nameserver records configured',
                    'can_analyze': False
                }
            except dns.resolver.NXDOMAIN:
                return {
                    'status': 'NXDOMAIN',
                    'message': 'Domain does not exist',
                    'can_analyze': False
                }
            except dns.resolver.NoNameservers:
                return {
                    'status': 'SERVFAIL',
                    'message': 'DNS server failure - no nameservers could be reached',
                    'can_analyze': False
                }
            except dns.exception.Timeout:
                return {
                    'status': 'TIMEOUT',
                    'message': 'DNS query timed out',
                    'can_analyze': False
                }

            # Try to resolve A/AAAA records (domain exists, check if it has addresses)
            try:
                a_answer = self.resolver.resolve(domain, 'A')
                return {
                    'status': 'OK',
                    'message': None,
                    'can_analyze': True
                }
            except dns.resolver.NoAnswer:
                # Try AAAA
                try:
                    aaaa_answer = self.resolver.resolve(domain, 'AAAA')
                    return {
                        'status': 'OK',
                        'message': None,
                        'can_analyze': True
                    }
                except dns.resolver.NoAnswer:
                    # Domain has NS but no A/AAAA - still analyzable for DNSSEC
                    return {
                        'status': 'NO_ADDRESS',
                        'message': 'Domain has nameservers but no A/AAAA records',
                        'can_analyze': True
                    }

            return {
                'status': 'OK',
                'message': None,
                'can_analyze': True
            }

        except Exception as e:
            return {
                'status': 'ERROR',
                'message': str(e),
                'can_analyze': False
            }

    def _get_authoritative_ns(self, domain: str) -> Optional[str]:
        try:
            ns_answer = self.resolver.resolve(domain, 'NS')
            if ns_answer:
                ns_name = str(ns_answer[0].target).rstrip('.')
                a_answer = self.resolver.resolve(ns_name, 'A')
                if a_answer:
                    return str(a_answer[0].address)
        except Exception:
            pass
        return None

    def _query_raw(self, qname: str, rdtype: str, nameserver: str = None) -> Optional[dns.message.Message]:
        ns = nameserver or self.resolver.nameservers[0]
        try:
            query = dns.message.make_query(qname, rdtype, want_dnssec=True)
            response = dns.query.udp(query, ns, timeout=self.resolver.timeout)
            if response.flags & dns.flags.TC:
                response = dns.query.tcp(query, ns, timeout=self.resolver.timeout)
            return response
        except Exception as e:
            print(f"WARNING: Raw query to {ns} failed for {qname}: {e}")
            return None

    def _detect_nsec_from_nxdomain(self, domain: str) -> Dict[str, Any]:
        result = {
            'nsec_records': [],
            'nsec3_records': [],
            'rrsig_records': [],
            'detection_source': None
        }

        probe_name = f"_dnssec-probe-{uuid.uuid4().hex}.{domain}"

        zone_apex_labels = len(domain.rstrip('.').split('.'))

        response = self._query_raw(probe_name, 'A')
        if response and response.authority:
            result['detection_source'] = 'recursive_resolver'
        else:
            auth_ns = self._get_authoritative_ns(domain)
            if auth_ns:
                response = self._query_raw(probe_name, 'A', nameserver=auth_ns)
                if response and response.authority:
                    result['detection_source'] = 'authoritative_ns'

        if response is None:
            return result

        for rrset in response.authority:
            if rrset.rdtype == dns.rdatatype.NSEC:
                for rdata in rrset:
                    result['nsec_records'].append({
                        'owner': str(rrset.name),
                        'next_domain': str(rdata.next),
                        'ttl': rrset.ttl
                    })
            elif rrset.rdtype == dns.rdatatype.NSEC3:
                for rdata in rrset:
                    result['nsec3_records'].append({
                        'owner': str(rrset.name),
                        'hash_algorithm': rdata.algorithm,
                        'flags': rdata.flags,
                        'iterations': rdata.iterations,
                        'salt': rdata.salt.hex() if rdata.salt else 'none',
                        'opt_out': bool(rdata.flags & 0x01),
                        'ttl': rrset.ttl
                    })
            elif rrset.rdtype == dns.rdatatype.RRSIG:
                for rdata in rrset:
                    type_covered = dns.rdatatype.to_text(rdata.type_covered)
                    if type_covered in ('NSEC', 'NSEC3') and rdata.labels == zone_apex_labels:
                        result['rrsig_records'].append(self._parse_rrsig(rdata))
        return result

    def _query_safe(self, domain: str, rdtype: str, use_dnssec: bool = True) -> Optional[Any]:
        cache_key = f"{domain}:{rdtype}:{use_dnssec}"

        if cache_key in self.cache:
            return self.cache[cache_key]

        try:
            if use_dnssec:
                answer = self.resolver.resolve(domain, rdtype, raise_on_no_answer=False)
            else:
                answer = self.resolver.resolve(domain, rdtype)

            self.cache[cache_key] = answer
            return answer
        except dns.resolver.NoAnswer:
            return None
        except dns.resolver.NXDOMAIN:
            print(f"WARNING: Domain does not exist: {domain}")
            return None
        except dns.exception.Timeout:
            print(f"WARNING: Timeout on {domain} ({rdtype})")
            return None
        except Exception as e:
            print(f"WARNING: Error on {domain} ({rdtype}): {e}")
            return None

    def analyze_dnskey(self, domain: str) -> Dict[str, Any]:
        result = {
            'present': False,
            'count': 0,
            'keys': [],
            'ttl': None
        }

        answer = self._query_safe(domain, 'DNSKEY')
        if not answer:
            return result

        result['present'] = True
        result['count'] = len(answer)
        result['ttl'] = answer.rrset.ttl if hasattr(answer, 'rrset') else None

        for rdata in answer:
            key_info = {
                'flags': rdata.flags,
                'protocol': rdata.protocol,
                'algorithm': rdata.algorithm,
                'algorithm_name': self._get_algorithm_name(rdata.algorithm),
                'key_size_bits': self._calculate_key_size(rdata),
                'is_sep': bool(rdata.flags & 0x0001),
                'is_zone_key': bool(rdata.flags & 0x0100)
            }
            result['keys'].append(key_info)

        return result

    def analyze_rrsig(self, domain: str, nsec_rrsig_records: List[Dict] = None) -> Dict[str, Any]:
        result = {
            'present': False,
            'count': 0,
            'signatures': [],
            'signatures_by_type': {},
            'ttl': None
        }

        response = self._query_raw(domain, 'RRSIG')
        if response:
            for rrset in response.answer:
                if rrset.rdtype == dns.rdatatype.RRSIG:
                    result['present'] = True
                    if result['ttl'] is None:
                        result['ttl'] = rrset.ttl
                    for rdata in rrset:
                        sig_info = self._parse_rrsig(rdata)
                        if sig_info not in result['signatures']:
                            result['signatures'].append(sig_info)

        if nsec_rrsig_records:
            for sig_info in nsec_rrsig_records:
                if sig_info not in result['signatures']:
                    result['signatures'].append(sig_info)
                    result['present'] = True

        for sig in result['signatures']:
            type_covered = sig['type_covered']
            if type_covered not in result['signatures_by_type']:
                result['signatures_by_type'][type_covered] = []
            result['signatures_by_type'][type_covered].append(sig)

        result['count'] = len(result['signatures'])
        return result

    def _parse_rrsig(self, rdata) -> Dict[str, Any]:
        return {
            'type_covered': dns.rdatatype.to_text(rdata.type_covered),
            'algorithm': rdata.algorithm,
            'algorithm_name': self._get_algorithm_name(rdata.algorithm),
            'labels': rdata.labels,
            'original_ttl': rdata.original_ttl,
            'expiration': datetime.fromtimestamp(rdata.expiration).isoformat(),
            'inception': datetime.fromtimestamp(rdata.inception).isoformat(),
            'key_tag': rdata.key_tag,
            'signer': str(rdata.signer).rstrip('.'),
            'is_expired': rdata.expiration < int(time.time()),
            'days_until_expiration': (rdata.expiration - int(time.time())) // 86400
        }

    def analyze_nsec(self, domain: str) -> Dict[str, Any]:
        result = {
            'nsec_type': 'none',
            'nsec_present': False,
            'nsec3_present': False,
            'nsec3param_present': False,
            'opt_out': False,
            'detection_source': None,
            'rrsig_records': [],
            'details': {}
        }

        nsec3param_answer = self._query_safe(domain, 'NSEC3PARAM')
        if nsec3param_answer:
            result['nsec3param_present'] = True
            param_records = []
            for rdata in nsec3param_answer:
                param_info = {
                    'hash_algorithm': rdata.algorithm,
                    'flags': rdata.flags,
                    'iterations': rdata.iterations,
                    'salt': rdata.salt.hex() if rdata.salt else 'none'
                }
                param_records.append(param_info)

            result['details']['nsec3param'] = {
                'count': len(nsec3param_answer),
                'ttl': nsec3param_answer.rrset.ttl if hasattr(nsec3param_answer, 'rrset') else None,
                'records': param_records
            }

        nxdomain_result = self._detect_nsec_from_nxdomain(domain)

        result['rrsig_records'] = nxdomain_result.get('rrsig_records', [])

        if nxdomain_result['nsec_records']:
            result['nsec_present'] = True
            result['nsec_type'] = 'NSEC'
            result['detection_source'] = nxdomain_result['detection_source']
            result['details']['nsec'] = {
                'count': len(nxdomain_result['nsec_records']),
                'ttl': nxdomain_result['nsec_records'][0]['ttl'] if nxdomain_result['nsec_records'] else None,
                'records': nxdomain_result['nsec_records'],
                'detection_method': 'authority_section'
            }

        if nxdomain_result['nsec3_records']:
            result['nsec3_present'] = True
            result['nsec_type'] = 'NSEC3'
            result['detection_source'] = nxdomain_result['detection_source']

            for nsec3_record in nxdomain_result['nsec3_records']:
                if nsec3_record.get('opt_out'):
                    result['opt_out'] = True
                    break

            result['details']['nsec3'] = {
                'count': len(nxdomain_result['nsec3_records']),
                'ttl': nxdomain_result['nsec3_records'][0]['ttl'] if nxdomain_result['nsec3_records'] else None,
                'records': nxdomain_result['nsec3_records'],
                'detection_method': 'authority_section'
            }

        if result['nsec3param_present'] and not result['nsec3_present']:
            result['nsec3_present'] = True
            result['nsec_type'] = 'NSEC3'
            result['detection_source'] = 'nsec3param_inference'
            if 'nsec3' not in result['details']:
                result['details']['nsec3'] = {
                    'count': 0,
                    'ttl': None,
                    'records': [],
                    'detection_method': 'nsec3param_inference'
                }

        if not result['nsec_present'] and not result['nsec3_present']:
            nsec_answer = self._query_safe(domain, 'NSEC')
            if nsec_answer:
                result['nsec_present'] = True
                result['nsec_type'] = 'NSEC'
                result['detection_source'] = 'direct_query'
                result['details']['nsec'] = {
                    'count': len(nsec_answer),
                    'ttl': nsec_answer.rrset.ttl if hasattr(nsec_answer, 'rrset') else None,
                    'records': [],
                    'detection_method': 'direct_query'
                }

        return result

    def analyze_ds(self, domain: str) -> Dict[str, Any]:
        result = {
            'present': False,
            'count': 0,
            'records': [],
            'ttl': None
        }

        answer = self._query_safe(domain, 'DS')
        if not answer:
            return result

        result['present'] = True
        result['count'] = len(answer)
        result['ttl'] = answer.rrset.ttl if hasattr(answer, 'rrset') else None

        for rdata in answer:
            ds_info = {
                'key_tag': rdata.key_tag,
                'algorithm': rdata.algorithm,
                'algorithm_name': self._get_algorithm_name(rdata.algorithm),
                'digest_type': rdata.digest_type,
                'digest_type_name': self._get_digest_type_name(rdata.digest_type),
                'digest': rdata.digest.hex()
            }
            result['records'].append(ds_info)

        return result

    def _get_zone_hierarchy(self, domain: str) -> List[str]:
        parts = domain.rstrip('.').split('.')
        hierarchy = []
        for i in range(len(parts)):
            zone = '.'.join(parts[i:])
            hierarchy.append(zone)
        hierarchy.append('.')
        return hierarchy

    def _analyze_zone_dnssec(self, zone: str) -> Dict[str, Any]:
        result = {
            'zone': zone,
            'has_dnskey': False,
            'has_ds': False,
            'has_rrsig': False,
            'algorithms': [],
            'key_tags': [],
            'is_signed': False
        }

        if zone == '.':
            result['has_dnskey'] = True
            result['has_rrsig'] = True
            result['is_signed'] = True
            result['algorithms'] = [8]
            result['key_tags'] = [20326]
            return result

        dnskey_answer = self._query_safe(zone, 'DNSKEY')
        if dnskey_answer:
            result['has_dnskey'] = True
            for rdata in dnskey_answer:
                if rdata.algorithm not in result['algorithms']:
                    result['algorithms'].append(rdata.algorithm)

        ds_answer = self._query_safe(zone, 'DS')
        if ds_answer:
            result['has_ds'] = True
            for rdata in ds_answer:
                if rdata.key_tag not in result['key_tags']:
                    result['key_tags'].append(rdata.key_tag)

        response = self._query_raw(zone, 'RRSIG')
        if response:
            for rrset in response.answer:
                if rrset.rdtype == dns.rdatatype.RRSIG:
                    result['has_rrsig'] = True
                    break

        result['is_signed'] = result['has_dnskey'] and result['has_rrsig']
        return result

    def analyze_chain_of_trust(self, domain: str) -> Dict[str, Any]:
        hierarchy = self._get_zone_hierarchy(domain)
        chain = []
        broken_at = None

        for zone in hierarchy:
            zone_status = self._analyze_zone_dnssec(zone)
            chain.append(zone_status)

            if not zone_status['is_signed'] and broken_at is None:
                broken_at = zone

        for i in range(len(chain) - 1):
            current = chain[i]
            if current['is_signed'] and not current['has_ds'] and current['zone'] != '.':
                if broken_at is None:
                    broken_at = current['zone']

        chain_valid = broken_at is None

        return {
            'hierarchy': hierarchy,
            'chain': chain,
            'is_complete': chain_valid,
            'broken_at': broken_at,
            'depth': len(hierarchy)
        }

    def analyze_spf(self, domain: str) -> Dict[str, Any]:
        """Analyze SPF (Sender Policy Framework) records"""
        result = {
            'present': False,
            'record': None,
            'mechanisms': [],
            'all_mechanism': None,
            'includes': [],
            'policy_strength': 'none'
        }

        txt_answer = self._query_safe(domain, 'TXT', use_dnssec=False)
        if not txt_answer:
            return result

        for rdata in txt_answer:
            txt_value = str(rdata).strip('"')
            if txt_value.lower().startswith('v=spf1'):
                result['present'] = True
                result['record'] = txt_value

                # Parse SPF mechanisms
                parts = txt_value.split()
                for part in parts[1:]:  # Skip v=spf1
                    part_lower = part.lower()
                    if part_lower.startswith('include:'):
                        result['includes'].append(part[8:])
                        result['mechanisms'].append({'type': 'include', 'value': part[8:]})
                    elif part_lower.startswith('a:') or part_lower == 'a':
                        result['mechanisms'].append({'type': 'a', 'value': part[2:] if ':' in part else domain})
                    elif part_lower.startswith('mx:') or part_lower == 'mx':
                        result['mechanisms'].append({'type': 'mx', 'value': part[3:] if ':' in part else domain})
                    elif part_lower.startswith('ip4:'):
                        result['mechanisms'].append({'type': 'ip4', 'value': part[4:]})
                    elif part_lower.startswith('ip6:'):
                        result['mechanisms'].append({'type': 'ip6', 'value': part[4:]})
                    elif part_lower in ['-all', '~all', '?all', '+all']:
                        result['all_mechanism'] = part_lower
                        if part_lower == '-all':
                            result['policy_strength'] = 'strict'
                        elif part_lower == '~all':
                            result['policy_strength'] = 'soft_fail'
                        elif part_lower == '?all':
                            result['policy_strength'] = 'neutral'
                        elif part_lower == '+all':
                            result['policy_strength'] = 'permissive'
                    elif part_lower.startswith('redirect='):
                        result['mechanisms'].append({'type': 'redirect', 'value': part[9:]})

                break  # Only process first SPF record

        return result

    def analyze_dmarc(self, domain: str) -> Dict[str, Any]:
        """Analyze DMARC (Domain-based Message Authentication) records"""
        result = {
            'present': False,
            'record': None,
            'policy': None,
            'subdomain_policy': None,
            'percentage': 100,
            'rua': [],  # Aggregate report addresses
            'ruf': [],  # Forensic report addresses
            'adkim': 'relaxed',
            'aspf': 'relaxed'
        }

        dmarc_domain = f'_dmarc.{domain}'
        txt_answer = self._query_safe(dmarc_domain, 'TXT', use_dnssec=False)
        if not txt_answer:
            return result

        for rdata in txt_answer:
            txt_value = str(rdata).strip('"')
            if txt_value.lower().startswith('v=dmarc1'):
                result['present'] = True
                result['record'] = txt_value

                # Parse DMARC tags
                tags = txt_value.split(';')
                for tag in tags:
                    tag = tag.strip()
                    if '=' in tag:
                        key, value = tag.split('=', 1)
                        key = key.strip().lower()
                        value = value.strip()

                        if key == 'p':
                            result['policy'] = value.lower()
                        elif key == 'sp':
                            result['subdomain_policy'] = value.lower()
                        elif key == 'pct':
                            try:
                                result['percentage'] = int(value)
                            except ValueError:
                                pass
                        elif key == 'rua':
                            result['rua'] = [addr.strip() for addr in value.split(',')]
                        elif key == 'ruf':
                            result['ruf'] = [addr.strip() for addr in value.split(',')]
                        elif key == 'adkim':
                            result['adkim'] = 'strict' if value.lower() == 's' else 'relaxed'
                        elif key == 'aspf':
                            result['aspf'] = 'strict' if value.lower() == 's' else 'relaxed'

                break  # Only process first DMARC record

        return result

    def analyze_dkim(self, domain: str) -> Dict[str, Any]:
        """Check for common DKIM selectors"""
        result = {
            'selectors_checked': [],
            'selectors_found': [],
            'records': []
        }

        # Common DKIM selectors used by various providers
        common_selectors = [
            'default', 'dkim', 'mail', 'email',
            'google', 'selector1', 'selector2',  # Microsoft 365
            'k1', 'k2', 'k3',  # Mailchimp
            's1', 's2',
            'mandrill', 'smtp', 'mx'
        ]

        for selector in common_selectors:
            dkim_domain = f'{selector}._domainkey.{domain}'
            result['selectors_checked'].append(selector)

            txt_answer = self._query_safe(dkim_domain, 'TXT', use_dnssec=False)
            if txt_answer:
                for rdata in txt_answer:
                    txt_value = str(rdata).strip('"')
                    if 'v=dkim1' in txt_value.lower() or 'k=rsa' in txt_value.lower():
                        result['selectors_found'].append(selector)
                        record_info = {
                            'selector': selector,
                            'record': txt_value[:200] + '...' if len(txt_value) > 200 else txt_value
                        }

                        # Parse some DKIM tags
                        if 'k=' in txt_value:
                            for part in txt_value.split(';'):
                                part = part.strip()
                                if part.startswith('k='):
                                    record_info['key_type'] = part[2:]
                                elif part.startswith('t='):
                                    record_info['flags'] = part[2:]

                        result['records'].append(record_info)
                        break

        result['found'] = len(result['selectors_found']) > 0
        return result

    def analyze_caa(self, domain: str) -> Dict[str, Any]:
        """Analyze CAA (Certificate Authority Authorization) records"""
        result = {
            'present': False,
            'records': [],
            'issue': [],
            'issuewild': [],
            'iodef': []
        }

        caa_answer = self._query_safe(domain, 'CAA', use_dnssec=False)
        if not caa_answer:
            return result

        result['present'] = True
        for rdata in caa_answer:
            record_info = {
                'flags': rdata.flags,
                'tag': rdata.tag.decode() if isinstance(rdata.tag, bytes) else str(rdata.tag),
                'value': rdata.value.decode() if isinstance(rdata.value, bytes) else str(rdata.value)
            }
            result['records'].append(record_info)

            tag = record_info['tag'].lower()
            value = record_info['value']
            if tag == 'issue':
                result['issue'].append(value)
            elif tag == 'issuewild':
                result['issuewild'].append(value)
            elif tag == 'iodef':
                result['iodef'].append(value)

        return result

    def analyze_email_security(self, domain: str) -> Dict[str, Any]:
        """Analyze all email security records (SPF, DKIM, DMARC)"""
        return {
            'spf': self.analyze_spf(domain),
            'dkim': self.analyze_dkim(domain),
            'dmarc': self.analyze_dmarc(domain)
        }

    def analyze_ns_diversity(self, domain: str) -> Dict[str, Any]:
        """Analyze nameserver diversity (different networks/providers)"""
        result = {
            'nameservers': [],
            'unique_tlds': [],
            'unique_providers': [],
            'ipv4_addresses': [],
            'ipv6_addresses': [],
            'has_ipv6': False,
            'diversity_score': 0,
            'recommendations': []
        }

        ns_answer = self._query_safe(domain, 'NS', use_dnssec=False)
        if not ns_answer:
            return result

        ns_names = []
        for rdata in ns_answer:
            ns_name = str(rdata.target).rstrip('.')
            ns_names.append(ns_name)
            result['nameservers'].append(ns_name)

            # Extract TLD/provider from NS name
            parts = ns_name.split('.')
            if len(parts) >= 2:
                tld = '.'.join(parts[-2:])
                if tld not in result['unique_tlds']:
                    result['unique_tlds'].append(tld)

        # Resolve NS IP addresses
        for ns_name in ns_names:
            # IPv4
            a_answer = self._query_safe(ns_name, 'A', use_dnssec=False)
            if a_answer:
                for rdata in a_answer:
                    ip = str(rdata.address)
                    if ip not in result['ipv4_addresses']:
                        result['ipv4_addresses'].append(ip)

            # IPv6
            aaaa_answer = self._query_safe(ns_name, 'AAAA', use_dnssec=False)
            if aaaa_answer:
                result['has_ipv6'] = True
                for rdata in aaaa_answer:
                    ip = str(rdata.address)
                    if ip not in result['ipv6_addresses']:
                        result['ipv6_addresses'].append(ip)

        # Detect providers from NS names
        provider_patterns = {
            'cloudflare': ['cloudflare', 'ns.cloudflare'],
            'aws_route53': ['awsdns', 'amazonaws'],
            'google_cloud': ['googledomains', 'google'],
            'godaddy': ['domaincontrol', 'godaddy'],
            'namecheap': ['namecheap', 'registrar-servers'],
            'digitalocean': ['digitalocean'],
            'azure': ['azure-dns', 'microsoft'],
            'dnsimple': ['dnsimple'],
            'he.net': ['he.net'],
            'ns1': ['ns1.'],
            'ultradns': ['ultradns'],
            'verisign': ['verisign']
        }

        for ns_name in ns_names:
            ns_lower = ns_name.lower()
            for provider, patterns in provider_patterns.items():
                if any(p in ns_lower for p in patterns):
                    if provider not in result['unique_providers']:
                        result['unique_providers'].append(provider)
                    break

        # Calculate diversity score (0-100)
        score = 0
        ns_count = len(result['nameservers'])
        if ns_count >= 2:
            score += 25
        if ns_count >= 4:
            score += 15
        if len(result['unique_tlds']) >= 2:
            score += 20
        if result['has_ipv6']:
            score += 20
        if len(result['ipv4_addresses']) >= 2:
            score += 10
        if len(result['unique_providers']) >= 1:
            score += 10

        result['diversity_score'] = min(score, 100)

        # Generate recommendations
        if ns_count < 2:
            result['recommendations'].append('Add at least 2 nameservers for redundancy')
        if not result['has_ipv6']:
            result['recommendations'].append('Consider adding IPv6 support for nameservers')
        if len(result['unique_tlds']) < 2 and ns_count >= 2:
            result['recommendations'].append('Consider using nameservers from different providers for better resilience')

        return result

    def analyze_dns_provider(self, domain: str) -> Dict[str, Any]:
        """Detect the DNS provider based on nameserver patterns"""
        result = {
            'detected_provider': None,
            'provider_name': 'Unknown',
            'confidence': 'low',
            'nameservers': []
        }

        ns_answer = self._query_safe(domain, 'NS', use_dnssec=False)
        if not ns_answer:
            return result

        ns_names = []
        for rdata in ns_answer:
            ns_name = str(rdata.target).rstrip('.').lower()
            ns_names.append(ns_name)
            result['nameservers'].append(ns_name)

        # Provider detection patterns
        providers = {
            'cloudflare': {
                'patterns': ['cloudflare.com'],
                'name': 'Cloudflare'
            },
            'aws_route53': {
                'patterns': ['awsdns-', 'amazonaws.com'],
                'name': 'Amazon Route 53'
            },
            'google_cloud': {
                'patterns': ['googledomains.com', 'google.com'],
                'name': 'Google Cloud DNS'
            },
            'godaddy': {
                'patterns': ['domaincontrol.com', 'godaddy.com'],
                'name': 'GoDaddy'
            },
            'namecheap': {
                'patterns': ['namecheaphosting.com', 'registrar-servers.com'],
                'name': 'Namecheap'
            },
            'digitalocean': {
                'patterns': ['digitalocean.com'],
                'name': 'DigitalOcean'
            },
            'azure': {
                'patterns': ['azure-dns.', 'microsoft.com'],
                'name': 'Microsoft Azure DNS'
            },
            'dnsimple': {
                'patterns': ['dnsimple.com'],
                'name': 'DNSimple'
            },
            'he_net': {
                'patterns': ['he.net'],
                'name': 'Hurricane Electric'
            },
            'ns1': {
                'patterns': ['nsone.net', 'ns1.'],
                'name': 'NS1'
            },
            'ultradns': {
                'patterns': ['ultradns.'],
                'name': 'UltraDNS'
            },
            'verisign': {
                'patterns': ['verisign'],
                'name': 'Verisign'
            },
            'ovh': {
                'patterns': ['ovh.net'],
                'name': 'OVH'
            },
            'hostgator': {
                'patterns': ['hostgator.com'],
                'name': 'HostGator'
            },
            'bluehost': {
                'patterns': ['bluehost.com'],
                'name': 'Bluehost'
            }
        }

        for provider_id, provider_info in providers.items():
            for ns_name in ns_names:
                if any(pattern in ns_name for pattern in provider_info['patterns']):
                    result['detected_provider'] = provider_id
                    result['provider_name'] = provider_info['name']
                    result['confidence'] = 'high'
                    return result

        # If no specific provider detected, try to identify self-hosted
        for ns_name in ns_names:
            if domain in ns_name:
                result['detected_provider'] = 'self_hosted'
                result['provider_name'] = 'Self-hosted DNS'
                result['confidence'] = 'medium'
                return result

        return result

    def analyze_infrastructure(self, domain: str) -> Dict[str, Any]:
        """Analyze DNS infrastructure (diversity, provider, TTLs)"""
        return {
            'ns_diversity': self.analyze_ns_diversity(domain),
            'provider': self.analyze_dns_provider(domain)
        }

    def analyze_basic_dns(self, domain: str) -> Dict[str, Any]:
        result = {
            'SOA': [],
            'NS': [],
            'A': [],
            'AAAA': [],
            'MX': []
        }

        soa_answer = self._query_safe(domain, 'SOA', use_dnssec=False)
        if soa_answer:
            for rdata in soa_answer:
                result['SOA'].append({
                    'mname': str(rdata.mname).rstrip('.'),
                    'rname': str(rdata.rname).rstrip('.'),
                    'serial': rdata.serial,
                    'refresh': rdata.refresh,
                    'retry': rdata.retry,
                    'expire': rdata.expire,
                    'minimum': rdata.minimum,
                    'ttl': soa_answer.rrset.ttl if hasattr(soa_answer, 'rrset') else None
                })

        ns_answer = self._query_safe(domain, 'NS', use_dnssec=False)
        if ns_answer:
            for rdata in ns_answer:
                result['NS'].append({
                    'nameserver': str(rdata.target).rstrip('.'),
                    'ttl': ns_answer.rrset.ttl if hasattr(ns_answer, 'rrset') else None
                })

        a_answer = self._query_safe(domain, 'A', use_dnssec=False)
        if a_answer:
            for rdata in a_answer:
                result['A'].append({
                    'address': str(rdata.address),
                    'ttl': a_answer.rrset.ttl if hasattr(a_answer, 'rrset') else None
                })

        aaaa_answer = self._query_safe(domain, 'AAAA', use_dnssec=False)
        if aaaa_answer:
            for rdata in aaaa_answer:
                result['AAAA'].append({
                    'address': str(rdata.address),
                    'ttl': aaaa_answer.rrset.ttl if hasattr(aaaa_answer, 'rrset') else None
                })

        mx_answer = self._query_safe(domain, 'MX', use_dnssec=False)
        if mx_answer:
            for rdata in mx_answer:
                result['MX'].append({
                    'exchange': str(rdata.exchange).rstrip('.'),
                    'preference': rdata.preference,
                    'ttl': mx_answer.rrset.ttl if hasattr(mx_answer, 'rrset') else None
                })

        return result

    def analyze_domain(self, domain: str) -> Dict[str, Any]:
        print(f"Analyzing: {domain}")

        result = {
            'domain': domain,
            'timestamp': datetime.now().isoformat(),
            'dns_basic': {},
            'dnssec': {
                'dnskey': {},
                'rrsig': {},
                'nsec': {},
                'ds': {},
                'summary': {}
            },
            'email_security': {},
            'caa': {},
            'infrastructure': {}
        }

        result['dns_basic'] = self.analyze_basic_dns(domain)
        result['dnssec']['dnskey'] = self.analyze_dnskey(domain)
        result['dnssec']['nsec'] = self.analyze_nsec(domain)
        nsec_rrsig = result['dnssec']['nsec'].get('rrsig_records', [])
        result['dnssec']['rrsig'] = self.analyze_rrsig(domain, nsec_rrsig_records=nsec_rrsig)
        result['dnssec']['ds'] = self.analyze_ds(domain)

        result['dnssec']['chain_of_trust'] = self.analyze_chain_of_trust(domain)

        # Phase 2: Email Security (SPF, DKIM, DMARC)
        result['email_security'] = self.analyze_email_security(domain)

        # Phase 2: Certificate Authority Authorization
        result['caa'] = self.analyze_caa(domain)

        # Phase 3: DNS Infrastructure Analysis
        result['infrastructure'] = self.analyze_infrastructure(domain)

        parts = domain.rstrip('.').split('.')
        result['dns_tree'] = {
            'parent_zone': '.'.join(parts[1:]) if len(parts) > 1 else None,
            'level': len(parts),
            'labels': parts
        }

        result['dnssec']['summary'] = {
            'dnssec_enabled': result['dnssec']['dnskey']['present'],
            'has_signatures': result['dnssec']['rrsig']['present'],
            'has_ds_record': result['dnssec']['ds']['present'],
            'nsec_type': result['dnssec']['nsec']['nsec_type'],
            'chain_complete': result['dnssec']['chain_of_trust']['is_complete'],
            'validation_status': self._determine_validation_status(result['dnssec'])
        }

        time.sleep(self.delay)

        return result

    def analyze_domains_from_file(self, input_file: str, output_dir: str = 'dnssec_reports'):
        if not os.path.exists(input_file):
            print(f"ERROR: Input file not found: {input_file}")
            sys.exit(1)

        with open(input_file, 'r') as f:
            domains = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        if not domains:
            print(f"ERROR: No domains found in {input_file}")
            sys.exit(1)

        os.makedirs(output_dir, exist_ok=True)

        print(f"\nDNSSEC Analysis")
        print(f"Total domains: {len(domains)}")
        print(f"DNS server: {self.resolver.nameservers[0]}")
        print(f"Output directory: {output_dir}")
        print(f"Delay between queries: {self.delay}s\n")

        results = {}
        start_time = time.time()

        for i, domain in enumerate(domains, 1):
            print(f"[{i}/{len(domains)}] {domain}")

            try:
                result = self.analyze_domain(domain)
                results[domain] = result

                self._generate_markdown_report(domain, result, output_dir)

                status = result['dnssec']['summary']['validation_status']
                print(f"  Status: {status}")

            except Exception as e:
                print(f"  ERROR: {e}")
                results[domain] = {
                    'domain': domain,
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                }

        summary_file = os.path.join(output_dir, '_summary.json')
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        elapsed = time.time() - start_time
        print(f"\nAnalysis completed")
        print(f"Time elapsed: {elapsed/60:.1f} minutes")
        print(f"Domains analyzed: {len(results)}")
        print(f"Summary saved to: {summary_file}")
        print(f"Individual reports in: {output_dir}/")

        self.results = results
        return results

    def _generate_markdown_report(self, domain: str, result: Dict, output_dir: str):
        if 'error' in result:
            filename = os.path.join(output_dir, f"{domain.replace('.', '_')}.md")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# DNSSEC Analysis Report: {domain}\n\n")
                f.write(f"**Analysis Date:** {result['timestamp']}\n\n")
                f.write(f"## Error\n\n")
                f.write(f"```\n{result['error']}\n```\n")
            return

        filename = os.path.join(output_dir, f"{domain.replace('.', '_')}.md")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# DNSSEC Analysis Report: {domain}\n\n")
            f.write(f"**Analysis Date:** {result['timestamp']}\n\n")

            dns_basic = result.get('dns_basic', {})
            dnssec = result.get('dnssec', {})
            summary = dnssec.get('summary', {})

            f.write("## Summary\n\n")
            f.write(f"- **DNSSEC Enabled:** {summary.get('dnssec_enabled', False)}\n")
            f.write(f"- **Validation Status:** {summary.get('validation_status', 'unknown')}\n")
            f.write(f"- **Has Signatures:** {summary.get('has_signatures', False)}\n")
            f.write(f"- **Has DS Record:** {summary.get('has_ds_record', False)}\n")
            f.write(f"- **NSEC Type:** {summary.get('nsec_type', 'none')}\n\n")

            f.write("---\n\n")

            if dns_basic.get('SOA'):
                f.write("## SOA Records\n\n")
                for soa in dns_basic['SOA']:
                    f.write(f"- **Primary Server:** {soa['mname']}\n")
                    f.write(f"- **Responsible Email:** {soa['rname']}\n")
                    f.write(f"- **Serial:** {soa['serial']}\n")
                    f.write(f"- **Refresh:** {soa['refresh']}s\n")
                    f.write(f"- **Retry:** {soa['retry']}s\n")
                    f.write(f"- **Expire:** {soa['expire']}s\n")
                    f.write(f"- **Minimum TTL:** {soa['minimum']}s\n")
                    f.write(f"- **Record TTL:** {soa['ttl']}s\n\n")

            if dns_basic.get('NS'):
                f.write("## NS Records\n\n")
                f.write(f"Total: {len(dns_basic['NS'])}\n\n")
                for ns in dns_basic['NS']:
                    f.write(f"- {ns['nameserver']} (TTL: {ns['ttl']}s)\n")
                f.write("\n")

            if dns_basic.get('A'):
                f.write("## A Records\n\n")
                f.write(f"Total: {len(dns_basic['A'])}\n\n")
                for a in dns_basic['A']:
                    f.write(f"- {a['address']} (TTL: {a['ttl']}s)\n")
                f.write("\n")

            if dns_basic.get('AAAA'):
                f.write("## AAAA Records\n\n")
                f.write(f"Total: {len(dns_basic['AAAA'])}\n\n")
                for aaaa in dns_basic['AAAA']:
                    f.write(f"- {aaaa['address']} (TTL: {aaaa['ttl']}s)\n")
                f.write("\n")

            if dns_basic.get('MX'):
                f.write("## MX Records\n\n")
                f.write(f"Total: {len(dns_basic['MX'])}\n\n")
                for mx in dns_basic['MX']:
                    f.write(f"- {mx['exchange']} (Priority: {mx['preference']}, TTL: {mx['ttl']}s)\n")
                f.write("\n")

            f.write("---\n\n")
            f.write("# DNSSEC Records\n\n")

            dnskey = dnssec.get('dnskey', {})
            if dnskey.get('present'):
                f.write("## DNSKEY Records\n\n")
                f.write(f"- **Total Keys:** {dnskey['count']}\n")
                f.write(f"- **TTL:** {dnskey['ttl']}s\n\n")

                for i, key in enumerate(dnskey['keys'], 1):
                    f.write(f"### Key {i}\n\n")
                    f.write(f"- **Algorithm:** {key['algorithm_name']} ({key['algorithm']})\n")
                    f.write(f"- **Key Size:** {key['key_size_bits']} bits\n")
                    f.write(f"- **Flags:** {key['flags']}\n")
                    f.write(f"- **Protocol:** {key['protocol']}\n")
                    f.write(f"- **Type:** {'KSK (Key Signing Key)' if key['is_sep'] else 'ZSK (Zone Signing Key)'}\n")
                    f.write(f"- **Zone Key:** {key['is_zone_key']}\n\n")
            else:
                f.write("## DNSKEY Records\n\n")
                f.write("No DNSKEY records found.\n\n")

            rrsig = dnssec.get('rrsig', {})
            if rrsig.get('present'):
                f.write("## RRSIG Records\n\n")
                f.write(f"- **Total Signatures:** {rrsig['count']}\n")
                f.write(f"- **TTL:** {rrsig['ttl']}s\n\n")

                signatures_by_type = rrsig.get('signatures_by_type', {})
                if signatures_by_type:
                    for type_covered, sigs in signatures_by_type.items():
                        f.write(f"### {type_covered} Signatures ({len(sigs)})\n\n")
                        for i, sig in enumerate(sigs, 1):
                            f.write(f"#### Signature {i}\n\n")
                            f.write(f"- **Algorithm:** {sig['algorithm_name']} ({sig['algorithm']})\n")
                            f.write(f"- **Key Tag:** {sig['key_tag']}\n")
                            f.write(f"- **Signer:** {sig['signer']}\n")
                            f.write(f"- **Labels:** {sig['labels']}\n")
                            f.write(f"- **Original TTL:** {sig['original_ttl']}s\n")
                            f.write(f"- **Inception:** {sig['inception']}\n")
                            f.write(f"- **Expiration:** {sig['expiration']}\n")
                            f.write(f"- **Days Until Expiration:** {sig['days_until_expiration']}\n")
                            f.write(f"- **Status:** {'EXPIRED' if sig['is_expired'] else 'VALID'}\n\n")
                else:
                    for i, sig in enumerate(rrsig['signatures'], 1):
                        f.write(f"### Signature {i}\n\n")
                        f.write(f"- **Type Covered:** {sig['type_covered']}\n")
                        f.write(f"- **Algorithm:** {sig['algorithm_name']} ({sig['algorithm']})\n")
                        f.write(f"- **Key Tag:** {sig['key_tag']}\n")
                        f.write(f"- **Signer:** {sig['signer']}\n")
                        f.write(f"- **Inception:** {sig['inception']}\n")
                        f.write(f"- **Expiration:** {sig['expiration']}\n")
                        f.write(f"- **Days Until Expiration:** {sig['days_until_expiration']}\n")
                        f.write(f"- **Status:** {'EXPIRED' if sig['is_expired'] else 'VALID'}\n\n")
            else:
                f.write("## RRSIG Records\n\n")
                f.write("No RRSIG records found.\n\n")

            ds = dnssec.get('ds', {})
            if ds.get('present'):
                f.write("## DS Records\n\n")
                f.write(f"- **Total DS Records:** {ds['count']}\n")
                f.write(f"- **TTL:** {ds['ttl']}s\n\n")

                for i, record in enumerate(ds['records'], 1):
                    f.write(f"### DS Record {i}\n\n")
                    f.write(f"- **Key Tag:** {record['key_tag']}\n")
                    f.write(f"- **Algorithm:** {record['algorithm_name']} ({record['algorithm']})\n")
                    f.write(f"- **Digest Type:** {record['digest_type_name']} ({record['digest_type']})\n")
                    f.write(f"- **Digest:** `{record['digest']}`\n\n")
            else:
                f.write("## DS Records\n\n")
                f.write("No DS records found in parent zone.\n\n")

            nsec = dnssec.get('nsec', {})
            f.write("## NSEC/NSEC3 Records\n\n")
            f.write(f"- **Type:** {nsec.get('nsec_type', 'none').upper()}\n")
            f.write(f"- **NSEC Present:** {nsec.get('nsec_present', False)}\n")
            f.write(f"- **NSEC3 Present:** {nsec.get('nsec3_present', False)}\n")
            f.write(f"- **NSEC3PARAM Present:** {nsec.get('nsec3param_present', False)}\n")
            f.write(f"- **Opt-Out:** {nsec.get('opt_out', False)}\n\n")

            if nsec.get('details'):
                if 'nsec' in nsec['details']:
                    nsec_data = nsec['details']['nsec']
                    f.write("### NSEC Details\n\n")
                    f.write(f"- **Count:** {nsec_data.get('count', 0)}\n")
                    f.write(f"- **TTL:** {nsec_data.get('ttl', 'N/A')}s\n\n")

                if 'nsec3' in nsec['details']:
                    nsec3_data = nsec['details']['nsec3']
                    f.write("### NSEC3 Details\n\n")
                    f.write(f"- **Count:** {nsec3_data.get('count', 0)}\n")
                    f.write(f"- **TTL:** {nsec3_data.get('ttl', 'N/A')}s\n\n")

                    for i, record in enumerate(nsec3_data.get('records', []), 1):
                        f.write(f"#### NSEC3 Record {i}\n\n")
                        f.write(f"- **Hash Algorithm:** {record['hash_algorithm']}\n")
                        f.write(f"- **Flags:** {record['flags']}\n")
                        f.write(f"- **Iterations:** {record['iterations']}\n")
                        f.write(f"- **Salt:** {record['salt']}\n\n")

                if 'nsec3param' in nsec['details']:
                    nsec3param_data = nsec['details']['nsec3param']
                    f.write("### NSEC3PARAM Details\n\n")
                    f.write(f"- **Count:** {nsec3param_data.get('count', 0)}\n")
                    f.write(f"- **TTL:** {nsec3param_data.get('ttl', 'N/A')}s\n\n")

                    for i, record in enumerate(nsec3param_data.get('records', []), 1):
                        f.write(f"#### NSEC3PARAM Record {i}\n\n")
                        f.write(f"- **Hash Algorithm:** {record['hash_algorithm']}\n")
                        f.write(f"- **Flags:** {record['flags']}\n")
                        f.write(f"- **Iterations:** {record['iterations']}\n")
                        f.write(f"- **Salt:** {record['salt']}\n\n")

            f.write("---\n\n")
            f.write("## DNS Tree Structure\n\n")

            parts = domain.split('.')
            if len(parts) > 1:
                parent = '.'.join(parts[1:])
                f.write(f"- **Domain:** {domain}\n")
                f.write(f"- **Parent Zone:** {parent}\n")
                f.write(f"- **Level:** {len(parts)}\n\n")

                if dns_basic.get('NS'):
                    f.write("### Nameserver Hierarchy\n\n")
                    f.write("```\n")
                    f.write(f"{domain}\n")
                    for i, ns in enumerate(dns_basic['NS']):
                        prefix = "└──" if i == len(dns_basic['NS']) - 1 else "├──"
                        f.write(f"{prefix} {ns['nameserver']} (TTL: {ns['ttl']}s)\n")
                    f.write("```\n\n")

                f.write("### Cryptographic Chain of Trust\n\n")
                if ds.get('present'):
                    f.write(f"DS record exists in parent zone ({parent}), establishing cryptographic chain of trust.\n\n")
                    f.write("```\n")
                    f.write(f"{parent} (parent zone)\n")
                    f.write(f"  └── DS Record → {domain}\n")
                    for record in ds['records']:
                        f.write(f"      └── KeyTag: {record['key_tag']}, Algorithm: {record['algorithm_name']}\n")
                    f.write("```\n\n")
                else:
                    f.write(f"No DS record found in parent zone ({parent}). Chain of trust not established.\n\n")

            chain_data = dnssec.get('chain_of_trust', {})
            if chain_data:
                f.write("### Full Chain of Trust to Root\n\n")
                f.write("| Zone | DNSKEY | DS | RRSIG | Status |\n")
                f.write("|------|--------|----|----- |--------|\n")
                for zone_info in chain_data.get('chain', []):
                    zone = zone_info['zone']
                    dnskey_status = 'Yes' if zone_info['has_dnskey'] else 'No'
                    ds_status = 'N/A' if zone == '.' else ('Yes' if zone_info['has_ds'] else 'No')
                    rrsig_status = 'Yes' if zone_info['has_rrsig'] else 'No'
                    if zone == '.':
                        status = 'Signed (Root)'
                    elif zone_info['is_signed']:
                        status = 'Signed'
                    else:
                        status = 'Unsigned'
                    f.write(f"| {zone} | {dnskey_status} | {ds_status} | {rrsig_status} | {status} |\n")
                f.write("\n")

                if chain_data.get('is_complete'):
                    f.write("**Chain Status:** Complete - Full trust path to root\n")
                else:
                    f.write(f"**Chain Status:** Broken at `{chain_data.get('broken_at')}`\n")

    def _determine_validation_status(self, dnssec: Dict) -> str:
        dnskey_present = dnssec.get('dnskey', {}).get('present', False)
        rrsig_present = dnssec.get('rrsig', {}).get('present', False)
        ds_present = dnssec.get('ds', {}).get('present', False)

        if not dnskey_present:
            return 'disabled'

        if dnskey_present and rrsig_present and ds_present:
            signatures = dnssec.get('rrsig', {}).get('signatures', [])
            if any(sig.get('is_expired', False) for sig in signatures):
                return 'enabled_incomplete'
            return 'valid'

        return 'enabled_incomplete'

    def _calculate_key_size(self, dnskey_rdata) -> int:
        try:
            key_bytes = len(dnskey_rdata.key)

            if dnskey_rdata.algorithm in [5, 7, 8, 10]:
                return key_bytes * 8
            elif dnskey_rdata.algorithm == 13:
                return 256
            elif dnskey_rdata.algorithm == 14:
                return 384
            elif dnskey_rdata.algorithm == 15:
                return 256
            elif dnskey_rdata.algorithm == 16:
                return 448
            else:
                return key_bytes * 8
        except:
            return 0

    def _get_algorithm_name(self, num: int) -> str:
        algorithms = {
            1: 'RSA/MD5',
            3: 'DSA/SHA-1',
            5: 'RSA/SHA-1',
            6: 'DSA-NSEC3-SHA1',
            7: 'RSASHA1-NSEC3-SHA1',
            8: 'RSA/SHA-256',
            10: 'RSA/SHA-512',
            12: 'GOST R 34.10-2001',
            13: 'ECDSA-P256/SHA-256',
            14: 'ECDSA-P384/SHA-384',
            15: 'Ed25519',
            16: 'Ed448'
        }
        return algorithms.get(num, f'Unknown-{num}')

    def _get_digest_type_name(self, num: int) -> str:
        digest_types = {
            1: 'SHA-1',
            2: 'SHA-256',
            3: 'GOST R 34.11-94',
            4: 'SHA-384'
        }
        return digest_types.get(num, f'Unknown-{num}')


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 dnssec_analyzer.py <domains_file.txt> [output_directory]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'dnssec_reports'

    analyzer = DNSSECAnalyzer(
        nameserver='8.8.8.8',
        delay_seconds=1.5,
        timeout=10
    )

    analyzer.analyze_domains_from_file(input_file, output_dir)


if __name__ == '__main__':
    main()
