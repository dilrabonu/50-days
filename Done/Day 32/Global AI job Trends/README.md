
# 🌍 Global AI Salary Predictor API with FastAPI 🚀

A complete end-to-end machine learning project that predicts AI-related job salaries using the **Global AI Job Trends and Salary Insights** dataset from Kaggle. The project includes data preprocessing, model training with XGBoost, and deployment using **FastAPI** for real-time salary prediction.

## 📌 Project Overview

The goal of this project is to:
- Predict the salary of an AI professional based on input features such as age, job level, department, gender, work-life balance, etc.
- Build a RESTful API using FastAPI to serve predictions via HTTP requests.
- Demonstrate an end-to-end ML lifecycle for real-world deployment scenarios.

---

## 📂 Directory Structure

├── main.py # FastAPI app file
├── xgb_model.pkl # Trained XGBoost regression model
├── feature_names.pkl # Ordered list of features used for prediction
├── requirements.txt # All dependencies needed to run the project
├── dataset/
│ └── ai_jobs.csv # Source Kaggle dataset (cleaned & processed)
└── README.md # Project documentation



---

## 🧠 Model Pipeline

1. **Dataset**: [Global AI Job Trends and Salary Insights](https://www.kaggle.com/datasets/promptcloud/global-ai-job-trends-and-salary-insights)
2. **Preprocessing**:
   - Encoding categorical variables (`Gender`, `Department`, `OverTime`)
   - Handling missing values
   - Feature selection: `Age`, `Gender`, `Department`, `JobLevel`, `MonthlyIncome`, `OverTime`, `WorkLifeBalance`, `JobSatisfaction`, `YearsAtCompany`
   - Feature scaling with `StandardScaler` (optional, based on model)
3. **Model**: `XGBoost Regressor`
4. **Evaluation**: RMSE, MAE, R² on train-test split
5. **Deployment**: FastAPI + Swagger UI for testing predictions

---

## 🚀 Run Locally

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/global-ai-salary-predictor-api.git
cd global-ai-salary-predictor-api
2️⃣ Install Dependencies

pip install -r requirements.txt
3️⃣ Run FastAPI App

uvicorn main:app --reload
4️⃣ Test via Swagger UI
Open your browser and visit:


http://127.0.0.1:8000/docs
🧪 Example Input

{
  "Age": 29,
  "Gender": "Female",
  "Department": "Sales",
  "JobLevel": 2,
  "MonthlyIncome": 4500,
  "OverTime": "Yes",
  "WorkLifeBalance": 2,
  "JobSatisfaction": 4,
  "YearsAtCompany": 3
}
📤 Example Response

{
  "prediction": 77472.69
}
🛠️ Tech Stack
Python 3.10+

Pandas, NumPy – for data manipulation

XGBoost – regression model

Scikit-learn – preprocessing & metrics

FastAPI – backend framework for API

Pydantic – request validation

Uvicorn – ASGI server

Swagger UI – built-in FastAPI docs

📈 Project Highlights
✅ Real-world ML use-case: AI job salary prediction
✅ Clean data pipeline and feature engineering
✅ FastAPI-based API deployment with Swagger UI
✅ Deployed model accepts real-time JSON input
✅ Ready-to-show portfolio project for ML Engineer role

👩‍💻 Author
Dilrabo Khidirova
🎓 Master’s in Software Engineering (Data & AI Track)
📫 LinkedIn
🌟 Passionate about AI, ML Deployment, and Building Intelligent Systems

📌 Future Enhancements
Add authentication to the API

Deploy on cloud (Heroku, Render, or AWS EC2)

Add Streamlit frontend for a full-stack app

Logging and monitoring with Prometheus/Grafana


![{70BCFBC0-137C-48A3-90AA-D0F76D467E2B}](https://github.com/user-attachments/assets/61f66804-7df9-419b-9483-04ba6136153a)

https://www.kaggle.com/code/dilrabonu/global-ai-job-market-trends-and-salary-insights
