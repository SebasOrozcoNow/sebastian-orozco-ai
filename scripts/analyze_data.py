import pandas as pd

# Load processed data
df = pd.read_csv("data/processed/clean_sales_data.csv")

# KPI 1: Total revenue
total_revenue = df["total_price"].sum()

# KPI 2: Revenue by country
revenue_by_country = df.groupby("country")["total_price"].sum()

# KPI 3: Top selling products
top_products = df.groupby("product")["quantity"].sum().sort_values(ascending=False)

# KPI 4: Sales by category
sales_by_category = df.groupby("category")["total_price"].sum()

print("\n=== BUSINESS KPIs ===")
print(f"Total Revenue: {total_revenue}\n")

print("Revenue by Country:")
print(revenue_by_country, "\n")

print("Top Products:")
print(top_products, "\n")

print("Sales by Category:")
print(sales_by_category, "\n")

with open ("data/processed/kpis.txt", "w") as f:
  f.write(f"Total Revenue: {total_revenue}\n\n")
  f.write("Revenue by Country:\n")
  f.write(str(revenue_by_country))
