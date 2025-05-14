# 📘 FAANG Prep Roadmap – Day 3

Welcome to **Day 3** of my 50-day FAANG preparation roadmap!  
Today's focus is on **Advanced Machine Learning**, **Sliding Window DSA**, and **SQL Top-N Query Patterns** — three critical topics for any aspiring ML Engineer or Software Developer aiming for top-tier companies like Google, Amazon, or Meta.

---

## 🔷 1. Advanced Classification Techniques

### 🧠 Topics Covered:
- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **ROC Curve and AUC Score**
- **Handling Imbalanced Datasets (e.g., Credit Card Fraud)**

### ✅ Key Learnings:
- Implemented Logistic Regression to classify fraudulent transactions.
- Used SVM with RBF kernel and `class_weight="balanced"` to handle imbalance.
- Visualized **ROC Curve** and calculated **AUC** to evaluate model performance.

### 📊 Tools:
- `scikit-learn` for model training and evaluation
- `matplotlib` and `seaborn` for visualizations

### 📂 Dataset:
[Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## 🧩 2. DSA – Sliding Window Technique

### 🎯 Problem Solved:
- **Longest Substring Without Repeating Characters**

### ✅ Key Concepts:
- Dynamic window resizing to optimize time complexity
- `set()` for constant-time character checks
- Real-world analogy: finding the longest stretch of unique notes in music

### 📎 Code Example:
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
🧪 LeetCode Practice:
Longest Substring Without Repeating Characters

Minimum Size Subarray Sum

💾 3. SQL – Top-N Queries
🧠 Topics Covered:
ORDER BY for sorting query results

LIMIT for restricting result count

OFFSET for pagination

🛠 Real Use Case:

-- Top 5 highest-paid employees
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;
🧪 Practice Queries:
Top 10 best-rated movies

Second page of bestselling products

Top 3 users with most transactions

📂 Dataset Suggestions:
IMDb Top 1000 Movies

Spotify 12M Songs Dataset

🏁 Summary
Skill	Mastery
🔹 Classification	Logistic Regression, SVM, ROC Curve
🔹 DSA	Sliding Window Problems
🔹 SQL	Top-N Ranking, Pagination
