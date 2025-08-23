# 📌 Day 37 – Handling Missing Data (Imputation)

Today’s focus: **detecting and handling missing values in datasets** using different imputation strategies.

---

## 📂 Assignments

### **1. Detect Missing Values**

**Filename:** `01_detect_missing.py`

* Load a dataset with missing values.
* Use `isnull()` and `sum()` to detect missing values.
* Generate a missing values summary.

---

### **2. Fill Missing Values**

**Filename:** `02_fill_missing.py`

* Practice filling missing values with:

  * Mean
  * Median
  * Mode
  * Forward fill
  * Backward fill

---

### **3. Case Study: Imputation Strategies**

**Filename:** `03_imputation_case.py`

* Use a realistic dataset with missing **Age, Salary, and Performance Scores**.
* Apply:

  * Department-wise mean imputation for Age
  * Median imputation for Salary
  * Forward fill for Performance Score
* Create a clean final dataset after imputation.