#!/usr/bin/env python3

import sys
import json
from typing import Dict, List, Any
from datetime import datetime

try:
    from .generator import DNSSECAnalyzer
except ImportError:
    from analyzer.generator import DNSSECAnalyzer


class RFCCheck:

    def __init__(self, rfc: str, check_id: str, description: str):
        self.rfc = rfc
        self.check_id = check_id
        self.description = description
        self.passed = None
        self.details = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            'rfc': self.rfc,
            'check_id': self.check_id,
            'description': self.description,
            'passed': self.passed,
            'details': self.details
        }


class RFCValidator:

    DEPRECATED_ALGORITHMS = [1, 3, 6]
    RECOMMENDED_ALGORITHMS = [13, 14, 15, 16]
    VALID_DIGEST_TYPES = [1, 2, 4]
    RECOMMENDED_DIGEST_TYPES = [2, 4]

    def __init__(self):
        self.analyzer = DNSSECAnalyzer(nameserver='8.8.8.8', delay_seconds=0.5, timeout=10)
        self.checks = []
        self.analysis_data = None

    def validate(self, domain: str) -> Dict[str, Any]:
        self.checks = []
        self.analysis_data = self.analyzer.analyze_domain(domain)
        self._run_all_checks()
        return self._build_result()

    def _run_all_checks(self):
        self._check_rfc4034_dnskey_protocol()
        self._check_rfc4034_dnskey_flags()
        self._check_rfc4034_ksk_sep_bit()
        self._check_rfc4034_rrsig_signer()
        self._check_rfc4034_rrsig_labels()
        self._check_rfc4034_ds_digest_type()
        self._check_rfc4034_ds_algorithm_match()
        self._check_rfc4034_nsec_presence()
        self._check_rfc4035_chain_of_trust()
        self._check_rfc4035_ds_in_parent()
        self._check_rfc4035_valid_signatures()
        self._check_rfc4035_dnskey_rrsig()
        self._check_rfc4035_signature_timing()
        self._check_rfc6840_no_rsamd5()
        self._check_rfc6840_no_dsa()
        self._check_rfc6840_nsec3_iterations()
        self._check_rfc6840_nsec3_salt()
        self._check_rfc9364_recommended_algorithm()
        self._check_rfc9364_key_size()
        self._check_rfc9364_digest_algorithm()
        self._check_rfc9364_signature_lifetime()

    def _build_result(self) -> Dict[str, Any]:
        passed = sum(1 for c in self.checks if c.passed is True)
        failed = sum(1 for c in self.checks if c.passed is False)
        total = passed + failed

        return {
            'domain': self.analysis_data['domain'],
            'timestamp': datetime.now().isoformat(),
            'analysis': self.analysis_data,
            'rfc_compliance': {
                'score': f"{passed}/{total}",
                'passed': passed,
                'failed': failed,
                'total': total,
                'not_applicable': sum(1 for c in self.checks if c.passed is None),
                'percentage': round(passed / total * 100, 1) if total > 0 else 0,
                'checks': [c.to_dict() for c in self.checks],
                'by_rfc': self._group_by_rfc()
            }
        }

    def _group_by_rfc(self) -> Dict[str, List[Dict]]:
        grouped = {}
        for check in self.checks:
            if check.rfc not in grouped:
                grouped[check.rfc] = []
            grouped[check.rfc].append(check.to_dict())
        return grouped

    def _get_dnskey(self) -> Dict:
        return self.analysis_data.get('dnssec', {}).get('dnskey', {})

    def _get_rrsig(self) -> Dict:
        return self.analysis_data.get('dnssec', {}).get('rrsig', {})

    def _get_ds(self) -> Dict:
        return self.analysis_data.get('dnssec', {}).get('ds', {})

    def _get_nsec(self) -> Dict:
        return self.analysis_data.get('dnssec', {}).get('nsec', {})

    def _get_chain(self) -> Dict:
        return self.analysis_data.get('dnssec', {}).get('chain_of_trust', {})

    def _check_rfc4034_dnskey_protocol(self):
        check = RFCCheck('RFC4034', '4034-01', 'DNSKEY protocol field is 3')
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'No DNSKEY records present'
        else:
            keys = dnskey.get('keys', [])
            all_valid = all(k.get('protocol') == 3 for k in keys)
            check.passed = all_valid
            check.details = 'All DNSKEY records have protocol=3' if all_valid else 'Invalid protocol value found'

        self.checks.append(check)

    def _check_rfc4034_dnskey_flags(self):
        check = RFCCheck('RFC4034', '4034-02', 'DNSKEY flags have Zone Key bit set')
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'No DNSKEY records present'
        else:
            keys = dnskey.get('keys', [])
            all_valid = all(k.get('is_zone_key', False) for k in keys)
            check.passed = all_valid
            check.details = 'All keys have Zone Key flag' if all_valid else 'Missing Zone Key flag on some keys'

        self.checks.append(check)

    def _check_rfc4034_ksk_sep_bit(self):
        check = RFCCheck('RFC4034', '4034-03', 'KSK has SEP bit set')
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'No DNSKEY records present'
        else:
            keys = dnskey.get('keys', [])
            ksks = [k for k in keys if k.get('flags') == 257]
            if not ksks:
                check.passed = None
                check.details = 'No KSK (flag 257) found'
            else:
                check.passed = True
                check.details = f'Found {len(ksks)} KSK(s) with SEP bit'

        self.checks.append(check)

    def _check_rfc4034_rrsig_signer(self):
        check = RFCCheck('RFC4034', '4034-04', 'RRSIG signer name matches zone')
        rrsig = self._get_rrsig()
        domain = self.analysis_data['domain']

        if not rrsig.get('present'):
            check.passed = None
            check.details = 'No RRSIG records present'
        else:
            sigs = rrsig.get('signatures', [])
            signers = [s.get('signer') for s in sigs]
            valid = all(s == domain or domain.endswith('.' + s) for s in signers if s)
            check.passed = valid
            check.details = f'Signers: {list(set(signers))}' if valid else f'Mismatched signers: {signers}'

        self.checks.append(check)

    def _check_rfc4034_rrsig_labels(self):
        check = RFCCheck('RFC4034', '4034-05', 'RRSIG labels count is valid')
        rrsig = self._get_rrsig()
        domain = self.analysis_data['domain']
        domain_labels = len(domain.rstrip('.').split('.'))

        if not rrsig.get('present'):
            check.passed = None
            check.details = 'No RRSIG records present'
        else:
            sigs = rrsig.get('signatures', [])
            labels = [s.get('labels') for s in sigs]
            valid = all(l is not None and l <= domain_labels for l in labels)
            check.passed = valid
            check.details = f'Label counts valid (domain has {domain_labels})' if valid else 'Invalid label count'

        self.checks.append(check)

    def _check_rfc4034_ds_digest_type(self):
        check = RFCCheck('RFC4034', '4034-06', 'DS digest type is valid')
        ds = self._get_ds()

        if not ds.get('present'):
            check.passed = None
            check.details = 'No DS records present'
        else:
            records = ds.get('records', [])
            digest_types = [r.get('digest_type') for r in records]
            valid = all(dt in self.VALID_DIGEST_TYPES for dt in digest_types)
            check.passed = valid
            check.details = f'Digest types: {digest_types}' if valid else f'Invalid digest types: {digest_types}'

        self.checks.append(check)

    def _check_rfc4034_ds_algorithm_match(self):
        check = RFCCheck('RFC4034', '4034-07', 'DS algorithm matches DNSKEY')
        ds = self._get_ds()
        dnskey = self._get_dnskey()

        if not ds.get('present') or not dnskey.get('present'):
            check.passed = None
            check.details = 'DS or DNSKEY not present'
        else:
            ds_algos = set(r.get('algorithm') for r in ds.get('records', []))
            key_algos = set(k.get('algorithm') for k in dnskey.get('keys', []))
            matching = ds_algos.intersection(key_algos)
            check.passed = len(matching) > 0
            check.details = f'Matching algorithms: {matching}' if matching else f'DS: {ds_algos}, DNSKEY: {key_algos}'

        self.checks.append(check)

    def _check_rfc4034_nsec_presence(self):
        check = RFCCheck('RFC4034', '4034-08', 'NSEC/NSEC3 present for signed zone')
        dnskey = self._get_dnskey()
        nsec = self._get_nsec()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'Zone not signed (no DNSKEY)'
        else:
            has_nsec = nsec.get('nsec_present') or nsec.get('nsec3_present')
            check.passed = has_nsec
            nsec_type = nsec.get('nsec_type', 'none')
            check.details = f'Using {nsec_type}' if has_nsec else 'No authenticated denial of existence'

        self.checks.append(check)

    def _check_rfc4035_chain_of_trust(self):
        check = RFCCheck('RFC4035', '4035-01', 'Chain of trust is complete to root')
        chain = self._get_chain()

        if not chain:
            check.passed = None
            check.details = 'Chain of trust data not available'
        else:
            check.passed = chain.get('is_complete', False)
            if check.passed:
                check.details = f'Complete chain through {chain.get("depth")} levels'
            else:
                check.details = f'Chain broken at: {chain.get("broken_at")}'

        self.checks.append(check)

    def _check_rfc4035_ds_in_parent(self):
        check = RFCCheck('RFC4035', '4035-02', 'DS record exists in parent zone')
        ds = self._get_ds()
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'Zone not signed'
        else:
            check.passed = ds.get('present', False)
            check.details = f'DS records: {ds.get("count", 0)}' if check.passed else 'No DS in parent zone'

        self.checks.append(check)

    def _check_rfc4035_valid_signatures(self):
        check = RFCCheck('RFC4035', '4035-03', 'At least one valid (non-expired) signature')
        rrsig = self._get_rrsig()

        if not rrsig.get('present'):
            check.passed = None
            check.details = 'No signatures present'
        else:
            sigs = rrsig.get('signatures', [])
            valid_sigs = [s for s in sigs if not s.get('is_expired', True)]
            check.passed = len(valid_sigs) > 0
            check.details = f'{len(valid_sigs)}/{len(sigs)} signatures valid' if check.passed else 'All signatures expired'

        self.checks.append(check)

    def _check_rfc4035_dnskey_rrsig(self):
        check = RFCCheck('RFC4035', '4035-04', 'DNSKEY has corresponding RRSIG')
        rrsig = self._get_rrsig()
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'No DNSKEY present'
        else:
            sigs_by_type = rrsig.get('signatures_by_type', {})
            has_dnskey_sig = 'DNSKEY' in sigs_by_type
            check.passed = has_dnskey_sig
            check.details = 'DNSKEY is signed' if has_dnskey_sig else 'No RRSIG for DNSKEY'

        self.checks.append(check)

    def _check_rfc4035_signature_timing(self):
        check = RFCCheck('RFC4035', '4035-05', 'Signature timing is valid')
        rrsig = self._get_rrsig()

        if not rrsig.get('present'):
            check.passed = None
            check.details = 'No signatures present'
        else:
            sigs = rrsig.get('signatures', [])
            valid = True
            for sig in sigs:
                if sig.get('is_expired'):
                    valid = False
                    break
            check.passed = valid
            check.details = 'All signatures within validity period' if valid else 'Timing issues found'

        self.checks.append(check)

    def _check_rfc6840_no_rsamd5(self):
        check = RFCCheck('RFC6840', '6840-01', 'No RSA/MD5 algorithm (algorithm 1)')
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'No DNSKEY present'
        else:
            keys = dnskey.get('keys', [])
            algos = [k.get('algorithm') for k in keys]
            has_rsamd5 = 1 in algos
            check.passed = not has_rsamd5
            check.details = 'RSA/MD5 not in use' if not has_rsamd5 else 'INSECURE: RSA/MD5 in use'

        self.checks.append(check)

    def _check_rfc6840_no_dsa(self):
        check = RFCCheck('RFC6840', '6840-02', 'No DSA algorithms (3, 6)')
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'No DNSKEY present'
        else:
            keys = dnskey.get('keys', [])
            algos = [k.get('algorithm') for k in keys]
            has_dsa = any(a in [3, 6] for a in algos)
            check.passed = not has_dsa
            check.details = 'DSA not in use' if not has_dsa else 'DEPRECATED: DSA in use'

        self.checks.append(check)

    def _check_rfc6840_nsec3_iterations(self):
        check = RFCCheck('RFC6840', '6840-03', 'NSEC3 iterations within limits (max 150)')
        nsec = self._get_nsec()

        if nsec.get('nsec_type') != 'NSEC3':
            check.passed = None
            check.details = 'Not using NSEC3'
        else:
            details = nsec.get('details', {})
            nsec3_records = details.get('nsec3', {}).get('records', [])
            nsec3param = details.get('nsec3param', {}).get('records', [])
            all_records = nsec3_records + nsec3param

            if not all_records:
                check.passed = None
                check.details = 'No NSEC3 iteration data'
            else:
                iterations = [r.get('iterations', 0) for r in all_records]
                max_iter = max(iterations)
                if max_iter > 150:
                    check.passed = False
                    check.details = f'Iterations too high: {max_iter} (max: 150)'
                elif max_iter > 0:
                    check.passed = True
                    check.details = f'Iterations: {max_iter} (acceptable, optimal: 0)'
                else:
                    check.passed = True
                    check.details = 'Optimal: iterations = 0'

        self.checks.append(check)

    def _check_rfc6840_nsec3_salt(self):
        check = RFCCheck('RFC6840', '6840-04', 'NSEC3 salt length reasonable')
        nsec = self._get_nsec()

        if nsec.get('nsec_type') != 'NSEC3':
            check.passed = None
            check.details = 'Not using NSEC3'
        else:
            details = nsec.get('details', {})
            nsec3param = details.get('nsec3param', {}).get('records', [])

            if not nsec3param:
                check.passed = None
                check.details = 'No NSEC3PARAM data'
            else:
                salts = [r.get('salt', 'none') for r in nsec3param]
                salt_lengths = [len(s) // 2 if s != 'none' else 0 for s in salts]
                max_salt = max(salt_lengths) if salt_lengths else 0

                if max_salt == 0:
                    check.passed = True
                    check.details = 'No salt (optimal per RFC 9276)'
                elif max_salt <= 8:
                    check.passed = True
                    check.details = f'Salt length: {max_salt} bytes (acceptable)'
                else:
                    check.passed = False
                    check.details = f'Salt too long: {max_salt} bytes (max recommended: 8)'

        self.checks.append(check)

    def _check_rfc9364_recommended_algorithm(self):
        check = RFCCheck('RFC9364', '9364-01', 'Uses recommended algorithm (ECDSA or EdDSA)')
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'No DNSKEY present'
        else:
            keys = dnskey.get('keys', [])
            algos = [k.get('algorithm') for k in keys]
            all_recommended = all(a in self.RECOMMENDED_ALGORITHMS for a in algos)

            if all_recommended:
                check.passed = True
                algo_names = [k.get('algorithm_name') for k in keys]
                check.details = f'Using: {list(set(algo_names))}'
            else:
                check.passed = False
                non_rec = [k.get('algorithm_name') for k in keys if k.get('algorithm') not in self.RECOMMENDED_ALGORITHMS]
                check.details = f'Non-recommended: {list(set(non_rec))}'

        self.checks.append(check)

    def _check_rfc9364_key_size(self):
        check = RFCCheck('RFC9364', '9364-02', 'Key sizes meet minimum requirements')
        dnskey = self._get_dnskey()

        if not dnskey.get('present'):
            check.passed = None
            check.details = 'No DNSKEY present'
        else:
            keys = dnskey.get('keys', [])
            issues = []
            for k in keys:
                algo = k.get('algorithm')
                size = k.get('key_size_bits', 0)
                if algo in [5, 7, 8, 10] and size < 2048:
                    issues.append(f'RSA key {size} bits < 2048')

            if not issues:
                check.passed = True
                check.details = 'All key sizes adequate'
            else:
                check.passed = False
                check.details = '; '.join(issues)

        self.checks.append(check)

    def _check_rfc9364_digest_algorithm(self):
        check = RFCCheck('RFC9364', '9364-03', 'DS uses SHA-256 or SHA-384')
        ds = self._get_ds()

        if not ds.get('present'):
            check.passed = None
            check.details = 'No DS records present'
        else:
            records = ds.get('records', [])
            digest_types = [r.get('digest_type') for r in records]
            has_strong = any(dt in self.RECOMMENDED_DIGEST_TYPES for dt in digest_types)
            has_sha1 = 1 in digest_types

            if has_strong and not has_sha1:
                check.passed = True
                check.details = 'Using strong digest algorithms only'
            elif has_strong:
                check.passed = True
                check.details = 'Has SHA-256/384 (also has SHA-1 for compatibility)'
            else:
                check.passed = False
                check.details = 'Using only SHA-1, recommend SHA-256 or SHA-384'

        self.checks.append(check)

    def _check_rfc9364_signature_lifetime(self):
        check = RFCCheck('RFC9364', '9364-04', 'Signature validity period reasonable')
        rrsig = self._get_rrsig()

        if not rrsig.get('present'):
            check.passed = None
            check.details = 'No signatures present'
        else:
            sigs = rrsig.get('signatures', [])
            days = [s.get('days_until_expiration', 0) for s in sigs if not s.get('is_expired')]

            if not days:
                check.passed = False
                check.details = 'No valid signatures'
            else:
                max_days = max(days)
                if max_days <= 30:
                    check.passed = True
                    check.details = f'Max validity: {max_days} days (good)'
                elif max_days <= 90:
                    check.passed = True
                    check.details = f'Max validity: {max_days} days (acceptable)'
                else:
                    check.passed = False
                    check.details = f'Max validity: {max_days} days (too long, recommend < 30)'

        self.checks.append(check)

    def print_console(self, result: Dict[str, Any]):
        domain = result['domain']
        compliance = result['rfc_compliance']

        print("=" * 80)
        print(f"{'DNSSEC RFC Compliance Report: ' + domain:^80}")
        print("=" * 80)
        print(f"\nAnalysis Timestamp: {result['timestamp']}\n")

        by_rfc = compliance['by_rfc']

        rfc_names = {
            'RFC4033': 'RFC 4033 - DNS Security Introduction and Requirements',
            'RFC4034': 'RFC 4034 - Resource Records for DNS Security Extensions',
            'RFC4035': 'RFC 4035 - Protocol Modifications for DNS Security Extensions',
            'RFC6840': 'RFC 6840 - Clarifications and Implementation Notes',
            'RFC9364': 'RFC 9364 - Current DNSSEC Operational Practices'
        }

        for rfc in ['RFC4034', 'RFC4035', 'RFC6840', 'RFC9364']:
            if rfc not in by_rfc:
                continue

            print("-" * 80)
            print(rfc_names.get(rfc, rfc))
            print("-" * 80)

            for check in by_rfc[rfc]:
                if check['passed'] is True:
                    status = '[PASS]'
                elif check['passed'] is False:
                    status = '[FAIL]'
                else:
                    status = '[N/A] '

                print(f"{status} {check['check_id']}: {check['description']}")
                if check['details'] and check['passed'] is False:
                    print(f"       -> {check['details']}")

            print()

        print("=" * 80)
        print(f"{'SUMMARY':^80}")
        print("=" * 80)
        print(f"\nScore: {compliance['score']} checks passed ({compliance['percentage']}%)")
        print(f"\nBy RFC:")

        for rfc in ['RFC4034', 'RFC4035', 'RFC6840', 'RFC9364']:
            if rfc not in by_rfc:
                continue
            checks = by_rfc[rfc]
            passed = sum(1 for c in checks if c['passed'] is True)
            total = sum(1 for c in checks if c['passed'] is not None)
            print(f"  {rfc}: {passed}/{total} passed")

        print(f"\nLegend: [PASS] = Compliant  [FAIL] = Non-compliant  [N/A] = Not Applicable")
        print("=" * 80)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 rfc_validator.py <domain>")
        print("Example: python3 rfc_validator.py unam.mx")
        sys.exit(1)

    domain = sys.argv[1]

    validator = RFCValidator()
    result = validator.validate(domain)

    validator.print_console(result)

    output_file = f"{domain.replace('.', '_')}_rfc_validation.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {output_file}")


if __name__ == '__main__':
    main()
