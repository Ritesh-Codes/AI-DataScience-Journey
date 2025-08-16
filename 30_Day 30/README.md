# 📊 Day 30 - Handling Missing Data

On Day 30 of my Data Science journey, I worked on detecting and handling missing data in datasets using **Pandas** and **NumPy**. Missing data is very common in real-world scenarios, so learning how to manage it is a key skill in data preprocessing.

---

## 📂 Assignments

### ✅ Assignment 1: `01_detect_missing_values.py`
- Learned how to detect missing values in a dataset.  
- Used:
  - `isnull()` and `notnull()` to identify missing entries  
  - `sum()` to count total missing values per column  

---

### ✅ Assignment 2: `02_handle_missing_values.py`
- Practiced handling missing values with different strategies:  
  - Dropping missing data using `dropna()`  
  - Filling missing values with constants or statistical measures (`fillna()`, mean, median, mode)  
- Understood when to drop vs. when to impute values.  

---

### ✅ Assignment 3: `03_interpolation.py`
- Learned how to fill missing values using **interpolation techniques**.  
- Covered:
  - Linear interpolation (`method='linear'`)  
  - Time-based interpolation (`method='time'`)  
  - Polynomial & Quadratic interpolation (using **SciPy**)  

---

## 🛠️ Key Learnings
- Missing data is inevitable in datasets.  
- Choice of handling strategy depends on:
  - Amount of missing data  
  - Nature of the dataset (categorical vs numerical)  
  - Impact on analysis and models  
- Interpolation is powerful for time-series data.  

---