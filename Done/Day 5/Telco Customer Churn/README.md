

![image](https://github.com/user-attachments/assets/5902eddf-de51-46aa-bae8-6afb3045b6f8)

# 📈 Customer Churn Prediction – Telco Dataset

Predicting which customers are likely to cancel their subscription is critical for business retention strategies. This end-to-end machine learning project uses the Telco Customer dataset to identify churn patterns and build an optimized predictive model.

---

## 📦 Dataset
**Source:** [Telco Customer Churn Dataset on Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn)

**Size:** 7,043 rows × 21 columns  
**Target:** `Churn` (Yes/No)

---

## 🎯 Objective

Build a machine learning model that accurately predicts customer churn and provides insights into the most influential features contributing to it.

---

## 🧪 ML Task
- **Type:** Supervised Learning
- **Goal:** Binary Classification (Churn: Yes/No)

---

## 🧠 Pipeline Overview

### 1. Data Exploration & Cleaning
- Handled categorical and numerical variables
- Converted `TotalCharges` to numeric and removed invalid entries
- Verified class imbalance (≈ 26% churned)

### 2. Feature Engineering
- Dropped `customerID` (non-informative)
- One-Hot Encoded categorical variables
- Split into training and test sets (80/20 stratified)

### 3. Model Building
- **Baseline:** Logistic Regression (with `class_weight='balanced'`)
- **Optimized Model:** Random Forest + GridSearchCV
- **Evaluation Metrics:** Accuracy, F1-Score, Confusion Matrix, ROC Curve

### 4. Model Explainability & Deployment
- Visualized key performance metrics
- Saved best model using `joblib` for future use

---

## 🧾 Key Results

| Model              | Accuracy | Churn Precision | Churn Recall | Churn F1 |
|-------------------|----------|------------------|--------------|----------|
| Logistic Regression | 0.73     | 0.49             | 0.78         | 0.60     |
| Random Forest (tuned) | **0.77** | **0.55**         | **0.75**     | **0.64** |

✅ **Best Params:** `{'n_estimators': 100, 'max_depth': 10, 'min_samples_split': 2}`

---

## 📊 Key Insights

- Customers with **month-to-month contracts**, **no tech support**, and **higher monthly charges** are more likely to churn.
- **Tenure** is a strong retention indicator: longer-tenure customers are more stable.
- **Electronic check** payment users had the highest churn rate.

---

## 📂 Tools & Libraries
- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn (LogisticRegression, RandomForest, GridSearchCV)
- Joblib for model persistence

---

## 💡 Business Impact
This model can help companies:
- Proactively retain at-risk customers
- Optimize contract types and services
- Improve loyalty through targeted offers

---

## 🚀 Next Steps
- Deploy model in a Streamlit dashboard or API
- Add SHAP/ELI5 for feature importance explainability
- Explore advanced models (XGBoost, LightGBM)

---

## 📎 Author
**Dilrabo Khidirova**  
ML/AI Engineer | Data Scientist  
https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/

---

