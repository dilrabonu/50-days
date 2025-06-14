Day 23 – Sentiment Analysis (TF-IDF + RNNs) | Queues (DSA) | SQL Date Functions

Welcome to Day 23 of my 50-day FAANG preparation challenge!

Today, I explored a complete mix of Machine Learning, Data Structures & Algorithms, and SQL, with a focus on real-world applications and FAANG-style problem-solving.

🧠 Machine Learning: Sentiment Analysis (TF-IDF + RNNs)
Goal: Build models to classify text (e.g., movie reviews) as positive or negative.

📌 Techniques Used:
TF-IDF + Logistic Regression – baseline classical ML

Recurrent Neural Networks (RNNs) – sequential deep learning for text

Word Embeddings – represent words in dense vectors

Sentiment Evaluation – Accuracy, Precision, Recall, F1-score

🛠️ Tools:
scikit-learn for TF-IDF & Logistic Regression

PyTorch for RNN implementation

📊 Real-World Use Cases:
Customer review analysis (e.g., Amazon, Yelp)

Social media sentiment mining (e.g., Twitter)

Brand monitoring and support automation

🧮 Data Structures: Queue (FIFO), Implement Queue using Stack
Goal: Understand and implement Queue data structure and simulate it using two stacks.

🔁 Topics Covered:
FIFO logic using collections.deque

Implementation of queue via 2 stacks (popular interview question)

Use Cases: Scheduling, Graph BFS, OS task queue

python
Copy
Edit
class MyQueue:
    def __init__(self):
        self.stack_in, self.stack_out = [], []

    def enqueue(self, x):
        self.stack_in.append(x)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
🧮 SQL: Date Functions
Goal: Analyze temporal user data using date-based SQL functions.

🔍 Functions Learned:
DATE_PART() – extract year, month, day, etc.

DATE_DIFF() – compute duration between two dates

FORMAT() – format date for presentation in dashboards or reports

💡 Example:
sql
Copy
Edit
SELECT 
  DATE_PART('year', signup_date) AS signup_year,
  DATE_DIFF('day', signup_date, last_login) AS days_active,
  FORMAT(signup_date, 'MM/dd/yyyy') AS formatted_date
FROM users;
✅ Summary
Area	Topic	Tool/Concept
ML	Sentiment Analysis	TF-IDF, RNN (PyTorch)
DSA	Queue	Stack-to-Queue Conversion
SQL	Date Analysis	DATE_PART, DATE_DIFF, FORMAT


🔮 What’s Next?
Tomorrow I’ll explore:

ML: Text Classification with Transformers (BERT)

DSA: Trees – Traversals & Path Sum

SQL: Window Functions (LAG, LEAD)

