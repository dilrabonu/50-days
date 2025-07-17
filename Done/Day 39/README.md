# 📅 Day 39: ML | DSA | SQL - FAANG Prep Journey

Welcome to **Day 37** of my 50-day FAANG-focused Machine Learning & Data Science preparation series. This day was dedicated to mastering **Deep Learning for Time Series (LSTM)**, **Heap-based Top-K Problems**, and **Modular SQL Design using Stored Procedures & Functions**.

---

## 🧠 Themes Covered

### 1️⃣ Deep Learning for Time Series Forecasting – **LSTM**

**Goal:** Use LSTM to capture long-term dependencies in sequential/time-based data.

- ✅ Learned the internals of LSTM (gates, memory cells)
- ✅ Built an LSTM-based time series forecasting pipeline
- ✅ Compared LSTM to classical methods (ARIMA, Prophet)

**Real-World Use Cases:**
- Energy demand forecasting
- Stock price prediction
- Sensor data monitoring in IoT

📌 *Why LSTM?* Handles long-term memory and nonlinear trends better than traditional models.

---

### 2️⃣ Data Structures – **Heap & Priority Queue**

**Key Problems Practiced:**
- 🔹 Kth Largest Element in an Array
- 🔹 Top K Frequent Elements
- 🔹 Merge K Sorted Lists (bonus)

**Techniques:**
- Min-Heap for Top-K elements
- Max-Heap for frequency sorting
- Priority Queue API in Python (`heapq`)

**Time Complexity Insight:**
- O(n log k) solutions using heaps for streaming problems

📌 *Why Heaps?* Efficient access to min/max elements in dynamic datasets.

---

### 3️⃣ SQL – **Stored Procedures & Functions**

**Focus:** Designing modular, secure, and reusable SQL code

- ✅ Created stored procedures for reporting logic
- ✅ Defined SQL functions for reusable business rules
- ✅ Used control flow (`IF`, `CASE`, `LOOP`) inside procedures

**Use Cases:**
- Logistics: Dynamic cost calculation
- ETL Pipelines: Batch data cleaning
- Reporting Systems: Scheduled, reusable computations

📌 *Why Stored Procs?* Performance boost, security, and consistency across systems.

---

## 📌 Key Takeaways

| Topic           | What I Learned                                              | Why It Matters in FAANG Interviews                                 |
|----------------|-------------------------------------------------------------|---------------------------------------------------------------------|
| LSTM            | Memory-enhanced RNN for sequence modeling                  | Expected in ML system design for forecasting & voice assistants     |
| Heap/PriorityQ  | Efficiently solve top-k and stream-based selection problems | Appears in almost all DSA interviews (Amazon, Google, Netflix)     |
| SQL Procedures  | Design reusable and optimized logic inside the database     | Crucial for backend-heavy roles and data-driven enterprise systems |

---

## 🧪 Next Steps

- Tune LSTM with multiple features and hyperparameters
- Implement max-heap with custom comparators
- Create a mini-project using SQL procedures + Python integration

