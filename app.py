import streamlit as st

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

st.image(
    "assets/banner.png",
    use_container_width=True
)

st.title("Welcome to Naman Arora's Sales Forecasting Dashboard")

st.write("This is a simple dashboard to visualize sales forecasting results.\nSelect a page from the sidebar to explore different aspects of the sales data and forecasting results.")

