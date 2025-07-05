# 📱 Day 33 – Predicting User Engagement | Linked List II | SQL A/B Testing

Welcome to **Day 33** of my 50-day FAANG Preparation Journey!  
This project showcases how to **design a Machine Learning system to predict user engagement**, implement **Linked List interview problems**, and **analyze A/B Testing metrics in SQL**.

---

## 🔮 Project 1: Machine Learning System Design – Predicting User Engagement

### 🧠 Objective
Design a scalable ML system that predicts **if a user will like or comment** on a mobile app post within 10 minutes of viewing.

### 🛠️ System Components
- **Feature Store**: Stores user, post, and context features
- **Model**: Trained using `XGBoost` and `Logistic Regression`
- **Inference Pipeline**: Serves predictions in real-time via API
- **Monitoring**: AUC, Precision@k, and Data Drift Monitoring

### 📊 Features Used
- `User`: Age, location, past engagement
- `Post`: Topic, media type, hashtags
- `Context`: Time of day, device, network quality

### 🧪 Output
- Binary: `Engaged` (Yes/No)
- Probability: `P(Engagement)`

---

## 👨‍💻 Project 2: DSA – Linked List II Problems

### 🔁 1. Detect Cycle in Linked List
- Detects loops to avoid infinite processing
- Implemented using Floyd’s Tortoise and Hare algorithm

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
🔀 2. Merge Two Sorted Linked Lists
Efficiently merges two sorted lists into a new sorted list

Common in feed ranking and log merging systems

def mergeTwoLists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
🧪 Project 3: SQL – A/B Testing Metrics
🧠 Goal
Compare control and variant user groups in an A/B test for a mobile app UI.

📂 Sample Table: ab_test_results
user_id	group	clicked	session_time
1	control	1	300
2	variant	0	180

📊 SQL Query

SELECT
  group,
  COUNT(*) AS total_users,
  SUM(clicked) AS total_clicks,
  AVG(clicked) AS conversion_rate,
  AVG(session_time) AS avg_session_time
FROM ab_test_results
GROUP BY group;
📈 Metrics Compared
Conversion Rate

Average Session Time

Click-through Rate (CTR)

💼 Real-World Applications
Module	Application
ML System Design	Feed ranking, notification optimization
DSA Linked List	Recommender integrity, data pipeline sorting
SQL A/B Testing	Product experiments, UI testing decisions
