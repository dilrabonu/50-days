# 🔍 Day 17: Anomaly Detection, Deque Data Structures & SQL Quartile Grouping  
> Part of the 50-Day FAANG Preparation Roadmap 🚀  

## 📌 Overview

This project focuses on three core topics essential for mastering technical interviews and real-world data applications:

1. **Machine Learning**: Anomaly detection using Isolation Forest and One-Class SVM for detecting rare fraudulent events in datasets.
2. **Data Structures & Algorithms (DSA)**: Deque and Monotonic Queue usage in sliding window problems, especially for the famous *Daily Temperatures* challenge.
3. **SQL Analytics**: Use of `NTILE()` and `PERCENT_RANK()` for quartile grouping and customer segmentation in large-scale databases.

---

## 🧠 Machine Learning: Anomaly Detection

### 📂 Dataset:
- **Name**: [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Size**: ~284,807 transactions
- **Imbalance**: Highly imbalanced dataset with <1% fraud

### 🔧 Techniques:
- **Isolation Forest**: Tree-based model that isolates anomalies quickly
- **One-Class SVM**: Kernel-based model for non-linear anomaly boundaries

### 📈 Use Case:
- Fraud detection in financial systems
- Unsupervised anomaly spotting in imbalanced data

### 🧪 Metrics:
- Precision, Recall, F1-Score, ROC AUC (used due to class imbalance)

---

## 🔁 DSA: Deque & Monotonic Queue

### 💡 Problems Solved:
- **[Daily Temperatures – LeetCode #739](https://leetcode.com/problems/daily-temperatures/)**
- Implemented using **monotonic decreasing stack**
- Time complexity: **O(n)**  
- Space complexity: **O(n)**

### 🔨 Tools:
- `collections.deque` in Python
- Optimized stack-based approach to track indices and temperatures

---

## 🧮 SQL: Quartile Grouping with NTILE and PERCENT_RANK

### 📊 Scenario:
Analyzing customer spending behavior by dividing into quartiles and evaluating percent ranks.

### 🔧 Functions Used:
- `NTILE(n) OVER (ORDER BY column)` – Used for bucket-based segmentation
- `PERCENT_RANK() OVER (ORDER BY column)` – For normalized ranking

### 🔗 Practice Links:
- [NTILE – HackerRank Practice](https://www.hackerrank.com/challenges/ntile/problem)
- [PERCENT_RANK – Microsoft Docs Example](https://learn.microsoft.com/en-us/sql/t-sql/functions/percent-rank-transact-sql)

---

## ✅ Key Takeaways

- Isolation Forest is fast and effective for high-dimensional anomaly detection.
- One-Class SVM provides non-linear separation but is sensitive to scale and tuning.
- Monotonic Queues simplify sliding window max/min problems with elegant O(n) solutions.
- NTILE and PERCENT_RANK are powerful for data analytics, segmentation, and business insights in SQL.

---

## 📚 Folder Structure

```bash
├── anomaly_detection/
│   ├── isolation_forest.ipynb
│   ├── one_class_svm.ipynb
│   └── dataset.csv (not uploaded, linked to Kaggle)
├── dsa/
│   └── daily_temperatures_monotonic_stack.py
├── sql/
│   ├── ntile_examples.sql
│   └── percent_rank_examples.sql
└── README.md

