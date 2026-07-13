import streamlit as st

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

# ==========================
# Sidebar
# ==========================

st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

st.sidebar.title("Navigation")

st.sidebar.info(
    "Use the pages below to explore the dashboard."
)

# ==========================
# Title
# ==========================

st.title("📊 End-to-End Sales Forecasting & Demand Intelligence")

st.markdown("""
Welcome to **Naman Arora's Sales Forecasting Dashboard**.

This dashboard demonstrates an end-to-end Machine Learning pipeline for:

- 📈 Sales Trend Analysis
- 🔮 Sales Forecasting
- 🚨 Anomaly Detection
- 📦 Product Demand Segmentation

Navigate through the pages from the sidebar to explore each module.
""")

st.divider()

# ==========================
# Dashboard Metrics
# ==========================

st.subheader("📌 Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Forecast Models",
    "3"
)

col2.metric(
    "Regions",
    "4"
)

col3.metric(
    "Categories",
    "3"
)

col4.metric(
    "Anomaly Methods",
    "2"
)

st.divider()

# ==========================
# Tech Stack
# ==========================

st.subheader("🛠 Tech Stack")

left, right = st.columns(2)

with left:

    st.markdown("""
- Python
- Pandas
- NumPy
- Matplotlib
""")

with right:

    st.markdown("""
- Scikit-Learn
- Prophet
- XGBoost
- Streamlit
""")

st.divider()

# ==========================
# Dashboard Modules
# ==========================

st.subheader("📂 Dashboard Modules")

c1, c2 = st.columns(2)

with c1:

    st.success("📈 Sales Overview")

    st.success("🔮 Forecast Explorer")

with c2:

    st.warning("🚨 Anomaly Report")

    st.info("📦 Product Demand Segments")

st.divider()

# ==========================
# Project Architecture
# ==========================

st.subheader("🏗 Project Architecture")

st.image(
    "assets/architecture.png",
    use_container_width=True
)

st.caption(
    "Complete workflow of the Sales Forecasting & Demand Intelligence pipeline."
)

st.divider()

# ==========================
# Footer
# ==========================

st.caption(
    "Developed by Naman Arora | End-to-End Sales Forecasting & Demand Intelligence Dashboard"
)