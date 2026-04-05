"""
Log Sentinel — Akıllı Log Avcısı
Module  : Discord Alert Notifier
Author  : OSSiqn Team
GitHub  : https://github.com/ossiqn
License : MIT © 2024 OSSiqn

Açıklama (TR):
Tespit edilen tehditleri anlik olarak Discord kanallarina iletir.

Description (EN):
Sends detected threats instantly to Discord channels.

This file was produced by OSSiqn — github.com/ossiqn
"""

import aiohttp
from datetime import datetime

class DiscordAlertSender:
    def __init__(self, config):
        self.url = config.get('discord_webhook_url')

    async def send(self, log, threat, ip_data):
        if not self.url or self.url == "YOUR_WEBHOOK_URL":
            return
        colors = {'SQL_INJECTION': 16711680, 'XSS': 16737792, 'BRUTE_FORCE_ATTEMPT': 16776960}
        embed = {
            'title': f"Threat Detected: {threat['type']}",
            'color': colors.get(threat['type'], 16711680),
            'fields': [
                {'name': 'IP Address', 'value': log.get('ip', 'Unknown'), 'inline': True},
                {'name': 'Country', 'value': ip_data.get('country', 'Unknown'), 'inline': True},
                {'name': 'Target Path', 'value': log.get('path', 'Unknown'), 'inline': False},
                {'name': 'Status Code', 'value': log.get('status', 'Unknown'), 'inline': True},
                {'name': 'Timestamp', 'value': datetime.now().isoformat(), 'inline': True}
            ]
        }
        async with aiohttp.ClientSession() as session:
            await session.post(self.url, json={'embeds': [embed]})
