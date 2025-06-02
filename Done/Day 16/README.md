# 🧠 Day 16 – FAANG Preparation Roadmap

## 🚀 Topics Covered:
Welcome to Day 16 of my 50-day journey to master Machine Learning, Data Structures & Algorithms, and SQL for FAANG-level interviews. Today’s focus was on **Dimensionality Reduction**, **Queue Data Structures**, and **SQL Ranking Functions**.

---

## 🧪 1. Machine Learning: Dimensionality Reduction Techniques

### 📌 Concepts Learned:
- **PCA (Principal Component Analysis)**: Linear projection technique that retains maximum variance.
- **t-SNE (t-Distributed Stochastic Neighbor Embedding)**: Non-linear technique for visualizing high-dimensional data in 2D.
- **UMAP (Uniform Manifold Approximation and Projection)**: Faster alternative to t-SNE preserving local & global structure.

### 📊 Practical Dataset:
- **Fashion MNIST** and **Gene Expression RNA-Seq** (Kaggle)
  
### 🔬 Tools Used:
- Python, Scikit-learn, UMAP, Matplotlib, Seaborn

### ✅ Outcome:
Visualized high-dimensional data effectively and prepared the foundation for clustering or classification tasks.

---

## 📚 2. DSA: Queue, Circular Queue, and Sliding Window Maximum

### 🧠 Data Structures Practiced:
- **Queue (FIFO)**
- **Circular Queue**: Fixed-size memory-efficient structure
- **Sliding Window Maximum**: Efficient solution using Monotonic Queue (`deque` in Python)

### 🧩 LeetCode Problems Solved:
- [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)
- [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

### ✅ Outcome:
Built an intuition for queue-based problems and implemented optimized solutions suitable for real-time systems.

---

## 🧠 3. SQL: Ranking Functions for Top-N Analysis

### 🎯 Functions Learned:
- `RANK()`
- `DENSE_RANK()`
- `ROW_NUMBER()`

### 💼 Business Scenario:
**Find Top 3 Sales per Region** using:
```sql
SELECT * FROM (
  SELECT *,
    RANK() OVER (PARTITION BY region ORDER BY sales DESC) as rnk
  FROM sales_table
) sub
WHERE rnk <= 3

🧩 SQL Practice:
Top Competitors (HackerRank)

Department Top Three Salaries (LeetCode)

✅ Outcome:
Mastered SQL window functions for grouped ranking — essential for business intelligence, analytics, and reporting roles.

🛠 Tools & Tech Stack
Python (Pandas, NumPy, Scikit-learn, UMAP)

SQL (PostgreSQL / MySQL)

LeetCode, HackerRank, Kaggle Notebooks

Jupyter Notebook, Google Colab

📌 Key Takeaways
Dimensionality Reduction is crucial for visualizing high-dimensional ML datasets.

Sliding Window problems benefit greatly from deque-based optimizations.

SQL Window Functions (RANK, DENSE_RANK, ROW_NUMBER) are powerful tools for data segmentation and insights.
