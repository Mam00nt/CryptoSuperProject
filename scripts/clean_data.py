#!/usr/bin/env python3
"""
Очистка raw данных и сохранение cleaned CSV
"""
import pandas as pd
from pathlib import Path
import config

import sys
from pathlib import Path

# добавляем корень проекта в путь поиска модулей
sys.path.append(str(Path(__file__).resolve().parent.parent))

import config


def run(input_path=None, output_path=None):
    input_path = Path(input_path) if input_path else config.DATA_RAW / config.RAW_FILENAME
    output_path = Path(output_path) if output_path else config.DATA_CLEAN / config.CLEAN_FILENAME

    df = pd.read_csv(input_path)

    # Чистим колонки
    df.columns = [c.strip() for c in df.columns]

    # Приводим к числовым типам
    df[config.PRICE_COLUMN] = pd.to_numeric(df[config.PRICE_COLUMN], errors="coerce")
    df[config.VOLUME_COLUMN] = pd.to_numeric(df[config.VOLUME_COLUMN], errors="coerce")

    # Заполняем NaN средним по колонке
    for col in [config.PRICE_COLUMN, config.VOLUME_COLUMN]:
        if df[col].isna().any():
            df[col].fillna(df[col].mean(), inplace=True)

    # Сохраняем
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned CSV сохранён: {output_path}")
    return output_path

if __name__ == "__main__":
    run()
