# ❤️ Heart Disease Prediction with Machine Learning

An end-to-end Machine Learning pipeline to **predict the risk of heart disease** using real-world patient data. This project follows **FAANG-style best practices**, combining deep data exploration, rigorous feature selection, model building, evaluation, and explainability using SHAP.

---

## 📊 Project Overview

**Objective:**  
To build an interpretable and high-performing ML model that can accurately predict whether a patient has heart disease, based on clinical attributes.

**Business Use Case:**  
Early prediction of heart disease risk enables:
- Timely medical interventions 🏥
- Integration into preventive care platforms 📱
- Clinical decision support systems for doctors 👩‍⚕️

---

## 🧠 Dataset

- **Name:** Heart Disease UCI Dataset
- **Source:** [Kaggle – Heart Failure Prediction](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
- **Samples:** 918 patients
- **Features:** 12 (categorical + numerical)
- **Target:** `HeartDisease` (1 = disease, 0 = no disease)

---

## 🛠️ Tools & Libraries

- Python 🐍
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-Learn
- XGBoost
- SHAP
- Joblib

---

## 📈 ML Pipeline Breakdown

### ✅ Step 1: Data Cleaning & EDA
- Removed duplicates and checked for missing values
- Handled categorical features with One-Hot Encoding
- Visualized distributions and correlations
- Identified outliers in features like `Cholesterol`, `Oldpeak`

### ✅ Step 2: Feature Selection
Used three complementary approaches to rank feature importance:
- **Lasso (L1 Regularization)**
- **SelectKBest (Univariate Stats)**
- **SHAP (Model Explainability)**

🧠 Top Features Identified:
- `ST_Slope_Up`, `ST_Slope_Flat`
- `Oldpeak`, `ExerciseAngina_Y`
- `MaxHR`, `Cholesterol`, `Age`

### ✅ Step 3: Model Training
Trained and evaluated 3 ML models:
- **Logistic Regression**
- **Random Forest**
- **XGBoost**

### ✅ Step 4: Model Evaluation

| Model         | Accuracy | Precision | Recall | F1 Score | ROC AUC |
|---------------|----------|-----------|--------|----------|---------|
| **RandomForest**  | 0.8206   | 0.8700    | **0.8130** | 0.8406   | **0.9041** ✅  
| XGBoost         | 0.8152   | **0.8842**  | 0.7850 | 0.8316   | 0.8878  
| Logistic        | 0.8043   | 0.8558    | 0.7949 | 0.8252   | 0.8875  

### ✅ Step 5: Model Explainability
- Used **SHAP force plots** to explain individual predictions
- Built interactive explanations for patient-level insights
- Visualized SHAP summary (global feature impact)

---



https://www.kaggle.com/code/dilrabonu/heart-failure-prediction
