# 🧠 Day 19 – TensorFlow vs PyTorch | Heapify + Custom Comparators | SQL Window Functions

Welcome to Day 19 of my **50-Day FAANG Preparation Challenge**, where I explored core ML, DSA, and SQL concepts in-depth with hands-on implementations and interview-level understanding.

---

## 📌 Topics Covered

### 1. 🧪 Machine Learning: TensorFlow vs PyTorch – Same Neural Network in Both

#### ✅ Concepts Explored
- Differences in framework design, debugging, and deployment.
- Dynamic vs static computation graphs.
- Building the **same MLP (Multilayer Perceptron)** for MNIST classification in **both TensorFlow and PyTorch**.

#### ✅ Key Learnings
- TensorFlow is production-ready and ideal for mobile/web deployment.
- PyTorch is intuitive and better for research and rapid prototyping.
- Both support GPU acceleration and industry-grade training pipelines.

#### 🛠️ Project
- Implemented MLPs using both frameworks on the MNIST dataset to compare usability, syntax, and performance.

---

### 2. 🧮 DSA: Heapify + Custom Comparators – Reorganize String

#### ✅ Concepts Explored
- Heap data structure: min-heap and max-heap using `heapq`.
- Priority-based operations for efficient top-k and scheduling tasks.
- Solved the **Reorganize String** problem using a **max-heap and custom comparator logic**.

#### ✅ Key Learnings
- Heap operations provide O(log n) insertion/removal.
- Custom comparators in Python can simulate max-heap with negative values.
- Reorganizing characters to avoid adjacent duplicates is a classic FAANG pattern.

#### 🔧 Problem Solved
- `Reorganize String` using Python `heapq` and character frequency tracking.

---

### 3. 🧾 SQL: Window Functions with OVER() – Moving Averages & Partitioning

#### ✅ Concepts Explored
- Introduction to SQL Window Functions.
- `OVER(PARTITION BY ...)` vs `GROUP BY`.
- Rolling computations with `ROWS BETWEEN ... PRECEDING AND CURRENT ROW`.

#### ✅ Key Learnings
- Window functions allow calculations **without collapsing rows**.
- Perfect for time series data (e.g., 3-day moving average).
- Partitioning helps compare groups within the same result set.

#### 🛠️ Query Example
```sql
SELECT 
  date,
  sales,
  AVG(sales) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg
FROM sales_data;
🧠 FAANG Interview Insights
Theme	Sample FAANG Question	Key Answer
ML	Why PyTorch vs TensorFlow?	PyTorch = flexibility, TF = production
DSA	How do you implement custom heaps?	Use heapq with negative values or __lt__
SQL	Difference between GROUP BY vs PARTITION BY?	GROUP BY aggregates, PARTITION BY retains rows

📚 Practice Resources

Kaggle	
Leetcode	Reorganize String
HackerRank	Window Functions

🚀 Outcome
Today’s exploration provided a hands-on and conceptual understanding of:

Writing portable ML models across frameworks.

Using heaps for string rearrangement problems.

Leveraging SQL window functions for advanced data analysis.


