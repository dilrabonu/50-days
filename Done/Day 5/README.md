# 🚀 FAANG Preparation Roadmap – Day 5

Welcome to Day 5 of my 50-day FAANG Preparation Journey!  
Today’s focus was on **Hyperparameter Tuning in Machine Learning**, **Prefix Sums in DSA**, and **GROUP BY + HAVING in SQL** — all critical topics for technical interviews and real-world applications.

---

## 📘 Machine Learning – Hyperparameter Tuning

### Topics Covered:
- GridSearchCV (Exhaustive Search over hyperparameters)
- RandomizedSearchCV (Efficient random sampling from parameter grid)

### Key Concepts:
- Hyperparameters are settings like `max_depth`, `n_estimators`, `C`, and `gamma` that control how the model learns.
- GridSearchCV tries every combination of parameters.
- RandomizedSearchCV selects random combinations and is faster for large search spaces.

### 📊 Practical Work:
- Implemented both tuning methods using the [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)
- Trained Random Forest and SVM models with different parameter sets
- Evaluated performance using cross-validation

---

## 🧠 DSA – Prefix Sums & Difference Arrays

### Topics Covered:
- Prefix Sums for Range Sum Query
- Efficient subarray sum calculations using cumulative arrays

### Leetcode Practice:
- ✅ [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- ✅ [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

### Real-World Insight:
> Used in analytics dashboards, finance calculations, image processing, and anywhere performance matters with range-based queries.

---

## 📊 SQL – GROUP BY + HAVING

### Topics Covered:
- `GROUP BY` to aggregate rows
- `HAVING` to filter aggregated results
- Difference between `WHERE` (before grouping) and `HAVING` (after grouping)

### HackerRank Practice:
- ✅ [The PADS](https://www.hackerrank.com/challenges/the-pads/problem)
- ✅ [Weather Observation Station 20](https://www.hackerrank.com/challenges/weather-observation-station-20/problem)

### Real-World Example:
> Used in sales dashboards, customer segmentation, and performance reports for analyzing grouped data.

---

## 🧩 Tools & Libraries Used
- Python (Pandas, Scikit-learn)
- Jupyter Notebook / Google Colab
- Leetcode & HackerRank for practice
- SQL (MySQL / PostgreSQL syntax)

---

## ✅ Key Takeaways
- Hyperparameter tuning boosts model performance — learn to balance time vs accuracy.
- Prefix sums improve runtime from `O(n)` to `O(1)` for range queries — a must-know trick.
- GROUP BY + HAVING are SQL essentials for advanced data aggregation and filtering.

---

## 📈 Next Steps
- Continue tuning models and exploring pipelines on Kaggle
- Dive into Segment Trees (Advanced DSA for range queries)
- Practice advanced SQL joins + nested queries

---

