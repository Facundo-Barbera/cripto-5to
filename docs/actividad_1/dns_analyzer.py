#!/usr/bin/env python3
"""
Analizador de Tráfico DNS desde archivos PCAP
Extrae y analiza registros DNS (SOA, NS, A, AAAA, CNAME)
"""

from scapy.all import rdpcap, DNS, DNSQR, DNSRR
from collections import defaultdict
import json
import sys

class DNSAnalyzer:
    def __init__(self, pcap_file):
        self.pcap_file = pcap_file
        self.packets = None
        self.domain_stats = defaultdict(lambda: {
            'SOA': [],
            'NS': [],
            'A': [],
            'AAAA': [],
            'CNAME': [],
            'queries': 0,
            'responses': 0
        })
        
    def load_pcap(self):
        """Carga el archivo PCAP"""
        try:
            print(f"[+] Cargando {self.pcap_file}...")
            self.packets = rdpcap(self.pcap_file)
            print(f"[+] {len(self.packets)} paquetes cargados")
            return True
        except Exception as e:
            print(f"[-] Error al cargar PCAP: {e}")
            return False
    
    def analyze_packets(self):
        """Analiza todos los paquetes DNS"""
        if not self.packets:
            return
        
        dns_packets = [pkt for pkt in self.packets if pkt.haslayer(DNS)]
        print(f"[+] {len(dns_packets)} paquetes DNS encontrados")
        
        for pkt in dns_packets:
            self._process_dns_packet(pkt)
    
    def _process_dns_packet(self, pkt):
        """Procesa un paquete DNS individual"""
        dns = pkt[DNS]
        qname = None
        
        # Procesar queries
        if dns.qd:
            try:
                qname = dns.qd.qname.decode('utf-8', errors='ignore').rstrip('.')
                self.domain_stats[qname]['queries'] += 1
            except:
                pass
        
        # Procesar respuestas (Resource Records)
        if dns.an and qname:
            self.domain_stats[qname]['responses'] += 1
            self._extract_records(dns, qname)
    
    def _extract_records(self, dns, domain):
        """Extrae información de los registros DNS"""
        # Procesar Answer Section
        for i in range(dns.ancount):
            rr = dns.an[i]
            self._process_rr(rr, domain)
        
        # Procesar Authority Section (NS records)
        if dns.ns:
            for i in range(dns.nscount):
                rr = dns.ns[i]
                self._process_rr(rr, domain)
        
        # Procesar Additional Section
        if dns.ar:
            for i in range(dns.arcount):
                rr = dns.ar[i]
                self._process_rr(rr, domain)
    
    def _process_rr(self, rr, domain):
        """Procesa un Resource Record"""
        try:
            rname = rr.rrname.decode('utf-8', errors='ignore').rstrip('.')
            rtype = rr.type
            ttl = rr.ttl
            
            record_info = {
                'name': rname,
                'ttl': ttl,
                'type_code': rtype
            }
            
            # Tipo 1: A (IPv4)
            if rtype == 1:
                record_info['address'] = rr.rdata
                self.domain_stats[domain]['A'].append(record_info)
            
            # Tipo 2: NS (Name Server)
            elif rtype == 2:
                record_info['nameserver'] = rr.rdata.decode('utf-8', errors='ignore').rstrip('.')
                self.domain_stats[domain]['NS'].append(record_info)
            
            # Tipo 5: CNAME
            elif rtype == 5:
                record_info['cname'] = rr.rdata.decode('utf-8', errors='ignore').rstrip('.')
                self.domain_stats[domain]['CNAME'].append(record_info)
            
            # Tipo 6: SOA (Start of Authority)
            elif rtype == 6:
                soa_data = {
                    'name': rname,
                    'ttl': ttl,
                    'mname': rr.mname.decode('utf-8', errors='ignore').rstrip('.'),
                    'rname': rr.rname.decode('utf-8', errors='ignore').rstrip('.'),
                    'serial': rr.serial,
                    'refresh': rr.refresh,
                    'retry': rr.retry,
                    'expire': rr.expire,
                    'minimum': rr.minimum
                }
                self.domain_stats[domain]['SOA'].append(soa_data)
            
            # Tipo 28: AAAA (IPv6)
            elif rtype == 28:
                record_info['address'] = rr.rdata
                self.domain_stats[domain]['AAAA'].append(record_info)
                
        except Exception as e:
            pass  # Ignorar errores en registros individuales
    
    def generate_report(self):
        """Genera reporte de análisis"""
        print("\n" + "="*70)
        print("REPORTE DE ANÁLISIS DNS")
        print("="*70)
        
        for domain, stats in self.domain_stats.items():
            if not domain or domain == '':
                continue
                
            print(f"\n{'─'*70}")
            print(f"DOMINIO: {domain}")
            print(f"{'─'*70}")
            print(f"Consultas realizadas: {stats['queries']}")
            print(f"Respuestas recibidas: {stats['responses']}")
            
            # SOA Records
            if stats['SOA']:
                print(f"\n   REGISTROS SOA ({len(stats['SOA'])}):")
                for soa in stats['SOA']:
                    print(f"    - Servidor primario: {soa['mname']}")
                    print(f"    - Email responsable: {soa['rname']}")
                    print(f"    - Serial: {soa['serial']}")
                    print(f"    - Refresh: {soa['refresh']}s")
                    print(f"    - Retry: {soa['retry']}s")
                    print(f"    - Expire: {soa['expire']}s")
                    print(f"    - Minimum TTL: {soa['minimum']}s")
                    print(f"    - TTL del registro: {soa['ttl']}s")
            
            # NS Records
            if stats['NS']:
                print(f"\n   REGISTROS NS ({len(stats['NS'])}):")
                for ns in stats['NS']:
                    print(f"    - {ns['nameserver']} (TTL: {ns['ttl']}s)")
            
            # A Records
            if stats['A']:
                print(f"\n   REGISTROS A ({len(stats['A'])}):")
                for a in stats['A']:
                    print(f"    - {a['address']} (TTL: {a['ttl']}s)")
            
            # AAAA Records
            if stats['AAAA']:
                print(f"\n   REGISTROS AAAA ({len(stats['AAAA'])}):")
                for aaaa in stats['AAAA']:
                    print(f"    - {aaaa['address']} (TTL: {aaaa['ttl']}s)")
            
            # CNAME Records
            if stats['CNAME']:
                print(f"\n  🔗 REGISTROS CNAME ({len(stats['CNAME'])}):")
                for cname in stats['CNAME']:
                    print(f"    - {cname['cname']} (TTL: {cname['ttl']}s)")
            
            # Resumen
            print(f"\n   RESUMEN:")
            print(f"    - Total NS: {len(stats['NS'])}")
            print(f"    - Total A: {len(stats['A'])}")
            print(f"    - Total AAAA: {len(stats['AAAA'])}")
            print(f"    - Total CNAME: {len(stats['CNAME'])}")
            print(f"    - Total SOA: {len(stats['SOA'])}")
    
    def export_json(self, output_file='dns_analysis.json'):
        """Exporta resultados a JSON"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(dict(self.domain_stats), f, indent=2, default=str)
            print(f"\n[+] Resultados exportados a {output_file}")
        except Exception as e:
            print(f"[-] Error al exportar JSON: {e}")
    
    def generate_dns_tree(self):
        """Genera árbol DNS de dependencias"""
        print("\n" + "="*70)
        print("ÁRBOL DNS DE DEPENDENCIAS")
        print("="*70)
        
        for domain, stats in self.domain_stats.items():
            if not domain or not stats['NS']:
                continue
            
            print(f"\n{domain}")
            print("  │")
            
            # Mostrar NS
            for i, ns in enumerate(stats['NS']):
                is_last = (i == len(stats['NS']) - 1)
                prefix = "  └── " if is_last else "  ├── "
                print(f"{prefix}NS: {ns['nameserver']}")
                
                # Buscar IPs de los NS
                ns_domain = ns['nameserver']
                if ns_domain in self.domain_stats:
                    ns_ips = self.domain_stats[ns_domain]['A']
                    for j, ip in enumerate(ns_ips):
                        ip_prefix = "      └── " if j == len(ns_ips) - 1 else "      ├── "
                        print(f"{ip_prefix}IP: {ip['address']}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 dns_analyzer.py <archivo.pcap>")
        sys.exit(1)
    
    pcap_file = sys.argv[1]
    
    analyzer = DNSAnalyzer(pcap_file)
    
    if analyzer.load_pcap():
        analyzer.analyze_packets()
        analyzer.generate_report()
        analyzer.generate_dns_tree()
        analyzer.export_json()
    else:
        print("[-] No se pudo analizar el archivo")
        sys.exit(1)


if __name__ == "__main__":
    main()
