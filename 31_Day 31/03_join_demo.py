import pandas as pd

employees = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "DeptID": [1, 2, 2, 3, 4]
}).set_index("EmpID")

departments = pd.DataFrame({
    "DeptID": [1, 2, 3],
    "Department": ["HR", "Finance", "IT"]
}).set_index("DeptID")

print("Employees Table:")
print(employees, "\n")

print("Departments Table:")
print(departments, "\n")

# Inner join
inner_join = employees.join(departments, on="DeptID", how="inner")
print("Inner Join Result:")
print(inner_join, "\n")

# Left join
left_join = employees.join(departments, on="DeptID", how="left")
print("Left Join Result:")
print(left_join, "\n")