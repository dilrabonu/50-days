📦 Day 32: ML Deployment with FastAPI + Postman | DSA - Linked List | SQL - Cohort Retention Analysis

Welcome to Day 32 of my AI/ML Engineering & FAANG Preparation Roadmap!  
Today, we focused on **serving Machine Learning models via FastAPI**, testing them using **Postman**, mastering **Linked List problems**, and implementing **Cohort Analysis** in SQL for user retention insights.

---

## 🚀 Project Highlights

### 🧠 1. Machine Learning: Burnout Prediction API
We trained an ML model on the [Employee Burnout Dataset](https://www.kaggle.com/datasets/shivamb/employee-burnout-analysis) to predict employee burnout risk using features like age, income, satisfaction, and work-life balance.

#### 📌 ML Pipeline:
- Data Cleaning & Preprocessing (Label Encoding, Imputation)
- Feature Engineering
- Model Selection (Random Forest Classifier)
- Evaluation (Accuracy, Confusion Matrix, Classification Report)

#### 🧪 API Deployment:
- Built using **FastAPI**
- Accepts JSON input and returns burnout prediction
- Tested using **Postman** with real employee data samples

### 🌐 API Endpoint Example:
```http
POST /predict
Content-Type: application/json

{
  "Age": 30,
  "MonthlyIncome": 5000,
  "JobSatisfaction": 3,
  "WorkLifeBalance": 2,
  "YearsAtCompany": 5
}


✅ Response:

{
  "Burnout Risk": "High"
}
🔗 2. DSA: Linked List Challenges
We implemented and deeply understood:

Reverse Linked List – reversing a singly linked list in-place

Middle of Linked List – finding the midpoint using slow/fast pointers

These exercises strengthen core understanding of pointer manipulation and memory-efficient data structures, crucial for FAANG interviews.

📊 3. SQL: Cohort Analysis – Retention Tracking
We wrote SQL queries to analyze user retention by signup month:

Grouped users into cohorts by signup_date

Tracked activity by activity_date month difference

Calculated retention percentage over time

Tools: PostgreSQL / BigQuery

✅ Real-world use cases: SaaS platforms, user growth tracking, churn analysis

📌 Technologies Used
Python 3.10+

FastAPI

scikit-learn, pandas, numpy

Uvicorn (for API hosting)

Postman (for API testing)

PostgreSQL / BigQuery (for SQL analysis)

📚 Learning Outcomes
✅ Learned how to deploy ML models with FastAPI

✅ Practiced API testing and input validation using Postman

✅ Mastered key Linked List operations for interviews

✅ Analyzed user retention through cohort SQL logic

🔥 Next Steps
Dockerize the API

Add Swagger docs for input validation

Deploy on Render or Hugging Face Spaces

Extend DSA to doubly linked lists

Use Tableau or Power BI for visual cohort dashboard

💡 Author
Dilrabo Khidirova
