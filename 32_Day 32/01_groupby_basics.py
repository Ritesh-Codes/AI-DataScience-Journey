import pandas as pd

# Sample dataset: employees and their departments with salaries
data = {
    "Employee": ["Amit", "Riya", "Karan", "Meena", "Vikas", "Sita", "Raj"],
    "Department": ["HR", "IT", "IT", "Finance", "Finance", "HR", "IT"],
    "Salary": [50000, 60000, 65000, 70000, 55000, 52000, 72000],
    "Experience": [2, 3, 5, 7, 4, 2, 6]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 1. Group by Department and calculate mean salary
mean_salary = df.groupby("Department")["Salary"].mean()
print("\nMean Salary by Department:")
print(mean_salary)

# 2. Group by Department and calculate sum of salaries
sum_salary = df.groupby("Department")["Salary"].sum()
print("\nTotal Salary by Department:")
print(sum_salary)

# 3. Group by Department and count employees
count_employees = df.groupby("Department")["Employee"].count()
print("\nNumber of Employees by Department:")
print(count_employees)