
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = (
    PROJECT_DIR / "data" / "processed"
    / "cleaned_customer_churn.csv"
)
OUTPUT_DIR = PROJECT_DIR / "reports" / "figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(DATA_PATH)

# Graphs ka appearance
sns.set_theme(style="whitegrid")

# GRAPH 1: Churn distribution
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "churn_distribution.png", dpi=300)
plt.show()
plt.close()

# GRAPH 2: Churn rate by contract
contract_churn = (
    df.groupby("Contract", observed=True)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="ChurnRate")
)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=contract_churn,
    x="Contract",
    y="ChurnRate"
)
plt.title("Churn Rate by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "churn_by_contract.png", dpi=300)
plt.show()
plt.close()

# GRAPH 3: Monthly charges distribution by churn
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="MonthlyCharges",
    hue="Churn",
    bins=30,
    kde=True,
    element="step"
)
plt.title("Monthly Charges Distribution by Churn")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "monthly_charges_by_churn.png",
    dpi=300
)
plt.show()
plt.close()

print("\nEDA graphs created successfully!")
print("Graphs saved in:", OUTPUT_DIR)
