# 🚀 Day 35 – ML Cloud Deployment, Sorting Algorithms, and Real-Time SQL Case Study

Welcome to Day 35 of my **FAANG-level AI/ML Engineering Roadmap**.  
This day focuses on deploying machine learning models to the cloud (GCP), implementing classic sorting algorithms, and solving real-time SQL problems for machine learning case studies.

---

## 📌 Contents

- [💻 Machine Learning – Cloud Deployment (GCP)](#-machine-learning--cloud-deployment-gcp)
- [🧠 Data Structures – Sorting Algorithms](#-data-structures--sorting-algorithms)
- [🧪 SQL – Real-Time ML Case Study](#-sql--real-time-ml-case-study)
- [🧠 FAANG Interview Takeaways](#-faang-interview-takeaways)
- [📂 Project Structure](#-project-structure)
- [🚀 How to Run](#-how-to-run)
- [📫 Connect with Me](#-connect-with-me)

---

## 💻 Machine Learning – Cloud Deployment (GCP)

### ✅ Objective
Deploy a trained ML model (e.g., XGBoost salary predictor) to **Google Cloud Run**, exposing a **REST API endpoint** for real-time inference.

### 🔧 Tech Stack
- Python 3.11
- FastAPI
- Google Cloud Run
- Docker
- joblib, pandas

### 🔁 REST Endpoint Sample
```bash
curl -X POST https://salary-predict.run.app/predict \
  -H "Content-Type: application/json" \
  -d '{"experience": 3, "education": "Masters", "role": "Data Scientist", "location": "Toronto"}'
🧠 Data Structures – Sorting Algorithms
1. Bubble Sort
Compare & swap adjacent elements

Time: O(n²)

Best for: Teaching purposes

2. Insertion Sort
Insert elements into sorted subarray

Time: O(n²), Best: O(n)

Best for: Nearly sorted data

3. Merge Sort
Divide & Conquer algorithm

Time: O(n log n)

Best for: Large datasets, stability guaranteed

All algorithms are implemented in sorting_algorithms.py with clear explanations and time complexities.

🧪 SQL – Real-Time ML Case Study
Scenario: Analyze product return behavior to assist a predictive ML system.

Key Queries:
Return rate in the last 30 days

Top 3 categories with most returns

High-risk users (those with >3 returns)

These queries are written in standard ANSI SQL and included in ml_sql_case_study.sql.


