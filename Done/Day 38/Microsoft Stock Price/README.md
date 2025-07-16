<img width="1369" height="428" alt="{6C5D9CF2-3FBE-4DC1-9F5F-EB0CEA41DF2F}" src="https://github.com/user-attachments/assets/79457f3c-02a5-4e78-9799-9bc2e13ebbaf" />

https://www.kaggle.com/code/dilrabonu/microsoft-stock-price-history

 Microsoft Stock Price Forecasting
This project explores time series forecasting techniques on Microsoft (MSFT) historical stock prices using classical and machine learning methods. We implement and compare ARIMA, Facebook Prophet, and XGBoost Regression to understand their effectiveness in predicting stock price trends.

🔍 Project Overview
The goal is to build a robust time series forecasting pipeline that:

Preprocesses stock price data

Engineers informative time-series features

Trains multiple forecasting models (ARIMA, Prophet, XGBoost)

Evaluates model performance using standard metrics (MAE, RMSE, MAPE)

Visualizes actual vs predicted prices

📊 Dataset
Source: Yahoo Finance (MSFT stock)

Period: 1986 – 2025 (Daily close prices)

Features: Date, Close, Lagged returns, Rolling means, Momentum, Seasonality

🔧 Methods Applied
✅ 1. ARIMA (AutoRegressive Integrated Moving Average)
Captures trend + autoregression + moving average

Requires stationarity preprocessing

Parameters selected via auto_arima with AIC minimization

✅ 2. Facebook Prophet
Decomposes time series into trend, seasonality, and holiday effects

Requires only 2 columns: ds (date) and y (target)

Automatically handles missing dates, outliers, and non-linear growth

✅ 3. XGBoost Regression
Supervised ML model trained on engineered lag features and rolling stats

Implements GridSearchCV for hyperparameter tuning

Scaled features with StandardScaler

📉 Model Evaluation
We use the following metrics:

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

MAPE (Mean Absolute Percentage Error)

📈 Visualizations
Each model's performance is plotted against the actual stock prices using:

Forecasted vs Actual plots

Time-based residual trends

Confidence intervals (Prophet only)

🚀 Future Work
Integrate LSTM and Transformer models for deep learning-based forecasting

Incorporate macroeconomic indicators and news sentiment

Build a Streamlit dashboard for interactive forecasting

🛠️ Tech Stack
Python (Pandas, Numpy, Matplotlib, Scikit-learn)

pmdarima, fbprophet, xgboost

Jupyter Notebook (Kaggle/Colab friendly)

👩‍💻 Author
Dilrabo Khidirova
Machine Learning Engineer | AI Forecasting Enthusiast
