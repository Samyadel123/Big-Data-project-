import streamlit as st
import pandas as pd
from PIL import Image

# ===============================
# Load Data
# ===============================
@st.cache_data
def load_data():
    merged_df = pd.read_parquet("clean_data/merged_data.parquet")
    monte_df = pd.read_parquet("gold/monte_carlo_simulation_results.parquet")
    factor_loadings = pd.read_parquet("gold/factor_analysis_loadings.parquet")
    factor_scores = pd.read_parquet("gold/factor_analysis_scores.parquet")
    return merged_df, monte_df, factor_loadings, factor_scores

merged_df, monte_df, factor_loadings, factor_scores = load_data()

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="Weather Impact on Urban Traffic",
    layout="wide"
)

st.title("🚦 Weather Impact on Urban Traffic Dashboard")

# ===============================
# Tabs
# ===============================
tab1, tab2, tab3 = st.tabs([
    "📊 Cleaned Data",
    "🎲 Simulation (Monte Carlo)",
    "🧠 Factor Analysis"
])

# ===============================
# Tab 1: Cleaned Data
# ===============================
with tab1:
    st.header("📊 Cleaned & Merged Dataset")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(merged_df))

    if "avg_speed_kmh" in merged_df.columns:
        col2.metric(
            "Average Speed (km/h)",
            round(merged_df["avg_speed_kmh"].mean(), 2)
        )

    if "vehicle_count" in merged_df.columns:
        col3.metric(
            "Average Vehicle Count",
            round(merged_df["vehicle_count"].mean(), 2)
        )

    st.subheader("Sample of Cleaned Data")
    st.dataframe(merged_df.head(20))

# ===============================
# Tab 2: Monte Carlo Simulation
# ===============================
with tab2:
    st.header("🎲 Monte Carlo Simulation Results")

    st.subheader("Simulation Output Sample")
    st.dataframe(monte_df.head(20))

    st.subheader("Simulation Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            Image.open("gold/Distribution of Congestion Risk.png"),
            caption="Distribution of Congestion Risk",
            use_container_width=True
        )

    with col2:
        st.image(
            Image.open("gold/Traffic Jam Probability by Scenarios.png"),
            caption="Traffic Jam Probability by Scenarios",
            use_container_width=True
        )

    st.image(
        Image.open("gold/Continuous Distribution of Traffic Severity.png"),
        caption="Continuous Distribution of Traffic Severity",
        use_container_width=True
    )

# ===============================
# Tab 3: Factor Analysis
# ===============================
with tab3:
    st.header("🧠 Factor Analysis Results")

    st.subheader("Factor Loadings")
    st.dataframe(factor_loadings)

    st.subheader("Factor Scores (Sample)")
    st.dataframe(factor_scores.head(20))

    st.image(
        Image.open("gold/Congestion Level by Scenarios.png"),
        caption="Congestion Level by Scenarios",
        use_container_width=True
    )

# ===============================
# Footer
# ===============================
st.markdown("---")
st.success("✅ Interactive dashboard with Cleaned Data, Monte Carlo Simulation, and Factor Analysis")