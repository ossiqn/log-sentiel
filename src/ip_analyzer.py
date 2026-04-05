"""
Log Sentinel — Akıllı Log Avcısı
Module  : IP Intelligence
Author  : OSSiqn Team
GitHub  : https://github.com/ossiqn
License : MIT © 2024 OSSiqn

Açıklama (TR):
IP adreslerini analiz eder, GeoIP bilgilerini ceker.

Description (EN):
Analyzes IP addresses and fetches GeoIP information.

This file was produced by OSSiqn — github.com/ossiqn
"""

import requests

class IPAnalyzer:
    def __init__(self, config):
        self.config = config
        self.cache = {}
    
    def analyze_ip(self, ip_address):
        if ip_address in self.cache:
            return self.cache[ip_address]
        try:
            resp = requests.get(f'http://ip-api.com/json/{ip_address}', timeout=5)
            if resp.status_code == 200:
                data = resp.json()
                result = {
                    'country': data.get('country', 'Unknown'),
                    'isp': data.get('isp', 'Unknown')
                }
                self.cache[ip_address] = result
                return result
        except:
            pass
        return {'country': 'Unknown', 'isp': 'Unknown'}
