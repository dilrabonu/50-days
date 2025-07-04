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
