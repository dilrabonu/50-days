# 🔐 Credit Card Fraud Detection Using Advanced Classification Techniques

This project tackles the challenge of **detecting fraudulent transactions** in real-world, highly imbalanced financial data using advanced machine learning algorithms and evaluation metrics. The goal is to create a scalable, interpretable, and efficient fraud detection model.

---

## 📌 Project Objective

- **Business Goal:** Build a machine learning pipeline that accurately detects fraudulent credit card transactions.
- **Challenge:** Fraudulent transactions represent less than 0.2% of the data—creating an **extreme class imbalance**.
- **Solution:** Apply advanced ML techniques and evaluation metrics to handle imbalance and optimize fraud detection performance.

---

## 📊 Dataset

- 📁 Source: [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- 🧾 Description: 284,807 transactions with 30 anonymized features (V1–V28 via PCA), `Amount`, `Time`, and `Class` (target: 0 = non-fraud, 1 = fraud)

---

## 🧠 Techniques & Tools Used

| Task | Tools/Methods |
|------|----------------|
| Data Cleaning | `pandas`, `duplicated().sum()`, `.isnull()` checks |
| Feature Scaling | `StandardScaler` for `Amount` and `Time` |
| Class Imbalance Handling | `class_weight='balanced'` in models |
| Modeling | `LogisticRegression` from `scikit-learn` |
| Evaluation | `roc_auc_score`, `roc_curve`, `matplotlib` |
| Deployment Readiness | `joblib` model saving |

---

## ⚙️ ML Pipeline Overview

### 1. **Data Cleaning**
- Removed 1,081 duplicate records
- Verified no missing values

### 2. **Feature Engineering**
- Applied `StandardScaler` to `Amount` and `Time`
- Dropped original unscaled columns

### 3. **Exploratory Data Analysis**
- Used `seaborn` to visualize class imbalance

### 4. **Model Training**
- Trained `LogisticRegression` with `class_weight='balanced'`
- Focused on **ROC AUC** instead of accuracy due to class imbalance

### 5. **Model Evaluation**
- Achieved **ROC AUC Score: 0.9656**
- Visualized **ROC Curve** for performance insight

### 6. **Model Saving**
- Exported model with `joblib` for future use or deployment

---

## 📈 Results

- 🚀 The model successfully identified fraudulent transactions with **high true positive rate** and **low false positives**
- 📉 Overcame the limitations of accuracy by using **ROC AUC and ROC Curve**
- 🔍 Insights gained on how to handle real-world imbalanced datasets with business-critical implications

---

---

## 💡 Key Learnings

- Importance of **choosing the right evaluation metric** for imbalanced datasets
- Practical application of **Logistic Regression** and **class weighting**
- End-to-end pipeline from cleaning → training → evaluation → saving model

---

## 📌 Next Steps

- 🔁 Try Random Forest and XGBoost for model comparison
- 🧠 Add SHAP or LIME for model explainability
- 💡 Build a simple Streamlit dashboard for real-time prediction

---

## 🧰 Tech Stack

- Python, Pandas, Scikit-Learn, Seaborn, Matplotlib, Joblib

---

## 🤝 Let’s Connect

If you're working on projects involving **financial risk**, **AI in real-world applications**, or **ML in production**, I’d love to collaborate, share ideas, or get feedback.  
📩 Reach out on https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/

---

> "Good fraud detection is not just about accuracy. It’s about trust, interpretability, and actionability."





https://www.kaggle.com/code/dilrabonu/credit-card-fraud-dataset
