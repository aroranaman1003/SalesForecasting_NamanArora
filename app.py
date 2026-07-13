import streamlit as st

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

# ==========================================
# Title
# ==========================================

st.title("📊 End-to-End Sales Forecasting & Demand Intelligence Dashboard")

st.markdown("""
Welcome to **Naman Arora's Sales Forecasting Dashboard**.

This project presents an end-to-end Machine Learning pipeline that analyzes historical sales data to:

- 📈 Forecast future sales demand
- 🚨 Detect unusual sales anomalies
- 📦 Segment products based on demand behavior
- 📊 Support inventory planning and business decision-making

Use the sidebar to explore each module of the project.
""")

st.divider()

# ==========================================
# Dashboard Summary
# ==========================================

st.subheader("📌 Dashboard Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Forecast Models",
        "3"
    )

with col2:
    st.metric(
        "Regions",
        "4"
    )

with col3:
    st.metric(
        "Categories",
        "3"
    )

with col4:
    st.metric(
        "Anomaly Methods",
        "2"
    )

st.divider()

# ==========================================
# Tech Stack
# ==========================================

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

# ==========================================
# Dashboard Modules
# ==========================================

st.subheader("📂 Dashboard Modules")

left, right = st.columns(2)

with left:

    st.success("📈 Sales Overview")

    st.success("🔮 Forecast Explorer")

with right:

    st.warning("🚨 Anomaly Report")

    st.info("📦 Product Demand Segments")

st.divider()

# ==========================================
# Project Architecture
# ==========================================

st.subheader("🏗 Project Architecture")

st.write("""
The workflow below illustrates the complete pipeline followed in this project,
starting from raw sales data preprocessing to forecasting, anomaly detection,
product demand segmentation, and interactive business intelligence using
Streamlit.
""")

st.image(
    "assets/architecture.png",
    use_container_width=True
)

st.divider()

# ==========================================
# Footer
# ==========================================

st.caption(
    "Developed by Naman Arora | End-to-End Sales Forecasting & Demand Intelligence System"
)