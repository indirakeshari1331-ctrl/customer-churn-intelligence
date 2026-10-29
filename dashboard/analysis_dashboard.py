
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "processed" / "cleaned_customer_churn.csv"

st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Churn Analytics Dashboard")
st.write("Explore customer churn patterns and service trends.")

# Load cleaned data
@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE)

try:
    df = load_data()
except FileNotFoundError:
    st.error("Cleaned dataset not found. Please run src/clean_data.py first.")
    st.stop()

# Prepare churn values
df["Churn"] = df["Churn"].astype(str).str.strip()
churned = df[df["Churn"] == "Yes"]
retained = df[df["Churn"] == "No"]

total_customers = len(df)
churn_count = len(churned)
churn_rate = (
    churn_count / total_customers * 100
    if total_customers else 0
)
avg_monthly = df["MonthlyCharges"].mean()

# KPI cards
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Customers", f"{total_customers:,}")
c2.metric("Churned Customers", f"{churn_count:,}")
c3.metric("Churn Rate", f"{churn_rate:.2f}%")
c4.metric("Average Monthly Charges", f"${avg_monthly:.2f}")

st.divider()

# Chart 1: Churn distribution
st.subheader("1. Customer Churn Distribution")

churn_counts = df["Churn"].value_counts().reindex(
    ["No", "Yes"], fill_value=0
)

fig1, ax1 = plt.subplots()
ax1.bar(
    ["Retained", "Churned"],
    [churn_counts["No"], churn_counts["Yes"]]
)
ax1.set_ylabel("Number of Customers")
ax1.set_title("Retained vs Churned Customers")
st.pyplot(fig1)
plt.close(fig1)

# Chart 2: Churn by contract
st.subheader("2. Churn by Contract Type")

contract_table = pd.crosstab(
    df["Contract"], df["Churn"]
).reindex(columns=["No", "Yes"], fill_value=0)

fig2, ax2 = plt.subplots()
contract_table.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Contract Type")
ax2.set_ylabel("Number of Customers")
ax2.set_title("Churn Count by Contract")
ax2.legend(["Retained", "Churned"], title="Customer Status")
plt.xticks(rotation=0)
st.pyplot(fig2)
plt.close(fig2)

# Chart 3: Monthly charges comparison
st.subheader("3. Monthly Charges by Customer Status")

charge_data = [
    df.loc[df["Churn"] == "No", "MonthlyCharges"].dropna(),
    df.loc[df["Churn"] == "Yes", "MonthlyCharges"].dropna()
]

fig3, ax3 = plt.subplots()
ax3.boxplot(charge_data, tick_labels=["Retained", "Churned"])
ax3.set_ylabel("Monthly Charges")
ax3.set_title("Monthly Charges: Retained vs Churned")
st.pyplot(fig3)
plt.close(fig3)

# Contract churn rate table
st.subheader("4. Contract-wise Churn Rate")

contract_rates = (
    df.assign(ChurnFlag=(df["Churn"] == "Yes").astype(int))
    .groupby("Contract")
    .agg(
        Customers=("ChurnFlag", "size"),
        Churned=("ChurnFlag", "sum"),
        ChurnRate=("ChurnFlag", "mean")
    )
    .reset_index()
)

contract_rates["ChurnRate"] = (
    contract_rates["ChurnRate"] * 100
).round(2)

st.dataframe(contract_rates, use_container_width=True)

st.caption(
    "This dashboard describes patterns in the dataset. "
    "Association does not prove causation."
)
