
 🔥 Burnout Prediction App with Machine Learning

An AI-powered application to detect and visualize employee burnout levels based on workplace data. Built using Python, Streamlit, and Scikit-Learn.

---

## 📌 Project Overview

Employee burnout is a silent productivity killer and often goes undetected until it's too late. This app uses a machine learning model to predict burnout risk levels from structured employee data and provides an interactive interface for HR or leadership to take proactive actions.

---

## 🎯 Key Features

- 📁 Upload employee data via CSV
- 🧠 Pre-trained machine learning model for burnout classification
- ⚙️ Automated preprocessing pipeline
- 📊 Real-time prediction and visualization in a Streamlit app
- 🧾 Outputs predicted burnout level and human-readable labels

---

## 🛠 Tech Stack

- **Python 3.13**
- **Scikit-learn** – model training and pipeline
- **Pandas** – data manipulation
- **Joblib** – model & pipeline serialization
- **Streamlit** – web app interface

---

## 🚀 How to Run the App

### 1. Clone the repository

```bash
git clone https://github.com/your-username/burnout-prediction-app.git
cd burnout-prediction-app
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Launch the Streamlit app
bash
Copy
Edit
streamlit run app.py
📥 Sample CSV Format
Make sure your CSV follows this format:

csv
Copy
Edit
EmployeeID,Age,Gender,Department,JobLevel,MonthlyIncome,OverTime,WorkLifeBalance,JobSatisfaction,YearsAtCompany
1,29,Female,Sales,2,4500,Yes,2,4,3
2,35,Male,R&D,3,7200,No,3,3,7
...
You can find a sample file in the repository: sample_employee_data.csv

📂 Project Structure
bash
Copy
Edit
├── app.py                     # Streamlit application
├── burnout_model.pkl          # Trained ML model
├── preprocessor.pkl           # Feature transformation pipeline
├── label_map.pkl              # Mapping from numeric labels to readable ones
├── requirements.txt           # Python dependencies
└── sample_employee_data.csv   # Example input data
📈 Model Overview
The model was trained using logistic regression (or specify model type) on anonymized HR data. Features include:

Demographics (Age, Gender)

Workplace behavior (OverTime, WorkLifeBalance)

Job metrics (JobLevel, MonthlyIncome, YearsAtCompany)

✅ Use Cases
🧑‍💼 HR Analytics: Identify high-risk employees

🧠 Mental Health Monitoring: Early detection of burnout

📊 Executive Dashboards: Add real-time ML insights into reports

🙋‍♀️ Author
Dilrabo Khidirova
💼 Data Scientist & AI Engineer



https://www.kaggle.com/code/dilrabonu/remote-work-health-impact
