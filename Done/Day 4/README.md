# 📅 Day 4 – FAANG Preparation Roadmap

## ✅ Themes Covered:
- 🧪 **Machine Learning**: Cross-Validation & Stratified Sampling  
- 📘 **DSA**: String Manipulation (Reverse String, Valid Palindrome)  
- 🎯 **SQL**: Aggregate Functions (COUNT, SUM, AVG)

---

## 🔬 Machine Learning: Stratified K-Fold Cross-Validation

### 📌 Objective:
Build a reliable classification model to **predict cervical cancer risk** using the Kaggle dataset:  
[Cervical Cancer Behavior Risk Dataset](https://www.kaggle.com/datasets/fedesoriano/cervical-cancer-behavior-risk)

### 📁 Dataset Overview:
- 858 rows, 36 features
- Binary target: `"Biopsy"` (cancer risk indicator)
- Features include habits, sexual behavior, and medical history
- **Imbalanced classes** → ideal for **Stratified K-Fold**

### ⚙️ What I Did:
- Performed **EDA** to understand feature distribution and class imbalance
- Applied **Standard K-Fold** vs **Stratified K-Fold** and compared performance
- Used **Logistic Regression**, **Random Forest**
- Visualized **SHAP values** for model interpretability

### 🧠 Key Takeaways:
- Stratified K-Fold ensures fair evaluation in imbalanced classification
- Logistic Regression performed surprisingly well with regularization
- SHAP helped uncover key behavioral risk features

---

## 📘 Data Structures & Algorithms (DSA)

### Problems Solved:
1. 🔄 **Reverse String** – Leetcode [#344](https://leetcode.com/problems/reverse-string/)
2. 🔍 **Valid Palindrome** – Leetcode [#125](https://leetcode.com/problems/valid-palindrome/)
3. 💡 **Valid Palindrome II** – Leetcode [#680](https://leetcode.com/problems/valid-palindrome-ii/)

### 💡 Concepts Practiced:
- Two-pointer technique
- String cleaning and manipulation
- Time/space complexity optimization

### 📌 Takeaways:
- Learned how to validate palindromes while ignoring punctuation and case
- Practiced memory-efficient in-place reversal of strings
- Used logic building blocks frequently asked in FAANG interviews

---

## 🎯 SQL Practice: Aggregate Functions

### Platform: HackerRank

### Problems Practiced:
1. `COUNT(*)` → Total records in a dataset
2. `SUM(column)` → Total sales or quantities
3. `AVG(column)` → Average order value or salaries

### 💼 Real-World Use Case:
> *"Given a sales database, calculate total revenue, total orders, and average revenue per order for Q1 2025."*

```sql
SELECT 
  COUNT(*) AS total_orders,
  SUM(order_amount) AS total_revenue,
  AVG(order_amount) AS average_order_value
FROM sales
WHERE order_date BETWEEN '2025-01-01' AND '2025-03-31';

🚀 What I Learned Today:
The power of Stratified K-Fold in handling imbalanced classification

Efficient string manipulation using Python

Writing aggregate SQL queries to summarize real-world datasets
