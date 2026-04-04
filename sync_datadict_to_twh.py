# sync_datadict_to_twh.py
# Reads RnHw_DataDict.json and pushes each entry as a tiddler to TwNode
# Usage: python sync_datadict_to_twh.py
# ============================================================

import json
import requests
from pathlib import Path

# Config
DATADICT_FILE = Path("RnHw_DataDict.json")
TW_BASE = "http://localhost:8080"
TW_USER = "user"
TW_PASS = "password"
TAG = "DataDict"

def tw_headers():
    import base64
    token = base64.b64encode(f"{TW_USER}:{TW_PASS}".encode()).decode()
    return {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
        "X-Requested-With": "TiddlyWiki",
    }

def push_tiddler(title: str, fields: dict) -> int:
    url = f"{TW_BASE}/recipes/default/tiddlers/{requests.utils.quote(title, safe='')}"
    # Format value as readable text
    text = json.dumps(fields, ensure_ascii=False, indent=2)
    payload = {
        "title": title,
        "text": text,
        "tags": TAG,
        "type": "text/plain",
    }
    resp = requests.put(url, json=payload, headers=tw_headers(), timeout=10)
    return resp.status_code

def main():
    if not DATADICT_FILE.exists():
        print(f"ERROR: {DATADICT_FILE} not found. Run from RnHw directory.")
        return

    d = json.load(open(DATADICT_FILE, encoding="utf-8"))
    print(f"Found {len(d)} entries in DataDict.")

    ok = 0
    fail = 0
    for key, val in d.items():
        status = push_tiddler(key, val)
        if status in (200, 201, 204):
            print(f"  ✓ {key}")
            ok += 1
        else:
            print(f"  ✗ {key} — HTTP {status}")
            fail += 1

    print(f"\nDone: {ok} pushed, {fail} failed.")

if __name__ == "__main__":
    main()