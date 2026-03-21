import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/sales_data.csv")

# Basic cleaning
df.dropna(inplace=True)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create new column: total_price
df["total_price"] = df["price"] * df["quantity"]

# Standardize text
df["country"] = df["country"].str.upper()
df["category"] = df["category"].str.lower()

# Save processed data
df.to_csv("data/processed/clean_sales_data.csv", index=False)

print("ETL process completed successfully")
