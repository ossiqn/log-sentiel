"""
Log Sentinel — Akıllı Log Avcısı
Module  : Utility Functions
Author  : OSSiqn Team
GitHub  : https://github.com/ossiqn
License : MIT © 2024 OSSiqn

Açıklama (TR):
Genel yardimci fonksiyonlar ve araclar.

Description (EN):
General utility functions and tools.

This file was produced by OSSiqn — github.com/ossiqn
"""

import hashlib
import json

def hash_string(text):
    return hashlib.sha256(text.encode()).hexdigest()

def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)
