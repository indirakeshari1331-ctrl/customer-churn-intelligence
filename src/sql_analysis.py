
from pathlib import Path
import sqlite3
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "processed" / "cleaned_customer_churn.csv"
DB_PATH = PROJECT_DIR / "data" / "processed" / "churn.db"

# Check dataset
if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Cleaned dataset nahi mili: {DATA_PATH}"
    )

# Load cleaned data
df = pd.read_csv(DATA_PATH)

# Create SQLite database
with sqlite3.connect(DB_PATH) as conn:
    df.to_sql("customers", conn, if_exists="replace", index=False)

    print("\n1. TOTAL CUSTOMERS")
    query = """
    SELECT COUNT(*) AS total_customers
    FROM customers;
    """
    print(pd.read_sql_query(query, conn).to_string(index=False))

    print("\n2. CHURN COUNTS")
    query = """
    SELECT Churn, COUNT(*) AS customer_count
    FROM customers
    GROUP BY Churn;
    """
    print(pd.read_sql_query(query, conn).to_string(index=False))

    print("\n3. OVERALL CHURN RATE")
    query = """
    SELECT
        ROUND(
            100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*), 2
        ) AS churn_rate_percent
    FROM customers;
    """
    print(pd.read_sql_query(query, conn).to_string(index=False))

    print("\n4. CHURN RATE BY CONTRACT")
    query = """
    SELECT
        Contract,
        COUNT(*) AS total_customers,
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
        ROUND(
            100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
            / COUNT(*), 2
        ) AS churn_rate_percent
    FROM customers
    GROUP BY Contract
    ORDER BY churn_rate_percent DESC;
    """
    print(pd.read_sql_query(query, conn).to_string(index=False))

    print("\n5. CHURN BY MONTHLY CHARGES")
    query = """
    SELECT
        Churn,
        ROUND(AVG(MonthlyCharges), 2) AS average_monthly_charges
    FROM customers
    GROUP BY Churn;
    """
    print(pd.read_sql_query(query, conn).to_string(index=False))

print("\nSQL analysis completed!")
print("Database saved at:", DB_PATH)
