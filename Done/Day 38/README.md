# 📈 Day 38 - ML/FAANG Prep Journey

Welcome to Day 38 of my Machine Learning + FAANG interview preparation! This day covers **Time Series Forecasting (ARIMA + Prophet)**, **Stack & Queue Challenges (Evaluate RPN, Daily Temperatures)**, and **SQL Security (Permissions & Roles)**. Each topic includes real-world context, code snippets, and FAANG-style thinking.

---

## 🔮 Machine Learning - Time Series Forecasting (ARIMA + Prophet)

### 📌 ARIMA
ARIMA (AutoRegressive Integrated Moving Average) is a classical forecasting model best suited for univariate time series that can be made stationary.

- **Use Case**: Predicting monthly product sales
- **Components**: AR (lags), I (differencing), MA (residuals)
- **Python Example**:
```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(data, order=(1,1,1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=5)
📌 Prophet (by Facebook)
Prophet is a robust, automatic forecasting library designed for business time series data with seasonality and holidays.

Use Case: Forecasting website traffic or video views

Components: Trend + Seasonality + Holidays

Python Example:


from prophet import Prophet

df = df.rename(columns={'date': 'ds', 'value': 'y'})
model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
🧱 DSA - Stack & Queue Challenges
🔢 Evaluate Reverse Polish Notation (RPN)
Given an array of tokens representing an RPN expression, evaluate the value using a stack.


def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(int(eval(f"{a}{token}{b}")))
    return stack[0]
Input: ["2", "1", "+", "3", "*"]

Output: 9

🌡️ Daily Temperatures
Return the number of days you have to wait until a warmer temperature using a monotonic stack.


def dailyTemperatures(temps):
    res = [0] * len(temps)
    stack = []
    for i in range(len(temps) - 1, -1, -1):
        while stack and temps[i] >= temps[stack[-1]]:
            stack.pop()
        if stack:
            res[i] = stack[-1] - i
        stack.append(i)
    return res
Input: [73, 74, 75, 71, 69, 72, 76, 73]

Output: [1, 1, 4, 2, 1, 1, 0, 0]

🛡️ SQL - Security: Permissions & Roles
📌 Key Concepts
Permissions: What actions users can perform (e.g., SELECT, INSERT)

Roles: Grouping of permissions for better access control

📂 Access Control Example

-- Create a role
CREATE ROLE analyst;

-- Grant permissions
GRANT SELECT ON sales_data TO analyst;

-- Assign role to user
GRANT analyst TO user_dilrabo;

-- Revoke permissions or role
REVOKE SELECT ON sales_data FROM analyst;
REVOKE analyst FROM user_dilrabo;
Use Case: Role-Based Access Control (RBAC) for enterprise-level databases

🎯 FAANG Interview Highlights
Topic	Sample Questions
ARIMA vs Prophet	How do you handle seasonality and missing data?
Stack Problems	Explain monotonic stack and its use in Daily Temperatures
SQL Roles	How would you design access control for a multi-team project?

✅ Summary
Built time series models using ARIMA and Prophet

Solved real-world stack/queue problems like Evaluate RPN and Daily Temperatures

Implemented secure, scalable role-based SQL permissions


