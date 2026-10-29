
from pathlib import Path
import pandas as pd

# Project ke main folder ka path
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Dataset ka path
DATA_PATH = PROJECT_DIR / "data" / "raw" / "Telco-Customer-Churn.csv"

# Check karo ki file exist karti hai ya nahi
if not DATA_PATH.exists():
    print("ERROR: Dataset file nahi mili!")
    print("Expected location:", DATA_PATH)
else:
    # CSV file ko DataFrame mein load karo
    df = pd.read_csv(DATA_PATH)

    print("\nDataset successfully loaded!")
    print("-" * 40)

    print("Number of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nMissing values per column:")
    print(df.isnull().sum())
