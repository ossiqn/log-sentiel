#!/bin/bash
# Log Sentinel — Installation Script
# Author  : OSSiqn Team
# GitHub  : https://github.com/ossiqn
# License : MIT © 2024 OSSiqn
# This file was produced by OSSiqn — github.com/ossiqn

echo "Log Sentinel Kuruluyor..."
python3 -m venv venv
source venv/bin/activate
pip install -r ../requirements.txt
mkdir -p ../logs
echo "Kurulum tamamlandi."
