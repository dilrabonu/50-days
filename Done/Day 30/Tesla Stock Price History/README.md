# 🚀 Tesla Stock Price Prediction API

This is a Flask-based REST API that serves a machine learning model trained to predict Tesla's stock closing price based on input features. The model was trained using Scikit-learn and saved as a `.pkl` file.

---

## 📂 Project Structure
Tesla Stock Price History/
├── app.py
├── test_api.py
├── evaluate_api.py
├── visualise.py
├── requirements.txt
├── tesla_stock_model.pkl
├── README.md




---

## 🧠 Model Info

- **Model Type**: Linear Regression
- **Framework**: Scikit-learn
- **Trained On**: Historical Tesla stock data
- **Input Features**: Must be provided as a list of numerical values
- **Output**: Predicted stock closing price

---

## ▶️ How to Run Locally (No Docker)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
Run Flask App


python app.py
The app will start at:

cpp
Copy
Edit
http://127.0.0.1:5000/
🔁 API Endpoints
🔹 GET /
Returns a simple health check message.

Example Response:


"Tesla Stock Model is Live!"
🔹 POST /predict
Takes in stock market features and returns the predicted closing price.

Request:


POST /predict
Content-Type: application/json

{
  "features": [1.5, 3.2, 0.9, 2.1]  # Example input
}
Response:


{
  "predicted_close_price": 203.15
}
🧪 Example Test Using Python

import requests

url = "http://127.0.0.1:5000/predict"
data = {"features": [1.5, 3.2, 0.9, 2.1]}  # Replace with actual input
response = requests.post(url, json=data)
print(response.json())