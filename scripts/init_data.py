#!/usr/bin/env python3
"""
Initialize directories and create/fetch raw data
"""
from pathlib import Path
import config
import fetch_data

def ensure_dirs():
    for folder in [config.DATA_RAW, config.DATA_CLEAN, config.DATA_PROCESSED, config.REPORTS]:
        folder.mkdir(parents=True, exist_ok=True)
    print("✅ Directories created/checked.")

def run():
    ensure_dirs()
    raw_file = config.DATA_RAW / config.RAW_FILENAME
    if raw_file.exists():
        print(f"✅ Raw CSV already exists: {raw_file}")
    else:
        print("ℹ️ Fetching data from CoinGecko API...")
        fetch_data.run(raw_file)

if __name__ == "__main__":
    run()
