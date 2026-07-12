import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sales Overview",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Overview Dashboard")

# Load Dataset
df = pd.read_csv("data/train.csv")

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d/%m/%Y"
)

yearly_sales = (
    df
    .groupby(
        df["Order Date"].dt.year
    )["Sales"]
    .sum()
    .reset_index()
)

yearly_sales

fig, ax = plt.subplots(figsize=(8,5))

ax.bar(
    yearly_sales["Order Date"],
    yearly_sales["Sales"]
)

ax.set_title("Total Sales by Year")

ax.set_xlabel("Year")

ax.set_ylabel("Sales")

st.pyplot(fig)



st.header("Monthly Sales Trend")

monthly_sales = (
    df
    .groupby(
        pd.Grouper(
            key="Order Date",
            freq="ME"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

fig, ax = plt.subplots(figsize=(12,5))

ax.plot(
    monthly_sales["Order Date"],
    monthly_sales["Sales"],
    linewidth=2
)

ax.set_title("Monthly Sales Trend")

ax.set_xlabel("Date")

ax.set_ylabel("Sales")

ax.grid(alpha=0.3)

st.pyplot(fig)



st.header("Sales by Region and Category")

selected_region = st.selectbox(
    "Select Region",
    sorted(df["Region"].unique())
)

selected_category = st.selectbox(
    "Select Category",
    sorted(df["Category"].unique())
)

filtered_data = df[
    (df["Region"] == selected_region) &
    (df["Category"] == selected_category)
]

st.write(filtered_data)