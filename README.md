# Car Sales Analysis Dashboard


[![Car Sales Analysis Dashboard](<img width="1272" height="826" alt="Screenshot 2026-05-29 at 16 29 15" src="https://github.com/user-attachments/assets/29b79641-7a49-4af8-a053-a200cee4582e" />)](https://public.tableau.com/app/profile/yusei.hosoya/viz/CarSalesAnalysis_17799323801300/MainDashboard?publish=yes)

<img width="2400" height="1600" alt="correlation_heatmap" src="https://github.com/user-attachments/assets/e711459f-4ca0-4c47-9f68-5f8be0f5644e" />


## Project Overview

This project analyzes car sales performance using Tableau and Python to identify the key drivers of profitability across car makes, years, monthly trends, discounts, costs, and sales volume.

The dashboard was designed to support business decision-making for a car dealership by answering questions such as:

- Which car makes generate the strongest profit margins?
- How do cost changes impact monthly profitability?
- Does discount rate directly reduce profit?
- Are higher sales volumes always linked to higher profit?
- Which brands may require pricing or cost-structure adjustments?
- How does year-over-year performance change across sales, cost, units sold, and profit?

The final Tableau dashboard allows users to interactively explore car sales performance from both detailed make-level analysis and broader year-over-year business performance perspectives.

## Live Dashboard

[View the Interactive Tableau Dashboard](https://public.tableau.com/app/profile/yusei.hosoya/viz/CarSalesAnalysis_17799323801300/MainDashboard?publish=yes)

---

## Dashboard Structure

The Tableau dashboard is divided into two main analytical views.

### 1. Make and Year Analysis Dashboard

This dashboard allows users to select a specific car make and year using interactive filters. It provides a detailed breakdown of KPIs by brand and time period.

Key features include:

- Car make selector
- Year selector
- KPI cards for sales, cost, profit, units sold, and margin
- Monthly profit and cost trends
- Revenue by make
- Profit margin by make
- Sales by day of week

This view is designed for detailed operational analysis. It helps identify which brands are performing well and which brands may be creating profitability risk.

### 2. Year-over-Year KPI Dashboard

This dashboard focuses on overall business performance across different years.

Key features include:

- Year-over-year KPI comparison
- Sales trend analysis
- Cost trend analysis
- Profit trend analysis
- Units sold trend analysis
- Monthly performance comparison

This view helps evaluate whether the dealership is improving or declining over time, and whether changes in cost or sales volume are affecting profit at the business level.

---

## Key Business Insights

### 1. Cost is the strongest driver of profit volatility

One of the most important findings is that profit is highly sensitive to cost changes.

In the make-level dashboard, some months show a sharp drop in profit when cost increases, even if the increase in cost is not extremely large. This suggests that certain months may involve higher inventory purchasing expenses or less favorable cost structures.

When cost rises even slightly, profit can fall significantly. In some cases, monthly profit moves close to or below zero.

Business interpretation:

The dealership should closely monitor vehicle acquisition cost, supplier pricing, and inventory purchasing timing. A small increase in cost can have a large impact on profitability if sale prices are not adjusted accordingly.

Recommended action:

- Track cost ratio by make and month
- Review high-cost inventory purchases
- Adjust pricing strategy when cost increases
- Set margin thresholds before approving sales
- Investigate brands or models that frequently produce low or negative profit

---

### 2. Overall YoY performance is more stable than individual make-level performance

Although make-level analysis shows that cost increases can strongly affect profit, the year-over-year dashboard shows that the business is more stable when viewed at the overall level.

This suggests that the dealership may be balancing risk across multiple car makes. Even when one make has higher costs or lower margins, other makes may offset the negative impact.

Business interpretation:

The dealership’s overall portfolio appears more stable than individual brand performance. A diversified make mix helps reduce the risk caused by cost increases in specific brands.

Recommended action:

- Continue monitoring make-level performance
- Avoid relying too heavily on low-margin brands
- Use high-margin brands to protect overall profitability
- Build a balanced portfolio across premium and volume brands

---

### 3. Profit changes more than unit sales

Year-over-year analysis shows that units sold do not fluctuate dramatically month by month. However, profit shows much larger movement.

This means that selling more cars is not necessarily the main driver of profit. Instead, profitability is more likely affected by:

- Car make
- Vehicle cost
- Sale price
- Profit margin
- Discount amount
- Mix of premium vs lower-margin vehicles

Business interpretation:

A volume-based strategy alone may not be enough. The dealership should focus more on margin quality than simply increasing the number of vehicles sold.

Recommended action:

- Prioritize high-margin vehicle categories
- Monitor average profit per unit
- Compare profit margin by make and model
- Avoid assuming that higher quantity automatically means better performance

---

### 4. Premium brands show stronger profit margins

The dashboard suggests that premium brands such as Mercedes-Benz and BMW generate stronger profit margins, often above 20%.

These brands also appear to contribute significantly to total revenue. Since profit margin and revenue by make move in a similar direction, the dealership is successfully generating strong revenue from brands that also have strong margins.

Business interpretation:

Premium brands are not only producing higher revenue but also protecting profitability. This makes them strategically important for the dealership.

Recommended action:

- Maintain strong inventory availability for high-margin premium brands
- Use premium brands as a core profit driver
- Compare sales volume and margin together, not separately
- Avoid over-investing in low-margin brands without pricing adjustments

---

### 5. Hyundai and Honda appear to have lower margins

The analysis suggests that Hyundai and Honda have profit margins closer to around 10%, which is relatively low compared with premium brands.

This does not necessarily mean they are bad brands to sell. They may still contribute to volume and customer acquisition. However, from a profitability perspective, these brands may require closer cost and pricing control.

Business interpretation:

Lower-margin brands may be useful for volume, but they create less profit protection when costs increase.

Recommended action:

- Review purchase costs for lower-margin brands
- Consider whether pricing can be adjusted
- Monitor discounting behavior on low-margin brands
- Avoid excessive discounting unless it supports a clear volume strategy

---

### 6. Discount rate alone does not explain profit loss

The Python correlation analysis shows that discount rate has almost no direct relationship with profit. However, estimated discount amount has a moderate negative relationship with profit.

This means the percentage discount may not be the main issue. Instead, the actual dollar value of the discount matters more.

For example, a small discount percentage on an expensive car can still represent a large dollar discount.

Business interpretation:

Managers should not only monitor discount percentage. They should also monitor the actual dollar amount of discounts.

Recommended action:

- Track estimated discount amount
- Set maximum discount dollar thresholds
- Review high-value discounts separately
- Compare discount amount against profit margin before approving deals

---

### 7. Quantity sold has almost no relationship with profit

The Python analysis shows that the correlation between quantity and profit is close to zero.

This suggests that selling more units does not automatically create more profit. Some high-volume vehicles may have lower margins, while some lower-volume premium vehicles may generate stronger profit.

Business interpretation:

A margin strategy is more important than a pure volume strategy.

Recommended action:

- Track profit per unit
- Compare high-volume brands with high-margin brands
- Focus on profitable sales, not just total sales count
- Build KPIs around margin and cost ratio, not only quantity

---
<img width="2400" height="1600" alt="correlation_heatmap" src="https://github.com/user-attachments/assets/f81f7ae7-d768-4a29-896c-51e17b36c40f" />

## Python Analysis Summary

Python was used to support the Tableau dashboard with deeper statistical analysis.

The Python analysis included:

- Data loading and cleaning
- Date conversion
- Profit margin calculation
- Cost ratio calculation
- Estimated discount amount calculation
- Negative profit flag creation
- Basic descriptive statistics
- Correlation analysis
- Negative profit analysis
- Profit margin by make
- Profit by gender
- Profit by age group
- Sale price vs profit scatter plot
- Cost ratio vs profit scatter plot
- Top negative profit records

---

## Key Metrics Created in Python

```python
df["Profit Check"] = df["Sale Price"] - df["Cost"]
df["Profit Margin"] = df["Profit"] / df["Sale Price"]
df["Cost Ratio"] = df["Cost"] / df["Sale Price"]
df["Estimated Discount Amount"] = df["Sale Price"] * df["Discount"]
df["Negative Profit Flag"] = df["Profit"] < 0
df["Age Group"] = (df["Customer Age"] // 10 * 10).astype(str) + "s"
