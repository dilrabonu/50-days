# 📅 Day 22: Time Series with RNNs/LSTM/GRU | Stack DSA | SQL Data Cleaning

Welcome to Day 22 of my 50-Day FAANG Preparation Journey! 🚀  
Today's focus is on mastering **Recurrent Neural Networks (RNNs, LSTM, GRU)** for time series forecasting, **Stack data structures** in Python for DSA, and **SQL Data Cleaning techniques** for handling real-world messy datasets.

---

## 🔹 Machine Learning: RNNs, LSTM, GRU for Time Series Forecasting

### 📘 Objective:
Learn how to use RNN-based models to predict time series data such as stock prices or weather conditions.

### ✅ Covered Concepts:
- RNN (Recurrent Neural Network) fundamentals
- LSTM (Long Short-Term Memory) – gate mechanism for long-term memory
- GRU (Gated Recurrent Unit) – a lighter alternative to LSTM
- Sequence generation, windowing time series
- Normalization and preparation of time series data

### 🧠 Tools:
- Python, NumPy, Pandas, Matplotlib
- TensorFlow / Keras or PyTorch

### 📈 Use Case Example:
Stock price prediction using past 60 days’ closing prices.

---

## 🔹 DSA in Python: Stack – LIFO, Push, Pop, Valid Parentheses, Min Stack

### ✅ Covered Concepts:
- Stack: Last-In-First-Out structure
- Push and Pop operations
- Valid Parentheses: Matching brackets using a stack
- Min Stack: Support getMin() in O(1) time complexity

### 🧠 LeetCode Problems Solved:
- [x] Valid Parentheses
- [x] Min Stack

### 📚 Real-World Applications:
- Browser history navigation
- Undo-redo systems
- Expression evaluation

---

## 🔹 SQL: Data Cleaning (NULL, COALESCE, CASE)

### ✅ Covered Concepts:
- Detecting and handling `NULL` values
- Using `COALESCE()` to fill missing data
- `CASE` statements for conditional cleaning and classification
- Writing clean, maintainable SQL queries for preprocessing

### 🧹 Real-World Use Case:
Cleaning customer tables with missing values, standardizing column values (e.g., status, phone).

### 🧠 Sample Query:
```sql
SELECT 
  name,
  COALESCE(income, 0) AS income_clean,
  CASE 
    WHEN status IN ('active', 'Active', 'ACTIVE') THEN 'Active'
    ELSE 'Inactive'
  END AS cleaned_status
FROM users;
🔗 Folder Structure
pgsql
Copy
Edit
📁 Day22/
│
├── 📂 ml_time_series/
│   ├── lstm_stock_prediction.ipynb
│   ├── gru_temperature_forecast.ipynb
│
├── 📂 dsa_stack/
│   ├── valid_parentheses.py
│   ├── min_stack.py
│
├── 📂 sql_data_cleaning/
│   ├── cleaning_nulls.sql
│   ├── case_statement_examples.sql
✅ What I Learned Today:
Why LSTM and GRU are better for time series than vanilla RNN

How to implement stack logic for interview-style problems

The power of COALESCE and CASE in real-world SQL pipelines


