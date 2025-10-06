# CryptoSuperProject

Pet-project: модульный пайплайн обработки и анализа крипто-данных (Pandas + Matplotlib + Seaborn).

## Структура

CryptoSuperProject/
├── data/
├── scripts/
├── config.py
├── requirements.txt
└── run_all.sh


## Установка

```bash
git clone <your-repo-url>
cd CryptoSuperProject
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Запустить весь пайплайн
python3 -m scripts.run_all

# Или запускать шаги по отдельности
python3 -m scripts.init_data
python3 -m scripts.clean_data
python3 -m scripts.filter_aggregate
python3 -m scripts.merge_tables
python3 -m scripts.analysis
Результаты и графики сохраняются в data/reports/.

Лицензия

MIT


---

### 4️⃣ Проверка структуры проекта

Убедись, что структура такая:



CryptoSuperProject/
├── .gitignore
├── README.md
├── requirements.txt
├── config.py
├── scripts/
│ ├── init_data.py
│ ├── clean_data.py
│ ├── filter_aggregate.py
│ ├── merge_tables.py
│ ├── analysis.py
│ └── run_all.py
└── data/
├── raw/
├── cleaned/
├── processed/
└── reports/


---

### 5️⃣ GitHub

Теперь можно пушить:

```bash
git init
git add .
git commit -m "Initial commit: CryptoSuperProject pipeline"
gh repo create CryptoSuperProject --public --source=. --remote=origin
git push origin main

# Запуск дашборда
```bash
streamlit run dashboard.py
yaml
Копировать код

---

💡 После этого проект будет:

- Модульным.
- Использовать реальные данные.
- Показывать интерактивные графики.
- Полностью готов к пушу на GitHub.

---

Если хочешь, я могу прямо сейчас написать **готовый рабочий `run_all.py` с интеграцией CoinGecko и Streamlit-ready пайплайном**, чтобы тебе не пришлось самому подправлять.  

Хочешь, чтобы я это сделал?