## Day 32: GroupBy with Multiple & Custom Aggregations

Today, I practiced advanced `groupby()` operations in Pandas.

### 🔹 Assignment 1: Multiple Aggregations (`01_groupby_multiple_aggs.py`)
- Used `.agg()` with multiple built-in functions (`sum`, `mean`, `max`, `min`) on grouped data.
- Practiced renaming aggregations for clarity.

### 🔹 Assignment 2: Multiple Columns GroupBy (`02_multiple_groupby.py`)
- Grouped data by **multiple keys** (`Department`, `Gender`) and applied aggregations.
- Learned how hierarchical grouping works and how to interpret multi-index results.

### 🔹 Assignment 3: Custom Aggregations (`03_groupby_custom_agg.py`)
- Applied **custom functions** inside `.agg()` (e.g., salary range).
- Used **lambdas** to compute ratios like *Bonus % of Salary*.
- Extracted **top salaries per department** using `.apply()` with `nlargest`.

📌 **Key Learnings**:  
- `.agg()` can take both **built-in functions** and **custom lambdas**.  
- Named aggregation (`("Custom Name", function)`) makes results clearer.  
- `groupby()` is extremely powerful for financial, HR, and performance datasets.  