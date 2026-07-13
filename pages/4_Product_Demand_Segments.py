import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Product Demand Segments",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Product Demand Segments")

st.image(
    "charts/product_demand_clusters.png",
    use_container_width=True
)

cluster_table = pd.read_csv(
    "models/product_clusters.csv"
)

st.subheader("Cluster Assignments")

st.dataframe(
    cluster_table,
    use_container_width=True
)

st.info("""
Cluster 0 → High Volume, Stable Demand

Cluster 1 → Declining Demand

Cluster 2 → Growing Demand

Cluster 3 → Low Volume, High Volatility
""")
