import streamlit as st

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# Sidebar
# ==========================================

st.sidebar.success(
    "Select a page from the navigation panel."
)

st.sidebar.markdown("---")

st.sidebar.subheader("Dashboard Modules")

st.sidebar.markdown("""
- Sales Overview
- Forecast Explorer
- Anomaly Report
- Product Demand Segments
""")

# ==========================================
# Dashboard Title
# ==========================================

st.title("End-to-End Sales Forecasting & Demand Intelligence Dashboard")

st.markdown("""
Welcome to **Naman Arora's Sales Forecasting Dashboard**.

This project presents an end-to-end Machine Learning pipeline for analyzing
historical sales data and generating business insights through forecasting,
anomaly detection, and product segmentation.

### Project Objectives

- Forecast future sales demand
- Detect unusual sales anomalies
- Segment products based on demand patterns
- Support inventory planning and business decision making

Use the navigation panel on the left to explore each module.
""")

st.divider()

# ==========================================
# Project Architecture
# ==========================================

st.subheader("Project Architecture")

st.write("""
The architecture below illustrates the complete workflow implemented in this project,
starting from raw sales data collection to forecasting, anomaly detection,
product segmentation, and interactive dashboard visualization.
""")

st.image(
    "assets/architecture.png",
    use_container_width=True
)

st.divider()

# ==========================================
# Dashboard Summary
# ==========================================

st.subheader("Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Forecast Models",
        value="3"
    )

with col2:
    st.metric(
        label="Regions",
        value="4"
    )

with col3:
    st.metric(
        label="Categories",
        value="3"
    )

with col4:
    st.metric(
        label="Anomaly Methods",
        value="2"
    )

st.divider()

# ==========================================
# Technology Stack
# ==========================================

st.subheader("Technology Stack")

left, right = st.columns(2)

with left:
    st.markdown("""
- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
""")

with right:
    st.markdown("""
- Scikit-Learn
- Statsmodels
- Prophet
- XGBoost
- Streamlit
""")

st.divider()

# ==========================================
# Dashboard Modules
# ==========================================

st.subheader("Dashboard Modules")

col1, col2 = st.columns(2)

with col1:

    st.success("Sales Overview")

    st.success("Forecast Explorer")

with col2:

    st.warning("Anomaly Report")
    st.info("Product Demand Segments")

st.divider()

# ==========================================
# Footer
# ==========================================

st.caption(
    "Developed by Naman Arora | Final Internship Project – XYLOFY AI"
)