📚 Day 25 – CNN vs RNN | Sets & Duplicates | SQL Pivot & Unpivot

Welcome to Day 25 of my #50DaysOfFAANGPreparation journey!

Today’s topics focus on model selection, hash-based logic, and SQL data reshaping—critical skills for interviews and real-world ML/DS projects.

🔍 Machine Learning: CNN vs RNN

🧠 What’s the Difference?
Feature	CNN (Convolutional Neural Network)	RNN (Recurrent Neural Network)
Input Type	Spatial data (images)	Sequential data (text, time series)
Operation	Convolution + pooling	Memory + recurrence
Parallelism	High (process all pixels at once)	Low (process step by step)
Use Case	Image classification, object detection	Text generation, stock prediction

🖼 Diagram

   CNN:
   Input → Conv → ReLU → Pool → FC → Softmax

   RNN:
   x₀ → h₀ → h₁ → h₂ → ... → hₙ
🛠 Real-World Use Cases:
CNN: Satellite wildfire image classification, facial recognition

RNN: Sentiment analysis on tweets, anomaly detection in heart rate data

🧮 DSA: Sets & Duplicates
✅ Problem 1: Contains Duplicate
Efficient check using a set:

def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
✅ Problem 2: Intersection of Arrays

def intersection(a, b):
    return list(set(a) & set(b))
Why Use Sets?
Fast O(1) lookups

Simple way to remove duplicates

Ideal for FAANG-style array filtering and deduplication tasks

🧾 SQL: Pivoting & Unpivoting
📊 Why It Matters:
Pivot: Converts long-form (tidy) data into wide-form tables for dashboards

Unpivot: Converts wide-form into long format for ML modeling or tidy data

🧱 Example – Pivot Sales Data

SELECT *
FROM (
  SELECT year, quarter, revenue FROM sales
) AS src
PIVOT (
  SUM(revenue)
  FOR quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS pvt;
🔁 Unpivot Example
sql
Copy
Edit
SELECT year, qtr AS quarter, rev AS revenue
FROM sales_wide
UNPIVOT (
  rev FOR qtr IN (Q1, Q2, Q3, Q4)
) AS unp;

🛠 Real-World Use Cases:

Pivot: Dashboard views (e.g., revenue per month)

Unpivot: ML pipelines and normalization tasks

🚀 Summary

Topic	Key Takeaway

CNN vs RNN	Choose model based on data structure (spatial vs temporal)
Set-Based DSA	Use sets for clean, fast deduplication and intersections
SQL Pivoting	Shape data to match use case: wide for reports, long for models

🔁 Practice Challenges
Implement CNN and RNN from scratch or using PyTorch/Keras

Solve: Leetcode 217, 349

Reshape real sales data in SQL: pivot by month, unpivot by product

🧠 Daily Reflection
“Model choice, data shape, and logic structure are three sides of the same coin.”
Understanding when and why to use each of today’s tools will help you solve real-world challenges—not just pass interviews.
