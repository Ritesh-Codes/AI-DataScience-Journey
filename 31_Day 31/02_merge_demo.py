import pandas as pd

# Employees DataFrame
employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "dept_id": [1, 2, 1, 3, 2]
})

# Departments DataFrame
departments = pd.DataFrame({
    "dept_id": [1, 2, 3],
    "dept_name": ["HR", "Finance", "IT"]
})

# Merge on dept_id
merged = pd.merge(employees, departments, on="dept_id", how="inner")
print(merged)