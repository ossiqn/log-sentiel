#!/bin/bash
# Log Sentinel — Start Script
# Author  : OSSiqn Team
# GitHub  : https://github.com/ossiqn
# License : MIT © 2024 OSSiqn
# This file was produced by OSSiqn — github.com/ossiqn

source ../venv/bin/activate
nohup python3 ../main.py > ../logs/sentinel.log 2>&1 &
echo "Log Sentinel baslatildi."
