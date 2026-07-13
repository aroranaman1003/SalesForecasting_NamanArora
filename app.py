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

st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

st.sidebar.success(
    "👈 Select a page from the navigation panel."
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Dashboard Modules

- 📈 Sales Overview
- 🔮 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Product Demand Segments
""")

# ==========================================
# Dashboard Title
# ==========================================

st.title("📊 End-to-End Sales Forecasting & Demand Intelligence Dashboard")

st.markdown("""
Welcome to **Naman Arora's Sales Forecasting Dashboard**.

This project demonstrates a complete Machine Learning pipeline for sales forecasting,
anomaly detection, and product demand segmentation.

### Key Objectives

- 📈 Forecast future sales demand
- 🚨 Detect abnormal sales behaviour
- 📦 Segment products using Machine Learning
- 📊 Support business decision making
""")

st.divider()

# ==========================================
# Project Architecture
# ==========================================

st.subheader("🏗 Project Architecture")

st.write("""
The following architecture summarizes the complete workflow implemented in this project.
""")

st.image(
    "assets/architecture.png",
    use_container_width=True
)

st.divider()

# ==========================================
# Dashboard Summary
# ==========================================

st.subheader("📌 Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Forecast Models", "3")
col2.metric("Regions", "4")
col3.metric("Categories", "3")
col4.metric("Anomaly Methods", "2")

st.divider()

# ==========================================
# Technology Stack
# ==========================================

st.subheader("🛠 Technology Stack")

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

# ==========================================
# Dashboard Modules
# ==========================================

st.subheader("📂 Dashboard Modules")

col1, col2 = st.columns(2)

with col1:
    st.success("📈 Sales Overview")
    st.success("🔮 Forecast Explorer")

with col2:
    st.warning("🚨 Anomaly Report")
    st.info("📦 Product Demand Segments")

st.divider()

# ==========================================
# Footer
# ==========================================

st.caption(
    "Developed by Naman Arora | End-to-End Sales Forecasting & Demand Intelligence Dashboard"
)