# 🚀 Day 2: Feature Selection, Regularization & Logical Thinking (FAANG 50-Day Prep)

Today’s focus was on sharpening both **Machine Learning model efficiency** and **fundamental coding logic**, combining advanced model techniques with practical DSA and SQL operations.

---

## 🔹 1. Feature Selection & Regularization (ML)

### 🧪 Lasso Path (L1 Regularization)
- Penalizes absolute coefficients to shrink irrelevant features to zero.
- Helps **automatically remove unimportant features** and reduce overfitting.
- Visualized using `lasso_path()` to understand how feature weights change as regularization increases.

### 🧪 SelectKBest
- Univariate feature selection using statistical tests.
- Kept only top **k most relevant features** based on variance or correlation with target.

### 🧪 SHAP (Explainability)
- SHAP values give deep insights into how each feature impacts model predictions.
- Used **SHAP beeswarm plot** to visualize positive/negative feature influence.

---

## 🔹 2. Data Structures & Algorithms (DSA) – Arrays

### 🔍 Problem 1: Two Sum
- Used a **hash map** for O(n) lookup to find pairs that sum to target.
- Classic FAANG question that tests use of dictionary and problem-solving.

### 🔍 Problem 2: Max Consecutive Ones
- Counted longest streak of 1s in a binary array.
- Reinforced loop logic and condition resets.

---

## 🔹 3. Logical Operators (Python & SQL)

### ✅ Python Operators
| Operator | Symbol | Usage Example       | Output  |
|----------|--------|---------------------|---------|
| AND      | `and`  | `True and False`    | False   |
| OR       | `or`   | `True or False`     | True    |
| NOT      | `not`  | `not True`          | False   |

### ✅ SQL Filtering Examples
- Customers with:
```sql
-- Total spent > $500 AND active
SELECT * FROM customers
WHERE total_spent > 500 AND status = 'active';

-- From Canada OR UK
SELECT * FROM customers
WHERE country = 'Canada' OR country = 'UK';

-- NOT from India
SELECT * FROM customers
WHERE NOT country = 'India';

