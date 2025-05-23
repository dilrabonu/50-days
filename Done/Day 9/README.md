# 🚀 Day 9 – FAANG Preparation Roadmap

## 📅 Topics Covered:
- **Machine Learning:** Ensemble Learning – Stacking & Voting
- **Data Structures & Algorithms (DSA):** Recursion vs Iteration – Climbing Stairs
- **SQL:** LEFT JOIN & RIGHT JOIN – Orders with Missing Customers

---

## 🧠 Machine Learning – Ensemble Learning (Stacking & Voting)

### ✅ Concepts:
- **Voting Classifier:**
  - Combines predictions of multiple models.
  - Can be hard voting (majority class) or soft voting (average probabilities).
- **Stacking Classifier:**
  - Uses a meta-model to combine base model predictions for improved performance.
  - Powerful in real-world tabular datasets.

### 🔍 Real-World Use Case:
In wildfire detection tasks, stacking CNN models (on satellite imagery) with tabular models (e.g., XGBoost on weather and location data) can significantly improve fire prediction accuracy.




---

## 💻 DSA – Recursion vs Iteration

### 🧩 Problem: Climbing Stairs
Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?

### 📌 Concepts:
- **Recursive Approach:** Elegant but inefficient (O(2^n))
- **Iterative Dynamic Programming Approach:** Memory efficient and fast (O(n))

### ✅ Leetcode Problems:
- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

---

## 🗃️ SQL – LEFT JOIN & RIGHT JOIN

### 🔍 Concepts:
- **LEFT JOIN:** Returns all rows from the left table, even if there are no matches in the right.
- **RIGHT JOIN:** Returns all rows from the right table, even if there are no matches in the left.

### 📌 Real-World Example:
Querying **orders with or without associated customers** (e.g., missing customer info).

### ✅ HackerRank Practice:
- [LEFT JOIN Practice](https://www.hackerrank.com/challenges/earnings-of-employees/problem)
- [RIGHT JOIN Practice](https://www.hackerrank.com/challenges/weather-observation-station-5/problem)

---

## ✅ Summary
| Area | Topic | Practice Resources |
|------|-------|---------------------|
| ML | Stacking + Voting | Wildfire Detection (Kaggle) |
| DSA | Recursion vs Iteration | Leetcode (Climbing Stairs) |
| SQL | LEFT JOIN / RIGHT JOIN | HackerRank Challenges |


