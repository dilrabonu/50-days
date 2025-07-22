# 🚀 Day 41 – ML System Design, DSA & SQL: FAANG Interview Prep

Welcome to **Day 41** of my **FAANG Machine Learning Interview Preparation Journey**. This session focused on **designing scalable ML systems**, reviewing **core DSA patterns**, and preparing **SQL system-level schemas** – all within the context of **real-world NLP and Time Series applications**.

---

## 🔧 1. ML System Design – NLP & Time Series

### 📌 NLP System Design: Autocomplete & Search Ranking
- Preprocessing: Tokenization, Lemmatization, Stopword removal
- Embeddings: BERT / TF-IDF + FAISS Vector DB
- Ranking Layer: Learning-to-rank with XGBoost
- Feedback Loop: Online learning from user interaction

✅ **Real-world scenario**: Product search autocomplete at Amazon

### 📌 Time Series System Design: Forecasting & Monitoring
- Data Ingestion: Batch and real-time (e.g., stock API, Kafka)
- Feature Engineering: Lags, rolling stats, Fourier transforms
- Models: Prophet, ARIMA, LSTM, Transformer-based models
- Serving: Batch + Stream inference pipelines
- Monitoring: Drift detection, anomaly alerting

✅ **Real-world scenario**: Google stock price forecasting system

---

## 🧠 2. DSA Mock Interview Questions – Recap

### Key Topics Covered:
- Hashing: `Group Anagrams`, `Top K Frequent`
- Heaps & Queues: Streaming frequency tasks
- Two Pointers: `Merge Intervals`, `Sliding Window`
- Graphs: `Word Ladder`, BFS/DFS
- Dynamic Programming: `Longest Palindromic Substring`

✅ **Mock Challenges Solved**:
- Design a real-time autocomplete engine
- Find anomalies in sensor stream using Z-Score
- Rank user search queries using embeddings

---

## 🗄️ 3. SQL System Design for ML Pipelines

### 📌 Schema Design:
- `experiments`: Track training experiments
- `models`: Store versioned model metadata
- `predictions`: Log model outputs and confidence
- `metrics`: Centralized evaluation metrics
- `datasets`: Ingestion sources and metadata

### 📌 Access Control:
| Role         | Access                                  |
|--------------|------------------------------------------|
| Data Engineer | Full access to data pipelines            |
| ML Engineer   | Full access to models & predictions      |
| Analyst       | Read-only access to metrics & logs       |
| Admin         | Manage all roles and audit trails        |

✅ Designed with **enterprise-grade auditability & collaboration** in mind.

---

## 🎯 Outcomes

- Practiced **real-world ML system design** thinking for interviews
- Reviewed and solved **DSA questions across patterns**
- Created a **secure and scalable SQL schema** for ML lifecycle tracking
- Prepared to **answer system design questions** with latency, accuracy, and monitoring trade-offs

---

## 📚 Next Steps

- Simulate mock system design interviews (verbal & diagram-based)
- Extend this into a deployable Streamlit prototype (e.g., Search Ranker or Time Series Dashboard)
- Prepare a professional architecture diagram (Lucidchart / draw.io)

---

## 🔗 Connect

If you're also preparing for FAANG or want to collaborate on AI/ML projects, feel free to connect with me on https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/


