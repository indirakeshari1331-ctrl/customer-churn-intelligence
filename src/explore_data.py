
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "raw" / "Telco-Customer-Churn.csv"

df = pd.read_csv(DATA_PATH)

print("\n===== DATASET INFORMATION =====")
print("Rows and columns:", df.shape)

print("\n===== FIRST 5 ROWS =====")
print(df.head().to_string())

print("\n===== COLUMN DATA TYPES =====")
print(df.dtypes.to_string())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum().to_string())

print("\n===== DUPLICATE ROWS =====")
print("Duplicate rows:", df.duplicated().sum())

print("\n===== CHURN DISTRIBUTION =====")
print(df["Churn"].value_counts().to_string())

print("\n===== DATA SUMMARY =====")
print(df.describe(include="all").to_string())

print("\nData exploration completed!")
print("TEST: Python code is running!")
input("Press Enter to exit...")

from pathlib import Path
import pandas as pd

# Project folder ka path
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Dataset ka path
DATA_PATH = PROJECT_DIR / "data" / "raw" / "Telco-Customer-Churn.csv"

# Dataset load karo
df = pd.read_csv(DATA_PATH)

print("\n===== 1. DATASET SIZE =====")
print("Rows and columns:", df.shape)

print("\n===== 2. FIRST 5 ROWS =====")
print(df.head().to_string())

print("\n===== 3. COLUMN DATA TYPES =====")
print(df.dtypes.to_string())

print("\n===== 4. MISSING VALUES =====")
print(df.isnull().sum().to_string())

print("\n===== 5. DUPLICATE ROWS =====")
print("Duplicate rows:", df.duplicated().sum())

print("\n===== 6. CHURN DISTRIBUTION =====")
print(df["Churn"].value_counts().to_string())

print("\n===== 7. DATA EXPLORATION COMPLETED =====")
