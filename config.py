from pathlib import Path

# Корень проекта
ROOT = Path(__file__).resolve().parent

# Папки
DATA_RAW = ROOT / "data" / "raw"
DATA_CLEAN = ROOT / "data" / "cleaned"
DATA_PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "data" / "reports"

# Файлы
RAW_FILENAME = "crypto_raw.csv"
CLEAN_FILENAME = "crypto_clean.csv"
PROCESSED_FILENAME = "crypto_aggregated.csv"
MERGED_FILENAME = "merged_data.csv"
CORR_PLOT = "correlation_plot.png"

# Столбцы
NAME_COLUMN = "Name"
PRICE_COLUMN = "Price"
VOLUME_COLUMN = "Volume"

# Фильтр
PRICE_THRESHOLD = 1.0

# Графики
PLOT_DPI = 150
PLOT_SIZE = (8, 5)
