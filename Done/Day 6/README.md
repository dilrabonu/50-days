Day 6:  – ML, DSA, SQL
Welcome to Day 6 of my 50-day FAANG preparation journey. Today's focus areas are:

Machine Learning: Exploring XGBoost, LightGBM, and CatBoost for tabular data.

Data Structures & Algorithms: Understanding Hash Maps and Hash Sets through problems like Two Sum and Group Anagrams.

SQL: Mastering Aliases and the DISTINCT clause for efficient data querying.

📌 Table of Contents
Machine Learning

Overview

Models Implemented

Dataset

Results

Data Structures & Algorithms

Concepts Covered

Problems Solved

SQL

Topics Covered

Queries Executed

Resources

Acknowledgements

Machine Learning
Overview
In this section, I delve into three powerful gradient boosting algorithms:

XGBoost: Known for its speed and performance.

LightGBM: Optimized for efficiency and scalability.

CatBoost: Handles categorical features seamlessly.

These models are benchmarked on a tabular dataset to compare their performance.

Models Implemented
XGBoost: Utilized XGBClassifier with default parameters.

LightGBM: Employed LGBMClassifier, focusing on speed and accuracy.

CatBoost: Implemented CatBoostClassifier with minimal preprocessing.

Dataset
Source: Tabular Playground Series - Feb 2021

Data Structures & Algorithms
Concepts Covered
Hash Maps: Key-value pair data structures allowing O(1) access.

Hash Sets: Collections of unique elements with efficient lookup times.

Problems Solved
Two Sum: Find indices of two numbers that add up to a target.

Group Anagrams: Group words that are anagrams of each other.

Implemented solutions in Python, emphasizing time and space complexity analysis.

SQL
Topics Covered
Aliases: Renaming columns or tables for readability.

DISTINCT: Retrieving unique records from a dataset.

Queries Executed
Count of unique customers by country.

Listing distinct product categories.

Sample Query:

SELECT country AS Country, COUNT(DISTINCT customer_id) AS UniqueCustomers
FROM Customers
GROUP BY country;
Resources
Kaggle Dataset: Tabular Playground Series - Feb 2021

LeetCode Problems:

Two Sum

Group Anagrams

HackerRank SQL Practice:

Revising the Select Query I

Weather Observation Station 5

Acknowledgements
Grateful to the creators of the datasets and problem sets:

Kaggle

LeetCode

HackerRank


