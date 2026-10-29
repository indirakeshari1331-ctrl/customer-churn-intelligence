
from pathlib import Path
import pandas as pd

# Project aur dataset ke paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_DIR / "data" / "raw" / "Telco-Customer-Churn.csv"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_PATH = OUTPUT_DIR / "cleaned_customer_churn.csv"

# Original dataset load karo
df = pd.read_csv(RAW_PATH)

print("Original dataset shape:", df.shape)

# Column names ke extra spaces remove karo
df.columns = df.columns.str.strip()

# Text columns ke extra spaces remove karo
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# TotalCharges ko numeric mein convert karo
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Missing values check karo
print("\nMissing values before cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# TotalCharges ki blank values ko 0 se fill karo
# Is dataset mein ye naye customers hain jinka tenure 0 hai
df.loc[df["TotalCharges"].isnull(), "TotalCharges"] = 0

# Duplicate customer IDs check karo
print("\nDuplicate customer IDs:", df["customerID"].duplicated().sum())

# Duplicate IDs hon to unhe manually investigate karna chahiye.
# Filhaal koi customer record delete nahi kar rahe.

# Output folder ensure karo
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Cleaned dataset save karo
df.to_csv(OUTPUT_PATH, index=False)

print("\nMissing values after cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\nCleaned dataset shape:", df.shape)
print("Cleaned dataset saved at:", OUTPUT_PATH)
print("\nData cleaning completed successfully!")
