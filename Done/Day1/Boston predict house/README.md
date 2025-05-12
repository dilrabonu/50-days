# 🏠 Boston Housing Price Prediction – Ridge, Lasso, ElasticNet Regression

## 📌 Objective
Predict median house values (`MEDV`) using advanced linear regression techniques with regularization to avoid overfitting.

---

## 🔍 Dataset
- Source: Kaggle Boston Housing Dataset
- Size: 506 records, 13 features + 1 target
- Features include: crime rate, number of rooms, pupil-teacher ratio, % lower-status population, etc.

---

## 🧪 Models Used
1. **Ridge Regression** (L2)
2. **Lasso Regression** (L1)
3. **ElasticNet Regression** (L1 + L2)

---

## 📈 Results

| Model      | RMSE     | R² Score |
|------------|----------|-----------|
| Ridge      | 4.93     | 0.56      |
| Lasso      | 4.92     | 0.57      |
| ElasticNet | 4.60 ✅ | 0.60 ✅   |

ElasticNet performed best by balancing bias-variance and performing feature selection.

---

## 📊 Visuals
- 📌 Heatmap of correlations
- 📌 Actual vs Predicted plot
- 📌 RMSE bar chart comparison
- 📌 Feature importance by model coefficients

---

## 🧠 Key Takeaways
- Regularized models reduce overfitting and handle multicollinearity.
- Lasso helps with feature selection.
- ElasticNet gives flexibility and robustness by combining Ridge and Lasso.

---

## 💾 Deployment
Best model saved as: `ridge_model.pkl`  
Ready to be deployed in Flask / Streamlit / FastAPI.

---

## 📁 Files
- `boston_regression.ipynb` – full implementation notebook
- `ridge_model.pkl` – saved model


![image](https://github.com/user-attachments/assets/61118a13-c5d3-4915-9c1c-6c2b6da0d597)

https://www.kaggle.com/code/dilrabonu/boston-predicting-house
