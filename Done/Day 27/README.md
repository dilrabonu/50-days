# 🚀 Day 27 – How I Built My First CNN | DSA Recap | SQL Anti & Semi Joins

Welcome to **Day 27** of my **50-Day FAANG Preparation Challenge**!  
Today’s work bridges **Computer Vision (CNNs)**, **DSA Mastery Recap**, and advanced **SQL Join Patterns**.  
Every section is built from the ground up – from theory to hands-on practice.

---

## 🧠 Machine Learning – How I Built My First CNN Model

### 🔍 Topic: Convolutional Neural Networks (CNNs) for Image Classification

CNNs are the foundation of deep learning for visual tasks.  
Today, I built my first CNN from scratch using **Keras + TensorFlow**.

### 📚 Key Concepts Covered:
- Convolution Layers (pattern detection)
- Pooling Layers (downsampling)
- Flattening and Fully Connected Layers
- Activation Functions (ReLU, Sigmoid)
- Binary classification setup

### 🧪 Implementation Summary:
```python
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])
📊 Use Case: Classifying images (e.g., cat vs. dog or wildfire detection)
📁 Dataset: Sample Dataset
📈 Result: Achieved good accuracy with basic preprocessing and simple architecture.

📦 Data Structures & Algorithms – Recap & Practice
🔁 DSA Review Topics:
✅ Sliding Window Technique (Kadane’s Algorithm)

✅ HashMap Practice (First Unique Character)

✅ Stack & Queue Patterns (Valid Parentheses)

🔄 Re-attempted LeetCode Problems:
Maximum Subarray (Kadane's Algorithm)

First Unique Character in a String

Valid Parentheses

🎯 Focused on code intuition, edge case handling, and runtime optimization.

🟪 SQL – Anti-Joins & Semi-Joins
🔍 Topic: Users who never ordered (Anti Join) / Users who did (Semi Join)
📊 Tables Used:

Customers

Orders

🧾 Anti Join (Users who NEVER ordered):

SELECT * FROM Customers
WHERE customer_id NOT IN (
  SELECT customer_id FROM Orders
);
✔️ Semi Join (Users who DID order):

SELECT * FROM Customers c
WHERE EXISTS (
  SELECT 1 FROM Orders o WHERE o.customer_id = c.customer_id
);
🛠 Use Cases:

Anti-Join: Find inactive users, unsubscribed members

Semi-Join: Identify engaged users, participants, payers

🧪 Tested in PostgreSQL with sample datasets

✅ Today’s Highlights
Category	Highlight
🧠 ML	Built and trained my first CNN model
🧩 DSA	Reinforced foundational patterns and edge cases
🟪 SQL	Practiced Semi & Anti Joins with real-world scenarios
