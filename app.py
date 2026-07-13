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
    "👈 Select a page from the navigation panel."
)

# ==========================================
# Project Logo (Centered)
# ==========================================

left, center, right = st.columns([1,2,1])

with center:
    st.image(
        "assets/logo.png",
        width=220
    )

# ==========================================
# Dashboard Title
# ==========================================

st.title("📊 End-to-End Sales Forecasting & Demand Intelligence Dashboard")

st.markdown("""
Welcome to **Naman Arora's Sales Forecasting Dashboard**.

This dashboard demonstrates a complete Machine Learning pipeline that transforms
historical sales data into actionable business insights.

The system can:

- 📈 Forecast future sales demand
- 🚨 Detect unusual sales anomalies
- 📦 Segment products based on purchasing behavior
- 📊 Assist inventory planning and business decision making

Use the navigation panel on the left to explore each module.
""")

st.divider()

# ==========================================
# Project Architecture
# ==========================================

st.subheader("🏗 Project Architecture")

st.write("""
The architecture below illustrates the complete workflow followed in this project.

It starts from raw sales data, performs preprocessing and feature engineering,
builds forecasting and anomaly detection models, segments products using
Machine Learning, and finally visualizes everything through an interactive
Streamlit dashboard.
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