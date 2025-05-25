Day 10 – AutoML, Sorting Algorithms, SQL Joins

📌 ML – AutoML Frameworks (H2O, AutoSklearn)

Automated Machine Learning (AutoML) simplifies the process of training and optimizing models.

Key Tools:

H2O AutoML: Supports deep learning, XGBoost, GLM, Random Forest, stacked ensembles.

AutoSklearn: Builds pipelines using scikit-learn and Bayesian optimization.

Use Case: Predict customer churn with zero manual model tuning.

import h2o
from h2o.automl import H2OAutoML

h2o.init()

data = h2o.import_file("customer_churn.csv")

train, test = data.split_frame(ratios=[.8])

aml = H2OAutoML(max_models=20, seed=1)

aml.train(y="churn", training_frame=train)


📌 DSA – Sorting Algorithms
Understand how different sorting algorithms work and their trade-offs.

Algorithm	Time Complexity	Best Use
Bubble Sort	O(n²)	Teaching, very small data
Selection Sort	O(n²)	Finding min/max repeatedly
Merge Sort	O(n log n)	Stable, large data sorting

Real-world example: Merge Sort is used in external sorting (e.g., when sorting large files on disk).

🔗 LeetCode Practice:

Sort Colors

Merge Intervals


📌 SQL – FULL OUTER JOIN & SELF JOIN
✅ FULL OUTER JOIN
Returns all matched and unmatched rows from both tables.

sql
Copy
Edit
SELECT a.id, a.name, b.salary
FROM employees_a a
FULL OUTER JOIN employees_b b ON a.id = b.id;
✅ SELF JOIN
Used to create employee–manager relationships from the same table.

sql
Copy
Edit
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
🔗 HackerRank Practice:

Employees earning more than their managers

The PADS (JOIN practice)


