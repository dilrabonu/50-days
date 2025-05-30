# 🚀 Day 15 – FAANG Prep: Clustering, Stacks, and SQL CASE Statements

Welcome to **Day 15** of my 50-day journey to master Machine Learning, SQL, and Data Structures & Algorithms (DSA) for FAANG-level interviews. Today focused on unsupervised learning techniques, stack-based data structures, and conditional logic in SQL for dynamic segmentation.

---

## 📘 Machine Learning – Clustering for Customer Segmentation

### Topics Covered:
- **KMeans Clustering**: Partitioning customers into K groups using distance to centroids.
- **DBSCAN**: Identifying clusters based on density – useful for anomaly detection.
- **Hierarchical Clustering**: Building a tree of nested clusters using linkage methods and dendrograms.

### Real-World Applications:
- Segmenting customers by spending behavior.
- Detecting fraud or outlier behavior.
- Understanding user patterns in e-commerce or retail.

### Dataset Used:
- [Mall Customer Segmentation Dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation)

### Key Techniques:
- Data standardization using `StandardScaler`
- Choosing optimal clusters with the Elbow Method
- Visualization using `matplotlib` and `dendrogram`

---

## 💡 Data Structures & Algorithms – Stack Problems

### Concepts Learned:
- Stack = LIFO (Last In, First Out)
- Real-world analogy: Stack of plates / browser back button

### Problems Solved:
1. **Valid Parentheses** – Check if all opening brackets are closed correctly.
2. **Min Stack** – Build a stack that returns the minimum in O(1) time.

### Tools Used:
- Python list-based stack implementation
- LeetCode practice:
  - [Valid Parentheses (#20)](https://leetcode.com/problems/valid-parentheses/)
  - [Min Stack (#155)](https://leetcode.com/problems/min-stack/)

---

## 🗃️ SQL – CASE Statements for Dynamic Bucketing

### Concepts Practiced:
- Conditional logic in SQL using `CASE`
- Creating dynamic labels like age groups or spending tiers

### Real-World Example:
```sql
SELECT customer_id,
       revenue,
       CASE
           WHEN revenue < 100 THEN 'Low Spender'
           WHEN revenue BETWEEN 100 AND 500 THEN 'Medium Spender'
           ELSE 'High Spender'
       END AS spender_segment
FROM transactions;
Practice Platforms:
HackerRank – CASE Practice

✅ Key Takeaways
Clustering helps discover hidden patterns without labeled data.

Stacks are powerful for expression parsing and tracking state.

SQL CASE statements allow dynamic categorization without creating new tables or columns.


