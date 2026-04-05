"""
Log Sentinel — Akıllı Log Avcısı
Module  : Database Management System
Author  : OSSiqn Team
GitHub  : https://github.com/ossiqn
License : MIT © 2024 OSSiqn

Açıklama (TR):
SQLite3 kullanarak uyarilari, engellenen IP'leri ve log pozisyonlarini saklar.

Description (EN):
Manages SQLite3 database for storing alerts, blocked IPs and log positions.

This file was produced by OSSiqn — github.com/ossiqn
"""

import sqlite3
import json

class Database:
    def __init__(self, config):
        self.path = config.get('database_path', 'logs/sentinel.db')
        self.setup()

    def setup(self):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY, ip TEXT, type TEXT, data TEXT)')
        c.execute('CREATE TABLE IF NOT EXISTS pos (path TEXT PRIMARY KEY, position INTEGER)')
        conn.commit()
        conn.close()

    def get_pos(self, path):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('SELECT position FROM pos WHERE path=?', (path,))
        res = c.fetchone()
        conn.close()
        return res[0] if res else 0

    def update_pos(self, path, pos):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('INSERT OR REPLACE INTO pos (path, position) VALUES (?, ?)', (path, pos))
        conn.commit()
        conn.close()

    async def save_alert(self, log, threat):
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('INSERT INTO alerts (ip, type, data) VALUES (?, ?, ?)', (log.get('ip', 'Unknown'), threat['type'], json.dumps(log)))
        conn.commit()
        conn.close()
