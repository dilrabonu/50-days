# 🚀 Day 14 – FAANG Preparation Series

Welcome to Day 14 of my **50-Day FAANG Preparation Journey**. Today's focus areas:

- 📦 Machine Learning: Mock ML System Design (Computer Vision + Inference Pipeline)
- 🧠 DSA: Sorting Algorithms (Mock Interview + Quiz)
- 🗄️ SQL: Multi-table JOINs Challenge (Interview Style)

---

## 📌 1. Machine Learning – Mock ML System Design (Computer Vision + Inference Pipeline)

### 🎯 Problem
Design a production-grade **image classification system** to detect plant diseases from leaf images.

### 🧱 Architecture Components
1. **Data Ingestion**: Images uploaded from mobile/web, stored in cloud (e.g., AWS S3)
2. **Preprocessing Pipeline**: Resize, normalize, augment
3. **Training**:
   - Model: CNN (EfficientNet / ResNet)
   - Framework: TensorFlow or PyTorch
   - Tracking: MLFlow / Weights & Biases
4. **Model Registry**: Save best models with version control
5. **Inference Pipeline**:
   - Model served via REST API (FastAPI or Flask)
   - Real-time prediction or batch inference
6. **Monitoring**: Track drift, performance, and feedback loop

### ✅ Outcome
Built a scalable pipeline that simulates real-world deployment, considering latency, versioning, and retraining strategy.

---

## 🧠 2. Data Structures & Algorithms – Sorting Algorithms

### 🎯 Topics Covered
- Bubble Sort
- Selection Sort
- Merge Sort
- Quick Sort
- Heap Sort
- TimSort (used in Python)

### 🧪 Mock Interview Practice
```python
arr = [(1, 3), (2, 1), (3, 5)]
sorted_arr = sorted(arr, key=lambda x: x[1], reverse=True)
✅ Insights
Trade-offs between time and space complexity

Stability in sorting algorithms

Choosing the right algorithm based on data context

🗄️ 3. SQL – Multi-table JOINs Challenge
🎯 Problem Statement
Write a query to list customer names and total amount spent in 2024 using JOINs on multiple tables.

🧩 Tables Involved
customers(customer_id, name)

orders(order_id, customer_id, order_date)

order_items(order_id, product_id, quantity, price)

💡 SQL Query

SELECT c.name AS customer_name,
       SUM(oi.quantity * oi.price) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE EXTRACT(YEAR FROM o.order_date) = 2024
GROUP BY c.name
ORDER BY total_spent DESC;
✅ Outcome
Practiced INNER JOINs, aggregations, and multi-table relational logic—essential for data science interviews.

📈 Summary
Day 14 was focused on building real-world ML systems, reinforcing sorting algorithm theory, and solving advanced SQL JOIN problems. These skills are crucial for acing technical interviews at FAANG companies.

🔗 Connect With Me
Follow my 50-day journey on:

💼 LinkedIn https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/


💬 Telegram – Python & AI Tips t.me/DilraboAI
