
# 📊 Google Stock Price Analysis (2015–2024)

This repository contains a complete exploratory data analysis (EDA) and visualization pipeline for the **Google Stock Prices dataset (2015–2024)**. The goal is to uncover trends, relationships, and anomalies in nearly a decade of financial data using Python-based tools.

## 📁 Dataset

- **Source**: [Kaggle - Google Stock Prices](https://www.kaggle.com/)
- **Period**: January 2015 to early 2024
- **Features**:
  - `Date`
  - `Open`
  - `High`
  - `Low`
  - `Close`
  - `Volume`

## 🧪 Key Steps

### ✅ 1. Data Cleaning & Preprocessing
- Converted `Date` to datetime format
- Checked and removed duplicates
- Verified null values (none found)
- Sorted data by time for time series consistency

### 📈 2. Exploratory Data Analysis (EDA)
- Used `.info()` and `.describe()` for basic inspection
- Plotted feature trends and closing price evolution
- Generated **correlation heatmaps** to identify multicollinearity
- Visualized rolling mean, volatility zones, and spike patterns

### 🎨 3. Visualization Tools
- **Matplotlib**: Publication-ready static charts
- **Seaborn**: Correlation matrices, distribution plots
- **Plotly**: Interactive time series and candlestick plots

## 📦 Tech Stack

| Tool        | Purpose                            |
|-------------|------------------------------------|
| `Python`    | Core language                      |
| `Pandas`    | Data manipulation & transformation |
| `Matplotlib`| Static plotting                    |
| `Seaborn`   | Heatmaps, distributions            |
| `Plotly`    | Interactive plotting               |
| `Jupyter`   | Analysis notebook                  |

## 🔍 Key Insights

- `Open`, `High`, `Low`, and `Close` are **highly correlated (≈1.0)** → feature engineering opportunities
- `Volume` shows moderate correlation with price, especially during volatile periods
- Noticeable trends during major tech booms, economic downturns, and market rebounds

## 📌 Future Work

This EDA lays the groundwork for:
- 📉 Anomaly detection using Z-Score, Isolation Forest, LSTM Autoencoders
- 📈 Forecasting using ARIMA, Prophet, XGBoost
- 🤖 Building an AI-powered anomaly monitoring app

---

## 🤝 Let's Collaborate

If you're interested in time series forecasting, financial AI, or building intelligent stock agents — feel free to fork, star ⭐ this repo, and connect on 
https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/

---

## 📎 License

MIT License © 2025

https://www.kaggle.com/code/dilrabonu/google-stock-price-2015-2024
