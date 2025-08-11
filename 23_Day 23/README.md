#  Day 23 – Pandas Missing Data & Aggregation

## 📌 Assignments
1. **01_pandas_missing_data.py**  
   - Learn to detect, handle, and fill missing data in Pandas DataFrames using:
     - `isnull()` & `notnull()`
     - `dropna()` for removing missing values
     - `fillna()` for replacing missing values with constants or computed values.
   - Practice with a CSV dataset containing intentional missing values.

2. **02_store_product_sales.py**  
   - Load a CSV dataset (`02_store_product_sales.csv`)  
   - Perform grouping using `groupby()` to find total sales per store and per product.
   - Save the results to `02_product_avg_sales.csv` and `02_store_sales.csv`.

3. **03_pandas_aggregation.py**  
   - Learn Pandas aggregation functions like:
     - `sum()`, `mean()`, `min()`, `max()`
     - Using `.agg()` for multiple aggregations at once.
   - Apply them to analyze store sales data.

---

---

## 🚀 How to Run
```bash
# Run Assignment 1
python 01_pandas_missing_data.py

# Run Assignment 2
python 02_store_product_sales.py

# Run Assignment 3
python 03_pandas_aggregation.py