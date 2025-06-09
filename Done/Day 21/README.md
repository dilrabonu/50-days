# 🚀 Day 21 – FAANG Preparation Roadmap

Welcome to **Day 21** of my 50-Day FAANG Preparation Challenge!  
Today’s focus areas are:

- ✅ Machine Learning: Transfer Learning using ResNet & EfficientNet
- ✅ Data Structures & Algorithms: Arrays Basics (Traversal, Sum, Max), Two Sum, Max Consecutive Ones
- ✅ SQL: Window Functions + Aggregation (Mock Interview Round 1)

---

## 📌 1. Machine Learning – Transfer Learning (ResNet & EfficientNet)

### 🔍 Objective
Leverage pre-trained deep learning models to solve custom image classification problems using Transfer Learning.

### 🧠 Key Concepts
- Pre-trained models (ImageNet)
- Freezing and unfreezing layers
- Custom classifier head
- Fine-tuning EfficientNet and ResNet on domain-specific datasets

### 🧪 Frameworks Used
- PyTorch
- TensorFlow
- torchvision / keras.applications

### 📦 Dataset
Wildfire

### 🔨 Tasks Implemented
- Load & preprocess image data
- Use EfficientNetB0 and ResNet50
- Fine-tune top layers
- Train model & evaluate performance
- Save model and visualize metrics

---

## 🧠 2. Data Structures & Algorithms – Arrays

### 🔍 Topics Covered
- Traversal, sum, and max operations on arrays
- Classic interview problems:
  - ✅ Two Sum (O(n) with hashmap)
  - ✅ Max Consecutive Ones (count longest run)

### 📘 LeetCode Problems
- [Two Sum](https://leetcode.com/problems/two-sum/)
- [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)

### 💡 Key Takeaways
- Optimize time complexity using hashmaps
- Practice array manipulation as the foundation of many FAANG questions

---

## 🧮 3. SQL – Window Functions & Aggregation

### 🔍 Focus
- Window functions: `RANK()`, `LAG()`, `LEAD()`, `ROW_NUMBER()`
- Use `PARTITION BY`, `ORDER BY` in analytical queries
- Running totals, previous row comparisons, trends

### 📘 HackerRank Practice
- [Weather Observation Station](https://www.hackerrank.com/challenges/weather-observation-station-13)
- [SQL Window Functions Practice](https://www.hackerrank.com/skills-directory/sql?filters=window-functions)

### 🧠 Mock Interview Example
```sql
SELECT 
  customer_id, 
  transaction_id, 
  amount,
  LAG(amount) OVER(PARTITION BY customer_id ORDER BY transaction_date) AS prev_amount,
  amount / NULLIF(LAG(amount) OVER(PARTITION BY customer_id ORDER BY transaction_date), 0) AS ratio
FROM transactions;
🎯 Summary
Area	Topic	Tools	Practice
ML	Transfer Learning	PyTorch, TensorFlow	Kaggle
DSA	Arrays (Two Sum, Max 1s)	Python	LeetCode
SQL	Window Functions	SQL	HackerRank

🧠 FAANG Interview Insights
✅ Transfer Learning helps when training data is limited

✅ Arrays are the foundation of DSA mastery

✅ Window functions are essential in analytics-heavy data science roles


