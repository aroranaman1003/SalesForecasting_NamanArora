import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Anomaly Report",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Sales Anomaly Report")

st.header("Isolation Forest Anomaly Detection")

st.image(
    "charts/isolation_forest_anomalies.png",
    use_container_width=True
)

isolation_table = pd.read_csv(
    "models/anomaly_table.csv"
)

st.subheader("Detected Anomalies")

st.dataframe(
    isolation_table,
    use_container_width=True
)

st.header("Z-Score Based Anomaly Detection")

st.image(
    "charts/zscore_anomalies.png",
    use_container_width=True
)

zscore_table = pd.read_csv(
    "models/zscore_anomalies.csv"
)

st.subheader("Detected Anomalies")

st.dataframe(
    zscore_table,
    use_container_width=True
)