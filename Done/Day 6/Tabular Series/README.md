
![image](https://github.com/user-attachments/assets/db2b9780-95c0-4571-8633-7664487d7447)

# 🚀 Tabular Playground Series – Feb 2021: End-to-End ML Pipeline with SHAP Explainability

Welcome! This repository contains a full professional machine learning pipeline built using the **Tabular Playground Series – Feb 2021** dataset from Kaggle. It demonstrates data preprocessing, exploratory data analysis, model benchmarking (XGBoost, LightGBM, CatBoost), and explainability using SHAP.

---

## 🧠 Project Objective

Predict a continuous `target` variable using:
- 🧾 10 categorical features (`cat0` to `cat9`)
- 📊 14 continuous features (`cont0` to `cont13`)
- 📁 Dataset size: 300,000 training rows, 200,000 test rows

---

## 🛠️ Tools & Libraries

- Python 3.11
- Pandas, NumPy
- Seaborn, Matplotlib, Plotly
- Scikit-learn
- XGBoost, LightGBM, CatBoost
- SHAP (Explainable AI)

---

## 📊 Workflow Overview

### ✅ Step 1: Exploratory Data Analysis
- Visualized value distribution using **boxenplots**
- Used **correlation heatmaps** to identify multicollinearity
- Explored categorical feature frequencies and cardinality

### ✅ Step 2: Preprocessing
- Applied **Label Encoding** to all categorical features
- Standardized continuous features using **StandardScaler**
- Ensured **no data leakage** by fitting encoders on training data only

### ✅ Step 3: Model Training
Benchmarked three state-of-the-art models:
| Model      | R² Score | MSE     |
|------------|----------|---------|
| XGBoost    | 0.8908   | 0.7178  |
| LightGBM   | 0.8926   | 0.7164  |
| CatBoost   | 0.8934   | 0.7236  |

- All models trained using 80/20 train-validation split
- Metrics evaluated: **R² Score**, **Mean Squared Error**

### ✅ Step 4: Feature Importance
- XGBoost revealed `cat1`, `cat2`, and `cat0` as top predictors
- Most `cont*` features had moderate to low influence

### ✅ Step 5: Explainability with SHAP
- Used **SHAP Explainer** to analyze prediction impacts
- Visualized global importance with **SHAP Beeswarm Plot**
- Interpreted how each feature (high/low) pushed predictions



### ✅ Step 6: Submission
- Generated predictions using CatBoost model
- Created a Kaggle-ready `submission.csv` file

---


---

## 📌 Key Takeaways

- Demonstrated full ML pipeline including EDA, modeling, tuning, and explainability
- Benchmarked 3 high-performing tree-based algorithms
- Applied SHAP to make models interpretable and production-ready
- Built entirely in Python with clean, reproducible code

---




https://www.kaggle.com/code/dilrabonu/tabular-playground-series
