# plp-da-a3-duka-sales-and-agent-cleanup

# Data Analytics Portfolio: Duka Sales & Mobile Money Agent Network

## Project Overview

This project contains two data analytics engagements demonstrating data generation, data exploration, data cleaning, analysis, reporting and data quality management.

### Engagement 1: Duka Sales Analysis

The first engagement analyses sales transactions from a fictional Duka business. The goal is to understand sales performance across branches, product categories and sales channels.

**Key activities:**
- Generated and explored the sales dataset.
- Examined data structure, completeness and distributions.
- Calculated revenue using quantity and unit price.
- Analysed sales patterns across branches, products and channels.
- Created branch-level summaries and an Excel report.

#### Duka Executive Summary

1. The dataset contains **1,000 transactions** across **5 branches**.
2. Sales cover **5 product categories** and **3 sales channels**.
3. The transactions cover **6 months**, from January to June 2026.
4. The customer segments include **435 Premium transactions** and **565 Value transactions**.
5. The analysis compares revenue performance across **5 branches** and **3 sales channels**.

### Engagement 2: Mobile Money Agent Network

The second engagement focuses on assessing and improving the quality of mobile money agent transaction data across five counties.

The dataset contains transaction records and a separate agent register. Deliberate data quality issues were introduced to simulate real-world data problems.

**Key activities:**
- Audited transaction and agent datasets.
- Identified and removed exact duplicate records.
- Standardised transaction type labels.
- Converted transaction amounts and dates into appropriate formats.
- Identified missing values, invalid amounts and potential outliers.
- Matched transactions with the agent register.
- Flagged transactions belonging to unknown agents.
- Created a reusable cleaning function in `cleaning_pipeline.py`.
- Prepared data for county-level summaries and weekly pivot analysis.
- Documented data quality findings and privacy considerations.

#### Agent Data: Before and After Cleaning

| Description | Number of rows |
|---|---:|
| Original transaction records | 612 |
| Exact duplicate rows removed | 11 |
| Cleaned transaction records | 601 |
| Agent register records | 20 |

The cleaning process retained unmatched transactions and records requiring further investigation instead of automatically deleting them.

---

## Project Structure

```text
data-analytics-portfolio/
│
├── engagement-1-duka/
│   ├── generator.py
│   ├── duka_sales.csv
│   ├── duka_sales_analysis.ipynb
│   └── excel/
│       └── duka_branch_summary.xlsx
│
├── engagement-2-mobile-money/
│   ├── agent_transactions.csv
│   ├── agents.csv
│   ├── mobile_money_analysis.ipynb
│   └── cleaning_pipeline.py
│
└── README.md
```

*The notebook filenames above are suggested names; use the actual filenames saved in your project.*

---

## How to Regenerate the Data

### Engagement 1: Duka Sales

1. Open the `engagement-1-duka` folder.
2. Run the data generator:

```bash
python generator.py
```

3. The generator creates `duka_sales.csv`.
4. Keep the generated CSV in the same folder as the Duka notebook.

### Engagement 2: Mobile Money Agent Network

1. Open the Mobile Money notebook in Google Colab.
2. Locate the dataset generator code cell.
3. Run the generator cell to recreate:
   - `agent_transactions.csv`
   - `agents.csv`
4. Ensure both CSV files are available in the notebook's working directory.

**Note:** The generator uses a fixed random seed, allowing the dataset to be reproduced consistently when the generator code remains unchanged.

---

## How to Run the Notebooks

### Engagement 1: Duka Sales Analysis

1. Open `duka_sales_analysis.ipynb` in Google Colab or Jupyter Notebook.
2. Upload or make `duka_sales.csv` available in the working directory.
3. Run the notebook cells from top to bottom.
4. Review the
