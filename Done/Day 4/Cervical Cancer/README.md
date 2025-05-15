# 🩺 Cervical Cancer Risk Prediction – Explainable ML with SHAP (Day 4)

A machine learning pipeline built to **predict the risk of cervical cancer** based on behavioral and medical data. This project was developed as part of my **50-Day FAANG Preparation Journey (Day 4)** and demonstrates advanced techniques in:
- Cross-Validation (Manual K-Fold & Stratified K-Fold)
- Imbalanced classification handling
- Model explainability using SHAP

---

## 📂 Dataset
- **Source**: [Kaggle – Cervical Cancer Behavior Risk Dataset](https://www.kaggle.com/datasets/fedesoriano/cervical-cancer-behavior-risk)
- **Samples**: 858
- **Features**: 36 (sexual behavior, smoking, STDs, contraception, cancer screenings)
- **Target**: `Biopsy` (binary classification – 0: No risk, 1: At risk)

---

## 🎯 Business Objective
To develop a model that can **reliably identify women at high risk of cervical cancer** using routine health indicators — with a strong focus on **explainability and trustworthiness** of predictions.

---

## 🛠️ Techniques Used

### 📊 Exploratory Data Analysis (EDA)
- Distribution plots for age, sexual partners, smoking years
- Correlation matrix to identify redundant or highly correlated features
- Target imbalance visualization

### 🧼 Data Preprocessing
- Dropped noisy features and leakage (e.g., `Dx:Cancer`)
- Imputation of missing values
- Feature scaling with `StandardScaler`

### 🔁 Stratified K-Fold Cross-Validation
Used to handle **imbalanced target labels** (`Biopsy`) and get robust evaluation metrics.

### 🤖 Model: Logistic Regression
Trained on the full dataset using stratified 5-fold CV.

#### 📈 Performance Metrics:
| Metric      | Value |
|-------------|--------|
| Accuracy     | 0.958 |
| Precision    | 0.643 |
| Recall       | 0.818 |
| F1 Score     | 0.720 |

📌 **Recall was prioritized** due to the critical nature of catching high-risk cases.

---

## 🔍 SHAP Explainability

Used `SHAP` to analyze the contribution of each feature to model predictions.

### 🧠 Top Contributing Features:
- `STDs: Number of diagnosis`
- `Dx:CIN`
- `Number of sexual partners`
- `Hormonal Contraceptives`
- `Dx:HPV`
- `Age`

```python
import shap
explainer = shap.Explainer(model, X_scaled)
shap_values = explainer(X_scaled)
shap.summary_plot(shap_values, features=X, feature_names=X.columns)

https://www.kaggle.com/code/dilrabonu/cervical-cancer
![image](https://github.com/user-attachments/assets/4b5bf19c-2c6a-4477-b830-6db59dcfe6d5)

