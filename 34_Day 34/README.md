# Day 34 – Pivot Tables & Crosstab Analysis

Today’s focus was on mastering **pivot tables** and **crosstab analysis** in Pandas.  
We learned how to reshape, summarize, and analyze data effectively using hierarchical indexing and multiple aggregation functions.

---

## 📂 Assignments

### 1. `01_pivot_basics.py`
- Created a simple pivot table with single-level rows and columns.
- Aggregated sales data by region and product.
- Learned how to use `aggfunc` for computing mean, sum, etc.

---

### 2. `02_pivot_multiple_agg.py`
- Introduced multiple aggregation functions in a pivot table.
- Calculated both **mean** and **sum** for sales grouped by product and region.
- Explored how Pandas structures results with **multi-level column headers**.

---

### 3. `03_pivot_hierarchical.py`
- Built pivot tables with **hierarchical row indexes** (`Region`, `Department`).
- Used **Employees as columns** for detailed salary & bonus analysis.
- Demonstrated **multiple value fields** (`Salary`, `Bonus`).
- Applied **multiple aggregation functions** (`mean`, `sum`) simultaneously.

---

## 📌 Key Learnings
- `pd.pivot_table()` is a powerful tool for **multi-dimensional analysis**.
- Supports:
  - Single & multiple aggregation functions.
  - Multi-level indexing (hierarchical rows and columns).
  - Summarizing multiple value fields at once.
- Crosstab (covered in Day 33) is a **specialized form of pivot**—great for frequency tables.

---

## ✅ Outcome
By the end of Day 34, we can:
- Build pivot tables with multiple dimensions.
- Combine different aggregation functions.
- Use pivot tables for **summarizing complex datasets** efficiently.