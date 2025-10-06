import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import config

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("📊 CryptoSuperProject Dashboard")

# Загружаем данные
csv_path = config.DATA_PROCESSED / config.MERGED_FILENAME
if not csv_path.exists():
    st.warning("Merged data not found! Запустите пайплайн сначала.")
else:
    df = pd.read_csv(csv_path)
    st.subheader("Merged Data")
    st.dataframe(df)

    # Scatter plot price vs volume
    st.subheader("Price vs Volume Scatter")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.scatterplot(data=df, x="price", y="volume", ax=ax)
    ax.set_xlabel("Price")
    ax.set_ylabel("Volume")
    st.pyplot(fig)

    # Корреляция
    corr = df["price"].corr(df["volume"])
    st.metric("Correlation (price vs volume)", f"{corr:.3f}")

    # Heatmap
    st.subheader("Correlation Heatmap")
    numeric = df.select_dtypes(include="number")
    fig2, ax2 = plt.subplots(figsize=(6,4))
    sns.heatmap(numeric.corr(), annot=True, fmt=".2f", ax=ax2)
    st.pyplot(fig2)
