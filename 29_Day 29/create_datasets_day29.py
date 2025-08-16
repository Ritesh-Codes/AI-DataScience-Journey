import pandas as pd

# Employees dataset
employees = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "DepartmentID": [1, 2, 3, 2, 4]
}
df_employees = pd.DataFrame(employees)
df_employees.to_csv("employees.csv", index=False)

# Departments dataset
departments = {
    "DepartmentID": [1, 2, 3, 5],
    "DepartmentName": ["HR", "Finance", "IT", "Marketing"]
}
df_departments = pd.DataFrame(departments)
df_departments.to_csv("departments.csv", index=False)

print("Datasets created: employees.csv, departments.csv")