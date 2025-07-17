# 🚚 Amazon Delivery Dataset – Delivery Delay Prediction & Time Estimation (ML Project)

Analyzing Last-Mile Logistics Performance with Machine Learning  
📦 Predicting Delays | ⏱ Estimating Delivery Time | 📊 Feature Insights | 🧠 Future AI Agent

---

## 📌 Project Overview

This project explores **last-mile delivery optimization** using the [Amazon Delivery Dataset](https://www.kaggle.com/datasets/shivamb/amazon-delivery-performance-dataset).  
We developed robust **classification** and **regression** models to:

- 🚦 Predict if a delivery will be **delayed** (`Is_Delayed`)
- ⏱ Estimate the **delivery time** in minutes (`Delivery_Time`)
- 💡 Extract insights from traffic, weather, agent ratings, and geographic factors
- 🔁 Prepare for AI agent integration for real-time decision support

---

## 🧠 Problem Statements

### 1. Classification Task
> Will the delivery be delayed?

- **Type**: Binary Classification  
- **Target**: `Is_Delayed`  
- **Models Used**: Logistic Regression (baseline), LightGBM, Neural Network (optional)  
- **Best Score**:  
  - Accuracy: **87%**  
  - ROC AUC: **0.93**

### 2. Regression Task
> What is the expected delivery time (in minutes)?

- **Type**: Regression  
- **Target**: `Delivery_Time`  
- **Models Used**: RandomForestRegressor, XGBoostRegressor  
- **Best Score**:  
  - MAE: **~23 min**  
  - RMSE: **~31 min**  
  - R² Score: **0.73 (RF)**, **-0.17 (XGBoost)**

---

## 🧹 Data Preprocessing

- ✅ Missing value imputation:
  - `Agent_Rating`: Imputed with **median**
  - `Weather`: Imputed with **mode**
- ✅ Feature Engineering:
  - `order_hour`, `is_weekend`, `distance_km`
- ✅ Categorical Encoding: OneHot for `Traffic`, `Weather`, `Vehicle`, etc.
- ✅ Data Cleaning: Filtered invalid or malformed time entries

---

## 📦 Features Used

| Type       | Features |
|------------|----------|
| Numerical  | `Agent_Age`, `Agent_Rating`, `distance_km`, `order_hour` |
| Categorical| `Weather`, `Traffic`, `Vehicle`, `Area`, `Category` |
| Temporal   | `order_dayofweek`, `is_weekend` |

---

## 🔧 Tech Stack

- **Python** (Pandas, NumPy, Scikit-Learn, XGBoost)
- **Jupyter Notebooks**
- **Matplotlib/Seaborn** for EDA
- **VS Code** (for AI Agent deployment - next stage)

---

## 📁 File Structure

amazon-delivery-ml/
│
├── data/
│ └── amazon_delivery.csv
├── notebooks/
│ └── 01_EDA_Cleaning.ipynb
│ └── 02_Classification_Model.ipynb
│ └── 03_Regression_Model.ipynb
│
├── models/
│ └── delivery_time_regressor.pkl
│ └── delay_classifier.pkl
│
├── assets/
│ └── visualization.png
│
└── README.md

yaml
Copy
Edit

---

## 🧠 Next Steps – AI Logistics Agent (🧭 Coming Soon)

> Our next goal is to build a **VS Code-powered AI Agent** that:

- Recommends best delivery agents for urgent orders
- Suggests fastest routes (based on traffic/weather)
- Predicts risk of delay and reroutes
- Visual UI with Streamlit or FastAPI

---

## 🤝 Contributing

Have ideas for optimization, model tuning, or visualization improvements?  
Feel free to fork, open issues, or submit PRs!

