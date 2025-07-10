 🚀 Day 36 – NLP Embeddings, Recursion, and SQL Views | FAANG Prep

Welcome to **Day 36** of my 50-day FAANG Machine Learning & DSA prep journey. Today, I focused on three core areas:
1. Natural Language Processing (Text Preprocessing & Embeddings)
2. Data Structures & Algorithms (Recursion & Backtracking)
3. SQL Concepts (Views vs Materialized Views)

---

## 📘 NLP – Text Preprocessing & Word Embeddings

### 🔹 Key Topics Covered:
- Text Cleaning & Tokenization
- Stopword Removal, Lemmatization
- TF-IDF Vectorization
- Word2Vec Embeddings (CBOW & Skip-Gram)
- BERT Contextual Embeddings using Transformers

### ✅ Libraries Used:
- `NLTK`, `Scikit-learn`
- `Gensim` for Word2Vec
- `Transformers` from HuggingFace

### 🧠 Learnings:
- Difference between sparse (TF-IDF) and dense (Word2Vec/BERT) representations
- Contextualized vs static embeddings
- Practical embedding extraction using BERT for downstream tasks

---

## 🧮 DSA – Recursion & Backtracking

### 🔹 Topics Practiced:
- Basic recursion (factorial, fibonacci)
- Memoization for optimization
- Intro to Backtracking with Subsets & Combinatorics

### ✅ Code Examples:
- `factorial_recursive.py`
- `fibonacci_memoized.py`
- `backtracking_subsets.py`

### 💡 Key Concepts:
- Recursive base case and recursive case
- Stack memory & call tracing
- Pruning recursion trees for efficiency in backtracking

📌 *Backtracking visualized via recursion trees helped reinforce tree traversal and DFS logic – key in interviews!*

---

## 🗃️ SQL – Views vs Materialized Views

### 🔹 What I Explored:
- **Views**: Virtual logical layers on top of base tables
- **Materialized Views**: Physically stored query results with refresh options

### ✅ SQL Files:
- `create_view.sql`
- `create_materialized_view.sql`

### 📊 Use Cases:
- Views: Logical abstraction for cleaner queries & access control
- Materialized Views: Speed up frequent read-heavy queries (e.g., BI dashboards)

---

## 📌 FAANG-Style Questions Practiced:

- How does BERT handle context compared to Word2Vec?
- Why is recursion less efficient in naïve Fibonacci and how do you optimize it?
- When would you use a materialized view over a regular view in a large-scale reporting system?

---

## 🛠️ Tech Stack

- Python 3.10+
- Transformers (HuggingFace)
- Gensim
- scikit-learn
- SQLite / PostgreSQL

---

## 📈 Outcomes

- Built a deeper intuition for text vectorization methods and their real-world applications
- Strengthened recursive problem-solving patterns used in FAANG coding rounds
- Understood SQL optimization strategies with abstraction layers (views)

