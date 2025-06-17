 🚀 Day 26 – FAANG Preparation Roadmap

## 🧠 Machine Learning Engineering: From Jupyter to Python Scripts

### 🔄 Goal:
Transform experimental Jupyter notebooks into production-ready, modular `.py` scripts with GitHub best practices.

### ✅ Topics Covered:
- Converting notebooks using `jupyter nbconvert` and manual refactoring
- Modularizing into `data_loader.py`, `train.py`, `evaluate.py`, etc.
- Structuring ML repositories for collaboration
- Using `.gitignore`, `README.md`, and `requirements.txt`
- GitHub-friendly structure for production deployment

---

## ⚙️ Data Structures & Algorithms: Sliding Window Technique

### 📌 Focus:
Efficiently solve array and subarray problems using the **Sliding Window** pattern.

### 📚 Key Problems:
1. **Maximum Subarray** (Kadane’s Algorithm)
   - 🔢 Find the contiguous subarray with the maximum sum
   - ✅ Time: `O(n)`, Space: `O(1)`
2. **Minimum Subarray Length**
   - 🧮 Smallest subarray whose sum ≥ target value
   - ✅ Technique: Shrinking window

### 🛠️ Skills Learned:
- Real-time window sum tracking
- Dynamic resizing of window boundaries
- Optimizing brute-force solutions to linear complexity

---

## 🧪 SQL Mastery: Advanced Joins with Conditions

### 🔍 Today’s Focus:
Move beyond standard joins to explore **conditional joins**, **non-equality joins**, and **self-joins**.

### 💼 Real-World Use Cases:
- Matching customers with promotions active on signup dates
- Performing joins with range conditions (`BETWEEN`)
- Linking employee hierarchies with self-joins
- Applying business logic with multi-condition joins

### 🧠 Example:
```sql
SELECT a.name, b.discount
FROM customers a
JOIN promotions b
  ON a.signup_date BETWEEN b.start_date AND b.end_date;
📁 Repository Structure
pgsql
Copy
Edit
/day26/
│
├── notebooks/
│   └── day26_experiments.ipynb
│
├── scripts/
│   ├── data_loader.py
│   ├── model.py
│   ├── train.py
│   └── main.py
│
├── sql/
│   └── advanced_joins.sql
│
├── leetcode/
│   └── sliding_window_problems.py
│
├── requirements.txt
└── README.md
🧠 Reflection
Learned how to transform ML research into reusable engineering pipelines.

Optimized DSA problems using smarter patterns like sliding window.

Strengthened SQL fluency for real-world data logic.

🔗 Resources
Jupyter nbconvert Docs

Kadane’s Algorithm Visual

SQL Advanced Joins


