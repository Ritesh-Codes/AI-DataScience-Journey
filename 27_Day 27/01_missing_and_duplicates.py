import pandas as pd

# 1. Load dataset
df = pd.read_csv("people_data.csv")
print("Original DataFrame:\n", df)

# 2. Find missing values count per column
print("\nMissing values per column:\n", df.isnull().sum())

# 3. Fill missing values in 'Age column with mean 
age_mean = df["Age"].mean()
df["Age"].fillna(age_mean, inplace=True)
print("\nAfter filling missing Age with mean:\n", df)

# 4. Fill missing values in 'City column with most frequent value (mode)
city_mode = df["City"].mode()[0]
df["City"].fillna(city_mode, inplace=True)
print("\nAfter filling missing city with mode:\n", df)

# 5. Drop all rows with any missing value (just for learning)
df_dropna = df.dropna()
print("\nAfter dropping rows with missing values:\n", df_dropna)

# 6. Remove duplicate rows
df_no_duplicates = df.drop_duplicates()
print("\nAfter removing duplicates:\n", df_no_duplicates)

# Optional: Save cleaned data
df_no_duplicates.to_csv("people_data_cleaned.csv", index=False)
print("\nCleaned data saved as people_data_cleaned.csv")