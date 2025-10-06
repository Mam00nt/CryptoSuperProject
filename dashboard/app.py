import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys

# добавляем корень проекта для импорта config
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("📊 CryptoSuperProject Dashboard")

# Загружаем данные
merged_path = config.DATA_PROCESSED / config.MERGED_FILENAME
if not merged_path.exists():
    st.warning(f"❌ Merged data not found: {merged_path}")
    st.stop()

df = pd.read_csv(merged_path)

st.subheader("Таблица данных")
st.dataframe(df)

# Фильтры
st.subheader("Фильтры")
coins = st.multiselect("Выбрать монеты:", options=df["name"].unique(), default=df["name"].unique())
df_filtered = df[df["name"].isin(coins)]

# График price vs volume
st.subheader("Price vs Volume")
fig, ax = plt.subplots(figsize=(8,5))
sns.scatterplot(data=df_filtered, x="price", y="volume", hue="name", ax=ax)
ax.set_title("Price vs Volume")
st.pyplot(fig)

# Корреляция
corr = df_filtered["price"].corr(df_filtered["volume"])
st.write(f"📈 Корреляция Price/Volume: **{corr:.3f}**")

# Дополнительно: гистограмма цен
st.subheader("Гистограмма цен")
fig2, ax2 = plt.subplots(figsize=(8,4))
sns.histplot(df_filtered, x="price", hue="name", multiple="stack", ax=ax2)
st.pyplot(fig2)
