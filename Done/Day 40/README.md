# 🚀 Day 40: Anomaly Detection, Hashing & SQL Consistency – FAANG Prep Series

Welcome to Day 40 of my Machine Learning and FAANG Interview Prep journey!  
This repo covers 3 core technical areas that are crucial for real-world systems and FAANG-level interviews:

- ✅ Machine Learning – Anomaly Detection in Time Series  
- ✅ Data Structures & Algorithms – Hashing & Frequency Maps  
- ✅ SQL – Triggers & Transactions for Automation & Consistency

---

## 📌 1. Machine Learning: Anomaly Detection in Time Series

### 🔍 Overview
Anomaly detection helps identify unusual patterns, outliers, or system failures in sequential data. In production systems, it's essential for monitoring reliability and detecting fraud, outages, or abnormal usage patterns.

### 🛠️ Techniques Implemented
- Z-Score based detection
- Rolling Window statistics (mean, std)
- Isolation Forest for unsupervised detection
- LSTM Autoencoder for sequence anomaly detection
- Prophet + Changepoint Detection

### 📈 Dataset
Simulated time series data for traffic and CPU usage with injected anomalies.

### 📦 Use Cases
- Server CPU spike detection (DevOps)
- Transaction fraud spotting (Finance)
- Logistics delivery failure detection (Supply Chain)

---

## 📌 2. DSA: Hashing & Frequency Maps

### 🧠 Core Problems
1. **Group Anagrams**  
   ➤ Group words that are anagrams using sorted strings or frequency tuples.

2. **Top K Frequent Words**  
   ➤ Extract the most common words from a dataset using heap or counter maps.

### 🧪 Tools
- Python `collections.defaultdict`, `Counter`, `heapq`
- Time/Space complexity analysis included

### 💡 Applications
- Natural Language Processing (TF-IDF, autocomplete)
- Log Analysis & Event Frequency
- Real-time trend tracking (e.g., social media or search queries)

---

## 📌 3. SQL: Triggers & Transactions

### 🔄 Triggers
Automate responses to database events. Includes examples for:
- Audit logs after `UPDATE`
- Auto-maintaining inventory counts after `INSERT/DELETE`

```sql
CREATE TRIGGER log_update
AFTER UPDATE ON orders
FOR EACH ROW
INSERT INTO orders_audit(order_id, changed_at)
VALUES (NEW.id, CURRENT_TIMESTAMP);
🔐 Transactions
Ensure ACID compliance in multi-step operations.

Bank transfer example

E-commerce order + stock sync

Use of BEGIN, COMMIT, ROLLBACK

💼 Real-World Relevance
Ensure data consistency in critical systems

Rollback on partial failures

Maintain audit and compliance logs


✅ Key Takeaways
Time series anomaly detection is essential for monitoring and prediction in real-time systems.

Hash maps (dictionaries) provide constant-time lookup and are critical in solving grouping/counting problems efficiently.

SQL Triggers and Transactions ensure automation, integrity, and rollback capabilities for critical operations.

🧠 Bonus: Interview Insights
Be ready to explain when to use Isolation Forest vs. LSTM in anomaly detection.

Know time complexity trade-offs between heapq and Counter.most_common().

Be able to discuss isolation levels (READ COMMITTED, SERIALIZABLE) and use cases.


