https://www.kaggle.com/code/dilrabonu/ai-developer-productivity-dataset

# 🤖 AI Developer Productivity Prediction

This project predicts whether a developer will successfully complete a task (`task_success`) based on behavioral and contextual features such as hours coding, coffee intake, sleep, distractions, AI tool usage, cognitive load, commits, and bugs reported.

## 📌 Project Objective

To build a **machine learning classification model** that uses behavioral data to:
- Predict task success (0 = failed, 1 = succeeded)
- Understand the most impactful features
- Apply and demonstrate ML concepts like **bias-variance tradeoff**, **cross-validation**, and **overfitting prevention**

---

## 📁 Dataset Overview

**File**: `ai_dev_productivity.csv`  
**Rows**: 500  
**Target**: `task_success`  
**Features**:
- `hours_coding`
- `coffee_intake_mg`
- `distractions`
- `sleep_hours`
- `commits`
- `bugs_reported`
- `ai_usage_hours`
- `cognitive_load`

---

## 📊 Exploratory Data Analysis (EDA)

- Checked for missing and duplicate values
- Visualized feature distributions using boxplots, KDE plots, and pairplots
- Built a correlation heatmap to examine feature relationships
- Analyzed class distribution for balance

---

## 🧠 Machine Learning Pipeline

### ✅ Preprocessing
- Standardized features using `StandardScaler`
- Stratified train/test split to preserve class ratios
- Feature-target separation

### ✅ Modeling
- **Logistic Regression** baseline
- Applied **5-fold cross-validation** to ensure stability
- Evaluated using:
  - Accuracy
  - ROC AUC Score
  - Confusion Matrix

---

## 🎯 Results

| Metric           | Score        |
|------------------|--------------|
| Cross-Val Mean Accuracy | `0.86` |
| Test Accuracy    | `0.93`       |
| Test ROC AUC     | `0.97`       |

📌 **Confusion Matrix Summary**:
- True Positives (TP): 59  
- True Negatives (TN): 34  
- False Positives (FP): 5  
- False Negatives (FN): 2  

---

## 🧪 Machine Learning Concepts Applied

| Concept              | Implementation                            |
|----------------------|--------------------------------------------|
| **Bias-Variance Tradeoff** | Balanced by using simple interpretable models + cross-validation |
| **Overfitting Prevention** | Cross-validation, test evaluation, regularization |
| **Model Evaluation** | Accuracy, ROC AUC, confusion matrix |
| **Explainability** | Coefficients of logistic regression interpreted |

---

## 📈 Feature Importance

Feature influence (sorted):
- `sleep_hours` ✅
- `hours_coding` ✅
- `ai_usage_hours` ✅
- `cognitive_load` ❌
- `distractions`, `bugs_reported`, `coffee_intake` had less predictive power

---

## 🔁 Future Work

- 🔍 Compare with advanced models (Random Forest, XGBoost)
- 🧠 Integrate **SHAP or LIME** for explainability
- 🌍 Deploy using **Streamlit**
- 📂 Create a dashboard or reporting app

---

## 📚 Learnings

This project demonstrated how real-world behavioral data can be used to:
- Predict outcomes with solid ML techniques
- Apply fundamental theory (bias, variance, cross-validation)
- Derive practical and interpretable insights for productivity

---

## 🧩 Tech Stack

- Python (Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn)
- Jupyter Notebook / Google Colab
- Logistic Regression
- Stratified K-Fold CV

---

## 🙋‍♀️ Author

**Dilrabo Khidirova**  
AI/ML Enthusiast | Data Scientist in Training | Women in Tech Advocate  
