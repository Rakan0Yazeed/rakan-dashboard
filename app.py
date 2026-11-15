import streamlit as st
import pandas as pd

df = pd.read_csv("cafe_sales.csv")

st.title("Qahwa Corner Sales Dashboard")

branch = st.selectbox("select branch", df["branch"].unique())
filtered = df[df["branch"] == branch]

st.metric("total revenue", int(filtered["total_sar"].sum()))

st.subheader("revenue by product")
st.bar_chart(filtered.groupby("product")["total_sar"].sum())
