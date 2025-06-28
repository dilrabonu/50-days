# 🚀 Day 30 – FAANG Preparation Roadmap

Welcome to **Day 30** of my 50-day FAANG-level Machine Learning & Data Science preparation journey.  
Today, I focused on:

- ✅ Deploying ML models using **Flask + Docker**
- ✅ Practicing **Binary Search algorithms** in DSA
- ✅ Performing **Time Series Analysis in SQL** using rolling aggregations

---

## 💻 Machine Learning – Model Deployment with Flask + Docker

### 🔧 Goal:
Expose a trained ML model via an API and containerize the app for consistent deployment.

### ✅ Steps Covered:
1. Saved model using `joblib`
2. Created a REST API with **Flask**
3. Wrote a `Dockerfile` to containerize the application
4. Deployed locally using Docker

### 📁 Project Structure
📁 ml-deployment/
├── app.py

├── model.pkl

├── requirements.txt

└── Dockerfile




### 🔗 Sample API Request
```bash
POST http://localhost:5000/predict
Content-Type: application/json

{
  "features": [3.5, 1200, 2, 1]
}
📦 Technologies Used
Flask (for API)

Docker (for containerization)

joblib (for model serialization)

📌 Real-World Use Case:
Deployed a fraud detection model as an API to internal servers using Docker and Kubernetes, enabling real-time predictions in a bank’s transaction system.

💡 DSA – Binary Search
🔍 Problems Practiced:
Classic Binary Search

First Bad Version (Leetcode 278)

📘 Binary Search Template


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
✅ Concepts Mastered:
Searching sorted data in O(log n)

Applying binary logic to find first occurrence (e.g., bugs, limits)

🗃️ SQL – Time Series Analysis with Rolling Sales
📊 Goal:
Analyze rolling sales totals per product across months.

🧾 SQL Query:


SELECT 
  product_id,
  sale_month,
  SUM(sale_amount) AS current_month_sales,
  SUM(sale_amount) OVER (
    PARTITION BY product_id 
    ORDER BY sale_month 
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS rolling_3_month_sales
FROM sales;
✅ Concepts Applied:
Window Functions (OVER, PARTITION BY)

Rolling aggregates (ROWS BETWEEN)

Time-based insights for seasonality and trend analysis

📌 Real-World Use Case:
Retail company tracks 3-month rolling sales per product to predict inventory needs and detect seasonal trends.

📈 Summary of Learnings
Topic	Key Takeaway
ML Deployment	Created a full local ML API using Flask and Docker
Binary Search	Mastered efficient search algorithms and applications
SQL Time Series	Built rolling metrics for monthly sales trends
