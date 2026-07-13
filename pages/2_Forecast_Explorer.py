import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Forecast Explorer",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Forecast Explorer")

df = pd.read_csv("data/train.csv")

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True
)

forecast_type = st.selectbox(
    "Select Forecast Type",
    [
        "Category",
        "Region"
    ]
)

if forecast_type == "Category":

    selected_item = st.selectbox(
        "Select Category",
        sorted(df["Category"].unique())
    )

else:

    selected_item = st.selectbox(
        "Select Region",
        sorted(df["Region"].unique())
    )

forecast_horizon = st.slider(
    "Forecast Horizon (Months)",
    min_value=1,
    max_value=3,
    value=3
)

file_name = (
    selected_item.lower().replace(" ", "_")+ "_forecast.csv"
)


forecast_df = pd.read_csv(
    f"models/{file_name}"
)

forecast_df = forecast_df.iloc[:forecast_horizon]

st.subheader("Forecast Output")

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(
    forecast_df["Month"],
    forecast_df["Forecast"],
    marker="o",
    linewidth=2
)

ax.set_title(f"{selected_item} Sales Forecast")

ax.set_xlabel("Forecast Month")

ax.set_ylabel("Forecast Sales")

ax.grid(alpha=0.3)

st.pyplot(fig)


col1, col2 = st.columns(2)

with col1:
    st.metric(
        "MAE",
        f"{forecast_df['MAE'].iloc[0]:,.2f}"
    )

with col2:
    st.metric(
        "RMSE",
        f"{forecast_df['RMSE'].iloc[0]:,.2f}"
    )

st.subheader("Forecast Table")

st.dataframe(forecast_df)