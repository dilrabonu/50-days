
# 🔥 California Wildfire Damage Analysis (2014–2023)

This project presents an end-to-end exploratory and predictive machine learning pipeline focused on analyzing wildfire incidents in California. The dataset contains details of 100 wildfire events including area burned, structures destroyed, injuries, and estimated financial loss.

---

## 📌 Project Objective

To analyze and model the estimated financial loss from wildfire incidents based on physical, temporal, and categorical features. The ultimate goal is to assist public safety organizations, environmental agencies, and insurers in better understanding wildfire impacts and risk factors.

---

## 🧰 Tools & Libraries

- Python 3.x
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn
- XGBoost
- Jupyter/Kaggle Notebook

---

## 📊 Workflow Summary

### 1. **Dataset Loading**
- CSV dataset with 100 wildfire incidents across California (2014–2023)
- Features: date, location, area burned, number of homes, businesses, vehicles affected, injuries, fatalities, and financial loss

### 2. **Data Cleaning**
- Verified nulls and duplicates
- Converted `Date` to datetime format
- Extracted `Year`, `Month`, and `Day` for temporal analysis

### 3. **Exploratory Data Analysis (EDA)**
- Visualized distribution of financial loss
- Identified key damage-causing years and causes
- Correlation heatmap of numeric features
- Average area burned by cause

### 4. **Feature Engineering**
- Label encoding of categorical features (`Cause`)
- Log-transformation of the target variable to handle skewness
- Defined structured input features for modeling

### 5. **Modeling Approaches**
- Baseline Random Forest Regressor
- Log-transformed regression using Random Forest
- Advanced modeling using XGBoost with early stopping
- Feature importance analysis using Gini Gain (XGBoost)

---

## 📈 Key Features Used in Modeling

- `Area_Burned (Acres)`
- `Homes_Destroyed`
- `Businesses_Destroyed`
- `Vehicles_Damaged`
- `Injuries`, `Fatalities`
- `Year`, `Month`, `Day`
- `Cause` (encoded)

---

## 🧠 What’s Next?

- Outlier handling (e.g. IQR filtering or quantile clipping)
- Classification-based modeling of financial risk (Low/Med/High/Extreme)
- External data integration: weather, satellite imagery, geolocation
- Deployment via dashboard (e.g. Power BI or Streamlit)




https://www.kaggle.com/code/dilrabonu/california-wildire-dataset-2014-2025
