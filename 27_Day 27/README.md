# Day 27 – Pandas Data Cleaning & Preprocessing

## 📌 Overview
Today’s focus was on **data cleaning** using Pandas — a crucial step before analysis or machine learning.  
We learned how to:
- Handle missing values
- Remove duplicates
- Convert data types
- Clean string/text data

---

## 📂 Files
- **people_data.csv** → Raw dataset with missing values & duplicates
- **01_missing_and_duplicates.py** → Handles missing values and duplicates
- **02_data_type_and_string_cleaning.py** → Cleans data types and text formatting
- **people_data_cleaned.csv** → Cleaned dataset after Assignment 1
- **people_data_cleaned_v2.csv** → Cleaned dataset after Assignment 2

---

## 📝 Assignment 1 – Missing Data & Duplicates
**Steps performed:**
1. Checked for missing values with `.isnull().sum()`
2. Filled `Age` missing values with **mean**
3. Filled `City` missing values with **mode**
4. Dropped rows with missing values (demo purpose)
5. Removed duplicate rows
6. Saved cleaned data to `people_data_cleaned.csv`

---

## 📝 Assignment 2 – Data Type & String Cleaning
**Steps performed:**
1. Converted `Salary` column from string to numeric
2. Converted `Joining Date` to datetime format
3. Lowercased all values in `City`
4. Trimmed spaces from `Name`
5. Saved final cleaned dataset to `people_data_cleaned_v2.csv`

---

## 📊 Key Pandas Functions Used
- **Missing values:** `isnull()`, `notnull()`, `fillna()`, `dropna()`
- **Duplicates:** `duplicated()`, `drop_duplicates()`
- **Type conversion:** `astype()`, `pd.to_numeric()`, `pd.to_datetime()`
- **String cleaning:** `.str.lower()`, `.str.strip()`, `.str.replace()`
- **Renaming columns:** `rename()`
- **Resetting index:** `reset_index()`

---

## 🚀 How to Run
```bash
# Create dataset (run only once)
python create_dataset_day27.py

# Run Assignment 1
python 01_missing_and_duplicates.py

# Run Assignment 2
python 02_data_type_and_string_cleaning.py