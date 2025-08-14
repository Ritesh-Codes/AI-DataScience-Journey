import pandas as pd
import numpy as np

# Create sample data
data = {
  "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Alice", "Grace", np.nan, "Hank"],
  "Age": [25, 30, np.nan, 45, 28, 35, 25, 40, 29, np.nan],
  "City": ["Mumbai", "Delhi", "Banglore", "Mumbai", np.nan, "Delhi", "Mumbai", "Pune", "Delhi", "Pune"],
  "Salary": [50000, 60000, 55000, np.nan, 65000, 58000, 50000, 72000, 62000, 71000]
  }

df = pd.DataFrame(data)

# Save dataset for assignments
df.to_csv("people_data.csv", index=False)
print("Dataset created and saved as people_data.csv")