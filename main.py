# main.py

import os
import pandas as pd
from eda import run_eda

def main():
    # Set up the path to the data file
    data_path = os.path.join("data", "data.csv")

    # Check if the file exists
    if not os.path.exists(data_path):
        print(f"❌ Error: File not found at {data_path}")
        return

    # Load the dataset
    print(f"📥 Loading dataset from {data_path}...")
    df = pd.read_csv(data_path)

    print("✅ Dataset loaded successfully!")
    print(f"🧮 Shape: {df.shape}")
    print(f"📋 Columns: {list(df.columns)}\n")

    # Run Exploratory Data Analysis
    print("🔍 Running EDA...\n")
    run_eda(df)

    # Placeholder for next steps
    print("\n✅ EDA completed.")
    print("🧪 Ready for preprocessing and modeling.")

if __name__ == "__main__":
    main()
