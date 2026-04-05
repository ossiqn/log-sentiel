"""
Log Sentinel — Akıllı Log Avcısı
Module  : Threat Detection Engine
Author  : OSSiqn Team
GitHub  : https://github.com/ossiqn
License : MIT © 2024 OSSiqn

Açıklama (TR):
Log verileri uzerinde SQLi, XSS ve Brute Force analizi yapar.

Description (EN):
Performs SQLi, XSS and Brute Force analysis on log data.

This file was produced by OSSiqn — github.com/ossiqn
"""

import re

class ThreatDetector:
    def __init__(self, config):
        self.sql_patterns = [r"UNION", r"SELECT", r"INSERT", r"UPDATE", r"DELETE", r"DROP", r"1=1", r"exec", r"xp_", r"sp_"]
        self.xss_patterns = [r"<script[^>]*>", r"javascript:", r"on(click|load|error|focus|blur)", r"<iframe[^>]*>", r"eval\s*\("]

    def analyze(self, log):
        threats = []
        target = str(log).lower()
        for p in self.sql_patterns:
            if re.search(p.lower(), target):
                threats.append({'type': 'SQL_INJECTION', 'severity': 'CRITICAL'})
                break
        for p in self.xss_patterns:
            if re.search(p.lower(), target):
                threats.append({'type': 'XSS', 'severity': 'HIGH'})
                break
        if log.get('status') in ['401', '403']:
            threats.append({'type': 'BRUTE_FORCE_ATTEMPT', 'severity': 'MEDIUM'})
        return threats
