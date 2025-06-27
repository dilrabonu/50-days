# 🧠 Day 39 – FAANG Preparation Roadmap

Welcome to **Day 39** of my 50-day FAANG Data Scientist & ML Engineer preparation journey!  
Today’s focus was on **MLOps**, **Two Pointers in DSA**, and **Feature Engineering in SQL**.

---

## 📘 Machine Learning: What is MLOps?

MLOps (Machine Learning Operations) is the discipline of building, deploying, and maintaining ML models in production efficiently and reliably. It bridges the gap between data science and DevOps.

### 🔧 Topics Covered:
- MLOps Architecture (Data → Model → Deployment → Monitoring)
- CI/CD for ML models (Automation of training and deployment)
- Model versioning, reproducibility, and automation
- Tools: MLflow, DVC, Kubeflow, Airflow, Docker, Seldon

### ✅ Real-World Example:
Built a fraud detection pipeline that auto-trains weekly with retraining triggers based on model drift. Used GitHub Actions + MLflow + Docker for CI/CD.

---

## 💻 DSA: Two Pointers Technique

### ✅ Problems Solved:
- **Valid Palindrome**
  - Clean and compare string using two pointers
- **Reverse String**
  - In-place reversal using two-pointer swapping

### 🧠 Why Two Pointers?
Efficient for problems involving symmetrical comparisons, substring checks, or inplace modifications.

```python
def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]: return False
        left += 1; right -= 1
    return True

🗃️ SQL: Feature Engineering
SQL is a powerful tool for aggregating raw data into meaningful features for machine learning models.

📌 Techniques Practiced:
COUNT, AVG, MAX aggregations

Time-based metrics (recency, frequency)

CASE WHEN for bucketing users

Window functions for rolling sums

sql
Copy
Edit
SELECT 
  customer_id,
  COUNT(order_id) AS order_count,
  AVG(order_value) AS avg_order_value,
  MAX(order_value) AS max_order
FROM orders
GROUP BY customer_id;
