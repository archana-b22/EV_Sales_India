import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="EV Sales Dashboard",
    page_icon="⚡",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/ev_sales_cleaned.csv")

# ---------------- TITLE ----------------
st.markdown(
    """
    <h1 style='text-align:center; color:#2E86C1;'>
    ⚡ Electric Vehicle Sales Analysis in India 🚗
    </h1>
    <h4 style='text-align:center; color:gray;'>
    Interactive Dashboard using Streamlit
    </h4>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

state = st.sidebar.selectbox(
    "Select State 🗺️",
    sorted(df["state"].unique())
)

vehicle_category = st.sidebar.selectbox(
    "Select Vehicle Category 🚘",
    sorted(df["vehicle_category"].unique())
)

filtered_df = df[
    (df["state"] == state) &
    (df["vehicle_category"] == vehicle_category)
]

# ---------------- KPI CARDS ----------------
col1, col2, col3 = st.columns(3)

col1.metric(
    label="🚗 Total EV Sales",
    value=f"{filtered_df['ev_sales_quantity'].sum():,}"
)

col2.metric(
    label="📅 Years Covered",
    value=filtered_df["year"].nunique()
)

col3.metric(
    label="🏷️ Vehicle Types",
    value=filtered_df["vehicle_type"].nunique()
)

st.markdown("---")

# ---------------- YEAR-WISE TREND ----------------
st.subheader(f"📈 Year-wise EV Sales Trend – {state}")

yearly_sales = (
    filtered_df.groupby("year")["ev_sales_quantity"]
    .sum()
    .reset_index()
)

fig, ax = plt.subplots()
ax.plot(
    yearly_sales["year"],
    yearly_sales["ev_sales_quantity"],
    marker="o",
    color="#1ABC9C"
)
ax.set_xlabel("Year")
ax.set_ylabel("EV Sales Quantity")
ax.grid(True)

st.pyplot(fig)

# ---------------- VEHICLE TYPE BAR CHART ----------------
st.subheader("🚙 EV Sales by Vehicle Type")

vehicle_sales = (
    filtered_df.groupby("vehicle_type")["ev_sales_quantity"]
    .sum()
    .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots()
vehicle_sales.plot(
    kind="bar",
    ax=ax2,
    color="#3498DB"
)
ax2.set_xlabel("Vehicle Type")
ax2.set_ylabel("Sales Quantity")

st.pyplot(fig2)

# ---------------- RAW DATA ----------------
with st.expander("📄 View Raw Data"):
    st.dataframe(filtered_df)