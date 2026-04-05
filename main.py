"""
Log Sentinel — Akıllı Log Avcısı
Module  : Main Entry Point
Author  : OSSiqn Team
GitHub  : https://github.com/ossiqn
License : MIT © 2024 OSSiqn

Açıklama (TR):
Log Sentinel ana giris noktasi. Loglari dinler ve analiz motorlarini koordine eder.

Description (EN):
Main entry point for Log Sentinel. Listens to logs and coordinates analysis engines.

This file was produced by OSSiqn — github.com/ossiqn
"""

import os
import sys
import yaml
import asyncio
from src.log_parser import LogParser
from src.threat_detector import ThreatDetector
from src.discord_webhook import DiscordAlertSender
from src.database import Database
from src.ip_analyzer import IPAnalyzer

class LogSentinel:
    def __init__(self):
        with open('config.yaml', 'r') as f:
            self.config = yaml.safe_load(f)
        self.parser = LogParser(self.config)
        self.detector = ThreatDetector(self.config)
        self.alert = DiscordAlertSender(self.config)
        self.db = Database(self.config)
        self.ip_analyzer = IPAnalyzer(self.config)

    async def run(self):
        while True:
            for source in self.config.get('log_sources', []):
                if os.path.exists(source['path']):
                    await self.process_file(source)
            await asyncio.sleep(self.config.get('check_interval', 2))

    async def process_file(self, source):
        last_pos = self.db.get_pos(source['path'])
        with open(source['path'], 'r', encoding='utf-8', errors='ignore') as f:
            f.seek(last_pos)
            lines = f.readlines()
            new_pos = f.tell()
        for line in lines:
            parsed = self.parser.parse(line, source['type'])
            if parsed:
                threats = self.detector.analyze(parsed)
                for t in threats:
                    ip_data = self.ip_analyzer.analyze_ip(parsed.get('ip', 'Unknown'))
                    await self.db.save_alert(parsed, t)
                    await self.alert.send(parsed, t, ip_data)
        self.db.update_pos(source['path'], new_pos)

if __name__ == "__main__":
    sentinel = LogSentinel()
    asyncio.run(sentinel.run())
