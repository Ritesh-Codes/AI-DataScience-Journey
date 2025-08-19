# Day 33: Pivot Tables in Pandas (Advanced)

Today’s focus was on working with **pivot tables in pandas**, including multiple aggregation functions and adding totals using margins.

---

## Assignment 1: Single Aggregation Pivot
**File:** `01_pivot_single_agg.py`  
- Created a pivot table to summarize sales by region and product.  
- Used a single aggregation function (`sum`) to get total sales.  
- Practiced understanding the pivot table structure.

---

## Assignment 2: Multiple Aggregations in Pivot
**File:** `02_pivot_multiple_agg.py`  
- Applied **multiple aggregation functions** in a pivot table.  
- For example:
  - `Sales` → `sum` and `mean`  
  - `Quantity` → `sum`  
- Learned how to pass dictionaries to `aggfunc` for different columns.

---

## Assignment 3: Pivot with Margins (Totals)
**File:** `03_pivot_with_margins.py`  
- Created a pivot table with **department-wise performance scores and bonuses**.  
- Used `margins=True` to add a **Total row** (overall mean/total).  
- Customized total row label using `margins_name="Total"`.

---

## Key Learnings
- Pivot tables provide an Excel-like summary tool inside pandas.  
- Can apply **different aggregations per column**.  
- `margins=True` makes it easy to add totals for rows/columns.  
- Very useful for **data summarization and quick insights**.