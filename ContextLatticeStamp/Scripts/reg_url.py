# -*- coding: utf-8 -*-
"""
reg_url.py — wrapper called by Register.ahk
Reads url/category/title from temp file, calls register_from_url()
HwWvWT260302
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from pathlib import Path
sys.path.insert(0, r'C:\Users\hwobb\RnHw')
from rnhw_json_manager import register_from_url

tmp   = Path(sys.argv[1])
lines = tmp.read_text(encoding='utf-8').splitlines()

url            = lines[0].strip().lstrip('\ufeff') if len(lines) > 0 else ''
category       = lines[1].strip() if len(lines) > 1 else ''
title_override = lines[2].strip() if len(lines) > 2 else ''

if not url:
    print("ERROR: no URL")
    sys.exit(1)

key = register_from_url(
    url      = url,
    category = category,
    title    = title_override,
)
print(f"OK: {key}")
