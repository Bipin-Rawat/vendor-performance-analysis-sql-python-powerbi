
# 🛒 Vendor Performance Analysis Project

This project focuses on uncovering actionable insights from vendor, sales, and inventory data using Python and Power BI. The goal is to optimize purchasing decisions, improve profit margins, manage inventory efficiently, and reduce vendor dependency.

---

## 📚 Table of Contents

- [🧩 Business Problem](#-business-problem)
- [🧹 Data Cleaning and Preparation](#-data-cleaning-and-preparation)
- [📊 Exploratory Data Analysis](#-exploratory-data-analysis)
- [📈 Dashboard](#-dashboard)
- [📁 Project Structure](#-project-structure)
- [▶️ How to Run This Project](#️-how-to-run-this-project)
- [✅ Final Recommendations](#-final-recommendations)
- [👤 Author and Contact](#-author-and-contact)

---

## 🧩 Business Problem

Retail and wholesale companies often deal with complex vendor relationships, unpredictable sales trends, and inefficient inventory practices. Poor visibility into these areas can lead to:

- Losses from high-cost purchases or excessive discounts
- Inventory pileups due to unsold stock
- Over-reliance on a few vendors
- Missed opportunities to optimize bulk purchases

🔍 This project aims to:

- Identify **underperforming brands** needing promotional or pricing changes
- Find **top vendors** contributing most to revenue and profits
- Analyze **bulk purchasing benefits**
- Spot **slow-moving inventory** draining capital
- Compare **profitability models** across vendors

---

## 🧹 Data Cleaning and Preparation

- Removed records where:
  - Gross Profit ≤ 0
  - Profit Margin ≤ 0
  - Sales Quantity = 0
- Detected and analyzed outliers in freight cost and pricing
- Converted columns to appropriate datatypes
- Merged vendor, sales, and purchase datasets
- Created new metrics like profit margin, turnover, and bulk cost benefit

---

## 📊 Exploratory Data Analysis

- Identified vendors with low turnover but high cost inventory
- Assessed brand performance based on sales vs profit margin
- Correlation matrix revealed:
  - Weak link between purchase price and sales/profit
  - Strong link between purchase quantity and sales quantity
- Detected heavy reliance on a few vendors and freight inefficiencies

---

## 📈 Dashboard

Built using Power BI to visualize:

- Top 10 vendors by sales and purchases
- Vendor-wise profit margins
- Inventory turnover heatmaps
- Bulk pricing benefit
- Slow-moving inventory cost

---

## 📁 Project Structure

```text
📦 Vendor Performance Analysis/
├── 📜 Exploratory Data Analysis.ipynb        # Main analysis notebook
├── 📜 Exploratory Data Analysis.py          # Script version of the notebook
├── 📜 get_vendor_summary.py                 # Data aggregation logic
├── 📜 injection_db.py                       # DB setup with vendor invoice data
├── 📊 vendor_performance.pbix               # Power BI dashboard file
├── 📄 Vendors Performance Report.pdf        # Final PDF report with insights
├── 📄 README.md                             # Project documentation
├── 📄 .gitignore                            # Ignore .db, logs, temp files
```

---

## ▶️ How to Run This Project

1. Clone this repo.
2. (Optional) Run `injection_db.py` to recreate the SQLite database.
3. Launch `Exploratory Data Analysis.ipynb` in Jupyter Notebook.
4. Open `vendor_performance.pbix` in Power BI to view dashboard.

---

## ✅ Final Recommendations

- 🏷️ Re-price or promote high-margin, low-sales brands.
- 🧃 Diversify vendor base to reduce supply chain risk.
- 📦 Encourage bulk buying for cost savings.
- 📉 Clear slow-moving stock through offers or reduced orders.
- 🚀 Improve distribution and marketing for low-performing vendors.

---

## 👤 Author and Contact

**Bipin Rawat**  
Data Analytics Enthusiast  
📧 rawatbipin76@gmail.com  
