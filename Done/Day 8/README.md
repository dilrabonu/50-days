# 📅 Day 8 – FAANG Preparation Roadmap

## 🧠 Theme: Model Interpretability | Recursion | SQL INNER JOIN

Welcome to Day 8 of my 50-day FAANG preparation journey. Today focuses on three critical skills: explaining machine learning model predictions, solving recursive problems, and performing relational joins in SQL.

---

## 🔍 Machine Learning – Model Interpretability (SHAP + LIME)

### 🧾 Objective
Interpret black-box models to explain predictions and build trust in ML systems.

### 🔧 Tools Used
- Python
- SHAP (`shap` library)
- LIME (`lime` library)
- scikit-learn
- XGBoost / Random Forest

### ✅ Key Takeaways
- **LIME** explains individual predictions locally by learning an interpretable model.
- **SHAP** is based on game theory and provides both global and local feature attributions.
- SHAP is preferred for high-stakes domains (finance, healthcare) due to fairness and consistency.

### 🧠 Interview Insight
> “How would you explain why a fraud detection model predicted a certain transaction as fraud?”  
Using SHAP: you show how much each feature (like transaction amount, time, country) contributed to the prediction.

---

## 📘 Data Structures – Recursion (Factorial & Fibonacci)

### ✅ Concepts Practiced
- Base case and recursive step
- Time complexity of recursive vs iterative solutions
- Stack memory usage in recursive functions

### 💻 Problems Solved
- Recursive implementation of `factorial(n)`
- Recursive implementation of `fibonacci(n)`
- Compared with iterative solutions

### 🧠 Interview Insight
> “What’s the difference between recursion and iteration?”  
Recursion breaks the problem into smaller versions of itself; it uses stack memory and can be elegant for tree-like problems.

---

## 🗂️ SQL – INNER JOIN (Customers + Orders)

### ✅ Concepts Practiced
- INNER JOIN between two tables using a foreign key
- Matching rows from both tables based on common column
- Understanding the difference between INNER JOIN vs LEFT JOIN

### 💻 Sample Query
```sql
SELECT Customers.name, Orders.product
FROM Customers
INNER JOIN Orders ON Customers.customer_id = Orders.customer_id;

