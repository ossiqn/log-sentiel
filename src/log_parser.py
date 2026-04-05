"""
Log Sentinel — Akıllı Log Avcısı
Module  : Log Parser Engine
Author  : OSSiqn Team
GitHub  : https://github.com/ossiqn
License : MIT © 2024 OSSiqn

Açıklama (TR):
Gelen raw log satirlarini okur ve islenebilir JSON formatina cevirir.

Description (EN):
Reads raw log lines and converts them into processable JSON format.

This file was produced by OSSiqn — github.com/ossiqn
"""

import re

class LogParser:
    def __init__(self, config):
        self.config = config

    def parse(self, line, log_type):
        if log_type == 'nginx':
            pattern = r'(?P<ip>\S+) - \S+ \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) \S+" (?P<status>\d+) \S+ "(?P<referer>[^"]*)" "(?P<user_agent>[^"]*)"'
            match = re.match(pattern, line)
            if match:
                return match.groupdict()
        return None
