import streamlit as st

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

# Sidebar Logo
st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

# Banner
st.image(
    "assets/banner.png",
    use_container_width=True
)

# Title
st.title("📊 End-to-End Sales Forecasting & Demand Intelligence")

# Description
st.markdown("""
Welcome to **Naman Arora's Sales Forecasting Dashboard**.

This project analyzes historical sales data to forecast future demand, detect anomalies, and segment products based on demand patterns.

### Features
- 📈 Sales Trend Analysis
- 🔮 Sales Forecasting
- 🚨 Anomaly Detection
- 📦 Product Demand Segmentation
""")

# Dashboard Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Forecast Models", "3")
col2.metric("Regions", "4")
col3.metric("Categories", "3")
col4.metric("Anomaly Detection", "2 Methods")

st.divider()

st.subheader("🛠 Tech Stack")

st.write("""
- Python
- Pandas
- Matplotlib
- Scikit-Learn
- XGBoost
- Prophet
- Streamlit
""")

st.divider()

st.info(
    "👈 Use the sidebar to explore different modules of the dashboard."
)