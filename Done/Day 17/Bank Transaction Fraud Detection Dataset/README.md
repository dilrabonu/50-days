

![{1562180B-EB8E-46DB-8B17-D1369C5CBFFD}](https://github.com/user-attachments/assets/b3c9e8a7-6114-41fd-be4c-abd0a6a34799)

# 🔍 Unsupervised Fraud Detection in Bank Transactions using Isolation Forest

This project showcases a full end-to-end machine learning pipeline for **detecting anomalous or potentially fraudulent bank transactions** using **Isolation Forest**, an unsupervised learning algorithm.

It was built entirely on an anonymized transactional dataset and assumes no prior knowledge of which transactions are fraudulent — simulating a real-world scenario where labeled fraud data is unavailable or delayed.

---

## 📌 Project Highlights

- 🧠 **Anomaly Detection without Labels**  
  Using unsupervised ML to flag unusual financial behavior based on transaction patterns.

- 🔧 **Feature Engineering**
  - Transaction amount, account balance, login frequency, time since previous transaction
  - Location, channel, customer type, device & merchant ID (label encoded)

- 📊 **Visualizations**
  - Distribution of anomaly scores
  - Outlier scatter plots (TransactionAmount vs AccountBalance)
  - Top 20 suspicious transactions (bar chart)

- 📈 **Model Used**
  - `IsolationForest` from Scikit-learn
  - Contamination set to 2% to simulate rare anomaly detection

---

## 🧾 Dataset

- **Name**: Bank Transaction Dataset for Fraud Detection  
- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/vala-khosravi/bank-transaction-dataset-for-fraud-detection)  
- **Size**: 2,512 rows × 16 columns  
- **Columns**: Transaction ID, Account ID, Amount, Timestamp, Device, Location, Channel, Customer demographics

---

## 🚀 Technologies Used

- Python 🐍
- Pandas & NumPy for data manipulation
- Scikit-learn for modeling
- Seaborn & Matplotlib for data visualization
- Jupyter Notebook / Kaggle Kernels for development

---

## 📊 Key Visualizations

- Anomaly Score Distribution (KDE + Histogram)
- Colored Scatterplot (TransactionAmount vs AccountBalance)
- Top 20 Most Anomalous Transactions (bar chart)

---

## 💡 Insights

- Isolation Forest successfully identified ~2% of the most unusual patterns.
- These outliers exhibited anomalies in login attempts, transaction amount, and behavior timing.
- Unsupervised methods like this are essential in industries like banking, where real-time decisions must be made before labels are available.



https://www.kaggle.com/code/dilrabonu/bank-trnasaction-dataset-for-fraud-detection
