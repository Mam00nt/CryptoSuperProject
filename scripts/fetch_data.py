#!/usr/bin/env python3
"""
Fetch crypto prices and volumes from CoinGecko API
and save to data/raw/crypto_raw.csv
"""
import requests
import pandas as pd
from pathlib import Path
import config

def fetch_coingecko_data(coin_ids=None, vs_currency="usd"):
    if coin_ids is None:
        coin_ids = ["bitcoin", "ethereum", "ripple", "solana", "cardano", "dogecoin"]

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "ids": ",".join(coin_ids),
        "order": "market_cap_desc",
        "per_page": len(coin_ids),
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    rows = []
    for d in data:
        rows.append({
            config.NAME_COLUMN: d["symbol"].upper(),
            config.PRICE_COLUMN: d["current_price"],
            config.VOLUME_COLUMN: d["total_volume"]
        })
    df = pd.DataFrame(rows)
    return df

def run(output_path=None):
    output_path = Path(output_path) if output_path else config.DATA_RAW / config.RAW_FILENAME
    df = fetch_coingecko_data()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Fetched CoinGecko data saved to {output_path}")

if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""
Fetch latest crypto data from CoinGecko API and save as CSV
"""
import requests
import pandas as pd
from pathlib import Path
import config

def fetch_coingecko_top(n=10):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": n,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    df = pd.DataFrame({
        config.NAME_COLUMN: [coin["symbol"].upper() for coin in data],
        config.PRICE_COLUMN: [coin["current_price"] for coin in data],
        config.VOLUME_COLUMN: [coin["total_volume"] for coin in data]
    })
    output_path = config.DATA_RAW / config.RAW_FILENAME
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Fetched {n} top coins from CoinGecko and saved to {output_path}")
    return df

if __name__ == "__main__":
    fetch_coingecko_top()
