import pandas as pd

# Load datasets
employees = pd.read_csv("employees.csv")
departments = pd.read_csv("departments.csv")

print("Employees DataFrame:\n", employees)
print("\nDepartments DataFrame:\n", departments)

# ---------------------------------
# 1. Inner Join (only matching rows)
inner_join = pd.merge(employees, departments, on="DepartmentID", how="inner")
print("\nInner Join (only matches):\n", inner_join)

# ---------------------------------
# 2. Left Join (all employees, keep matching depts)
left_join = pd.merge(employees, departments, on="DepartmentID", how="left")
print("\nLeft Join (all employees):\n", left_join)

# ---------------------------------
# 3. Right Join (all departments, keep matching employees)
right_join = pd.merge(employees, departments, on="DepartmentID", how="right")
print("\nRight Join (all departments):\n", right_join)

# ---------------------------------
# 4. Outer Join (all rows from both)
outer_join = pd.merge(employees, departments, on="DepartmentID", how="outer")
print("\nOuter Join (all data):\n", outer_join)