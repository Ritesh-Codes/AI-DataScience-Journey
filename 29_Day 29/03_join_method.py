import pandas as pd

# -------------------------
# Example 1: Basic join on index
# -------------------------
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Salary': [70000, 80000, 90000]
}, index=[1, 2, 3])

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# --- join example 1: simple join on index ---
print("\n--- join: Combine DataFrames on index ---")
joined_df = df1.join(df2)
print(joined_df)

# --- join example 2: left join ---
print("\n--- join with how='left' ---")
joined_left = df1.join(df2, how='left')
print(joined_left)

# --- join example 3: right join ---
print("\n--- join with how='right' ---")
joined_right = df1.join(df2, how='right')
print(joined_right)

# --- join example 4: outer join ---
print("\n--- join with how='outer' ---")
joined_outer = df1.join(df2, how='outer')
print(joined_outer)

# --- join example 5: handling mismatched indexes ---
df3 = pd.DataFrame({
    'City': ['Houston', 'Miami'],
    'Salary': [60000, 75000]
}, index=[4, 5])

print("\nDataFrame 3 (with different indexes):")
print(df3)

print("\n--- join df1 with df3 (outer) ---")
joined_mismatch = df1.join(df3, how='outer')
print(joined_mismatch)


# -------------------------
# Example 2: Realistic CSV-based data join
# -------------------------
# Imagine we have two CSVs:
# employees.csv:
#   EmpID, Name, DepartmentID
#   101, Alice, D1
#   102, Bob, D2
#   103, Charlie, D1
#
# departments.csv:
#   DepartmentID, DepartmentName
#   D1, HR
#   D2, Finance
#   D3, IT

employees = pd.DataFrame({
    'EmpID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'DepartmentID': ['D1', 'D2', 'D1']
}).set_index('DepartmentID')

departments = pd.DataFrame({
    'DepartmentName': ['HR', 'Finance', 'IT']
}, index=['D1', 'D2', 'D3'])

print("\nEmployees DataFrame:")
print(employees)
print("\nDepartments DataFrame:")
print(departments)

print("\n--- join employees with departments (left join) ---")
emp_dept = employees.join(departments, how='left')
print(emp_dept)

print("\n--- join employees with departments (outer join) ---")
emp_dept_outer = employees.join(departments, how='outer')
print(emp_dept_outer)