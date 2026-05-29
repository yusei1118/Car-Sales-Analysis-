
import pandas as pd
import matplotlib.pyplot as plt
import os

# =========================
# 1. File paths
# =========================

csv_path = "/Users/yusei/Desktop/Car_Sales.csv"

output_folder = "/Users/yusei/Desktop/Car_Sales_Analysis_Output"
os.makedirs(output_folder, exist_ok=True)

print("Starting analysis...")

# =========================
# 2. Load data
# =========================

df = pd.read_csv(csv_path)

pd.set_option("display.float_format", "{:.2f}".format)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("CSV loaded successfully.")
print("Rows and columns:", df.shape)

# =========================
# 3. Create useful metrics
# =========================

df["Profit Check"] = df["Sale Price"] - df["Cost"]
df["Profit Margin"] = df["Profit"] / df["Sale Price"]
df["Cost Ratio"] = df["Cost"] / df["Sale Price"]
df["Estimated Discount Amount"] = df["Sale Price"] * df["Discount"]
df["Negative Profit Flag"] = df["Profit"] < 0
df["Age Group"] = (df["Customer Age"] // 10 * 10).astype(str) + "s"

# =========================
# 4. Basic statistics
# =========================

basic_stats = df[
    [
        "Customer Age",
        "Car Year",
        "Quantity",
        "Sale Price",
        "Cost",
        "Profit",
        "Discount",
        "Commission Rate",
        "Commission Earned",
        "Profit Margin",
        "Cost Ratio",
    ]
].describe().round(2)

print("\nBasic statistics:")
print(basic_stats)

basic_stats.to_csv(f"{output_folder}/basic_statistics.csv")

# =========================
# 5. Correlation table
# =========================

corr_columns = [
    "Customer Age",
    "Car Year",
    "Quantity",
    "Sale Price",
    "Cost",
    "Profit",
    "Discount",
    "Commission Rate",
    "Commission Earned",
    "Profit Margin",
    "Cost Ratio",
    "Estimated Discount Amount",
]

corr_table = df[corr_columns].apply(pd.to_numeric, errors="coerce").corr().round(2)

print("\nCorrelation table:")
print(corr_table)

corr_table.to_csv(f"{output_folder}/correlation_table.csv")

# =========================
# 6. Correlation heatmap
# =========================

plt.figure(figsize=(12, 8))
plt.imshow(corr_table, cmap="coolwarm", vmin=-1, vmax=1)

plt.xticks(range(len(corr_table.columns)), corr_table.columns, rotation=45, ha="right")
plt.yticks(range(len(corr_table.index)), corr_table.index)

plt.colorbar(label="Correlation")

for i in range(len(corr_table.index)):
    for j in range(len(corr_table.columns)):
        plt.text(j, i, corr_table.iloc[i, j], ha="center", va="center", fontsize=8)

plt.title("Correlation Heatmap - Car Sales Metrics")
plt.tight_layout()
plt.savefig(f"{output_folder}/correlation_heatmap.png", dpi=200)
plt.close()

# =========================
# 7. Negative profit analysis
# =========================

negative_df = df[df["Profit"] < 0]

print("\nNegative profit rows:")
print(len(negative_df))

print("\nNegative profit rate:")
print(f"{len(negative_df) / len(df) * 100:.2f}%")

negative_by_make = negative_df["Car Make"].value_counts()

print("\nNegative profit by Car Make:")
print(negative_by_make)

negative_by_make.to_csv(f"{output_folder}/negative_profit_by_make.csv")

comparison = pd.DataFrame(
    {
        "All Data Average": df[
            [
                "Sale Price",
                "Cost",
                "Profit",
                "Discount",
                "Commission Rate",
                "Commission Earned",
                "Profit Margin",
                "Cost Ratio",
            ]
        ].mean(),
        "Negative Profit Average": negative_df[
            [
                "Sale Price",
                "Cost",
                "Profit",
                "Discount",
                "Commission Rate",
                "Commission Earned",
                "Profit Margin",
                "Cost Ratio",
            ]
        ].mean(),
    }
).round(2)

print("\nAverage values: Negative Profit vs All Data")
print(comparison)

comparison.to_csv(f"{output_folder}/negative_profit_comparison.csv")

# =========================
# 8. Negative profit count by make graph
# =========================

negative_by_make_sorted = negative_by_make.sort_values(ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(negative_by_make_sorted.index, negative_by_make_sorted.values)
plt.title("Negative Profit Count by Car Make")
plt.xlabel("Number of Negative Profit Sales")
plt.ylabel("Car Make")
plt.tight_layout()
plt.savefig(f"{output_folder}/negative_profit_by_make.png", dpi=200)
plt.close()

# =========================
# 9. Average profit margin by car make
# =========================

margin_by_make = df.groupby("Car Make")["Profit Margin"].mean().sort_values()

plt.figure(figsize=(10, 6))
plt.barh(margin_by_make.index, margin_by_make.values * 100)
plt.title("Average Profit Margin by Car Make")
plt.xlabel("Average Profit Margin (%)")
plt.ylabel("Car Make")
plt.tight_layout()
plt.savefig(f"{output_folder}/profit_margin_by_make.png", dpi=200)
plt.close()

margin_by_make.to_csv(f"{output_folder}/profit_margin_by_make.csv")

# =========================
# 10. Profit by gender
# =========================

profit_by_gender = df.groupby("Customer Gender")[["Sale Price", "Cost", "Profit"]].mean().round(2)

print("\nAverage sale price, cost, and profit by gender:")
print(profit_by_gender)

profit_by_gender.to_csv(f"{output_folder}/profit_by_gender.csv")

profit_by_gender["Profit"].plot(kind="bar", figsize=(8, 5))
plt.title("Average Profit by Customer Gender")
plt.xlabel("Customer Gender")
plt.ylabel("Average Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{output_folder}/profit_by_gender.png", dpi=200)
plt.close()

# =========================
# 11. Profit by age group
# =========================

profit_by_age = df.groupby("Age Group")["Profit"].mean().sort_index()

plt.figure(figsize=(10, 5))
plt.plot(profit_by_age.index, profit_by_age.values, marker="o")
plt.title("Average Profit by Customer Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Profit")
plt.tight_layout()
plt.savefig(f"{output_folder}/profit_by_age_group.png", dpi=200)
plt.close()

profit_by_age.to_csv(f"{output_folder}/profit_by_age_group.csv")

# =========================
# 12. Sale Price vs Profit scatter
# =========================

sample_df = df.sample(n=min(5000, len(df)), random_state=1)

plt.figure(figsize=(10, 6))
plt.scatter(sample_df["Sale Price"], sample_df["Profit"], alpha=0.4)
plt.axhline(0, linestyle="--")
plt.title("Sale Price vs Profit")
plt.xlabel("Sale Price")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(f"{output_folder}/sale_price_vs_profit.png", dpi=200)
plt.close()

# =========================
# 13. Cost Ratio vs Profit scatter
# =========================

plt.figure(figsize=(10, 6))
plt.scatter(sample_df["Cost Ratio"], sample_df["Profit"], alpha=0.4)
plt.axhline(0, linestyle="--")
plt.axvline(1, linestyle="--")
plt.title("Cost Ratio vs Profit")
plt.xlabel("Cost Ratio")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(f"{output_folder}/cost_ratio_vs_profit.png", dpi=200)
plt.close()

# =========================
# 14. Top negative profit records
# =========================

top_negative = negative_df.sort_values("Profit").head(20)

print("\nTop 20 worst negative profit records:")
print(
    top_negative[
        [
            "Date",
            "Salesperson",
            "Customer Age",
            "Customer Gender",
            "Car Make",
            "Car Model",
            "Car Year",
            "Sale Price",
            "Cost",
            "Profit",
            "Discount",
            "Commission Rate",
            "Commission Earned",
            "Sales Region",
            "Profit Margin",
            "Cost Ratio",
        ]
    ].round(2)
)

top_negative.to_csv(f"{output_folder}/top_negative_profit_records.csv", index=False)

# =========================
# 15. Done
# =========================

print("\nDone. Files saved here:")
print(output_folder)