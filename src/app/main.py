# app/main.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from app.utils import load_combined_data, summary_table

st.set_page_config(page_title="Solar Compare", layout="wide")

st.title("Cross-country solar potential comparison")

# Load data (reads local CSVs)
combined = load_combined_data()

# Country selector
countries = st.multiselect("Select countries", options=combined['country'].unique(), default=list(combined['country'].unique()))

metrics = ['GHI','DNI','DHI']
metric = st.selectbox("Metric", metrics)

# Filter
df = combined[combined['country'].isin(countries)]

# Boxplot
st.subheader(f'Boxplot — {metric}')
fig, ax = plt.subplots(figsize=(8,4))
sns.boxplot(data=df, x='country', y=metric, ax=ax)
st.pyplot(fig)

# Summary table
st.subheader("Summary statistics")
st.dataframe(summary_table(df))

# Simple ranking
st.subheader("Average GHI ranking")
ghi_rank = df.groupby('country')['GHI'].mean().sort_values(ascending=False).reset_index()
st.bar_chart(ghi_rank.set_index('country'))
