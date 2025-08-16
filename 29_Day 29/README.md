# Day 29 - Combining DataFrames

In this day, we practiced different methods to combine multiple DataFrames in Pandas.  
This is crucial when working with real-world datasets that are often split across different sources.

## 📂 Assignments
1. **01_concat_dataframes.py**  
   - Demonstrates how to use `pd.concat()` to combine DataFrames vertically and horizontally.  

2. **02_merge_dataframes.py**  
   - Shows how to merge DataFrames using SQL-style joins (`inner`, `outer`, `left`, `right`).  

3. **03_join_method.py**  
   - Uses the `.join()` method to combine DataFrames on their index or on a key column.  

## 📊 Datasets Used
- **employees.csv** → Contains employee details (id, name, dept_id).  
- **departments.csv** → Contains department details (dept_id, dept_name).  
- **sales.csv** → Contains sales records (employee_id, sales_amount).  

## 📘 Concepts Learned
- Concatenation (`pd.concat`)  
- Merging (`pd.merge`) with different join types  
- Joining (`.join`) on indexes and keys  

---
✅ Completed as part of my **AI & Data Science Journey (Day 29)**