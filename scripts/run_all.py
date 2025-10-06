#!/usr/bin/env python3
"""
Полностью самодостаточный запуск пайплайна:
1) Создаёт директории
2) Создаёт demo CSV, если нет raw
3) Чистит данные
4) Фильтрует и агрегирует
5) Объединяет таблицы
6) Строит анализ и графики
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# ====== Настройки ======
ROOT = Path(__file__).resolve().parent.parent
DATA_RAW = ROOT / "data/raw"
DATA_CLEAN = ROOT / "data/cleaned"
DATA_PROCESSED = ROOT / "data/processed"
REPORTS = ROOT / "data/reports"

RAW_FILE = DATA_RAW / "crypto_raw.csv"
CLEAN_FILE = DATA_CLEAN / "crypto_clean.csv"
AGG_FILE = DATA_PROCESSED / "crypto_aggregated.csv"
MERGED_FILE = DATA_PROCESSED / "merged_data.csv"
CORR_PLOT = REPORTS / "correlation_plot.png"

PRICE_COLUMN = "Price"
VOLUME_COLUMN = "Volume"
NAME_COLUMN = "Name"

PRICE_THRESHOLD = 1.0
PLOT_SIZE = (8,5)
PLOT_DPI = 150

# ====== Функции ======
def ensure_dirs():
    for folder in [DATA_RAW, DATA_CLEAN, DATA_PROCESSED, REPORTS]:
        folder.mkdir(parents=True, exist_ok=True)
    print("✅ Директории созданы/проверены.")

def create_demo_csv():
    if RAW_FILE.exists():
        print(f"✅ Raw CSV уже есть: {RAW_FILE}")
        return
    data = {
        NAME_COLUMN: ["BTC","ETH","XRP","SOL","ADA","DOGE"],
        PRICE_COLUMN: [27000,1800,0.54,95,0.45,0.07],
        VOLUME_COLUMN: [35000000000,19000000000,5000000000,2400000000,1200000,800000000]
    }
    df = pd.DataFrame(data)
    df.to_csv(RAW_FILE, index=False)
    print(f"✅ Demo raw CSV создан: {RAW_FILE}")

def clean_data():
    df = pd.read_csv(RAW_FILE)
    df.columns = [c.strip() for c in df.columns]
    df[PRICE_COLUMN] = pd.to_numeric(df[PRICE_COLUMN], errors="coerce")
    df[VOLUME_COLUMN] = pd.to_numeric(df[VOLUME_COLUMN], errors="coerce")
    df.fillna(df.mean(numeric_only=True), inplace=True)
    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_FILE, index=False)
    print(f"✅ Cleaned CSV сохранён: {CLEAN_FILE}")

def filter_aggregate():
    df = pd.read_csv(CLEAN_FILE)
    df = df[df[PRICE_COLUMN] > PRICE_THRESHOLD]
    agg = df.groupby(NAME_COLUMN, as_index=False).agg(
        mean_price=(PRICE_COLUMN,"mean"),
        total_volume=(VOLUME_COLUMN,"sum"),
        count=(NAME_COLUMN,"count")
    )
    AGG_FILE.parent.mkdir(parents=True, exist_ok=True)
    agg.to_csv(AGG_FILE, index=False)
    print(f"✅ Aggregated CSV сохранён: {AGG_FILE}")

def merge_tables():
    df_clean = pd.read_csv(CLEAN_FILE)
    df_agg = pd.read_csv(AGG_FILE)
    merged = pd.merge(df_clean, df_agg, on=NAME_COLUMN, how="inner")
    merged = merged[[NAME_COLUMN, PRICE_COLUMN, "total_volume"]]
    merged.columns = ["name","price","volume"]
    MERGED_FILE.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(MERGED_FILE, index=False)
    print(f"✅ Merged CSV сохранён: {MERGED_FILE}")
    return merged

def analysis(df):
    REPORTS.mkdir(parents=True, exist_ok=True)
    corr = df["price"].corr(df["volume"])
    print(f"📊 Корреляция price/volume: {corr:.3f}")

    sns.set(style="whitegrid")
    plt.figure(figsize=PLOT_SIZE)
    sns.scatterplot(data=df, x="price", y="volume")
    plt.title(f"Price vs Volume (corr={corr:.2f})")
    plt.tight_layout()
    plt.savefig(CORR_PLOT, dpi=PLOT_DPI)
    plt.close()
    print(f"✅ Scatter plot сохранён: {CORR_PLOT}")

# ====== MAIN ======
if __name__ == "__main__":
    print("🚀 Запуск пайплайна...")
    ensure_dirs()
    create_demo_csv()
    clean_data()
    filter_aggregate()
    merged_df = merge_tables()
    analysis(merged_df)
    print("🎉 Пайплайн завершён успешно!")

from scripts.fetch_data import fetch_coingecko_top

def run_pipeline():
    print("🚀 Запуск пайплайна...")
    fetch_coingecko_top()
    # Далее clean_data, filter_aggregate, merge_tables, analysis
