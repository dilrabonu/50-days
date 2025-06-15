 Day 24 – Attention, Transformers, HashMaps, and SQL Regex | FAANG Prep Roadmap
Welcome to Day 24 of my 50-Day FAANG Preparation Journey. Today’s focus includes foundational and advanced concepts across Machine Learning, Data Structures & Algorithms, and SQL, preparing me for real-world AI applications and FAANG-style interviews.

📌 Topics Covered
Category	Topic
ML	Attention Mechanism, Transformers, BERT, HuggingFace
DSA	HashMap / Dictionary – First Unique Character, Isomorphic Strings
SQL	REGEX – Extracting emails and hashtags from text columns

🧠 Machine Learning – Attention & Transformers (BERT Intro)
🔷 What I Learned
Attention Mechanism: Helps models focus on relevant input parts, critical for sequence modeling.

Transformers: Parallelized deep learning architecture built on self-attention, used in NLP models like BERT.

BERT: Bidirectional Transformer pretrained on massive corpora, excels at downstream NLP tasks.

HuggingFace Transformers: Open-source library to easily use, fine-tune, and deploy transformer models.

🔨 Hands-on Project
python
Copy
Edit
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
print(classifier("This roadmap makes me confident for FAANG!"))
📚 Real-World Use Cases
Customer support chatbots

Resume parsing and classification

Text summarization for news and legal docs

💡 Data Structures – HashMap / Dictionary
🧩 Concepts Practiced
First Unique Character in a String

Isomorphic Strings – Check character pattern mapping between two strings

🧪 Sample Code
python
Copy
Edit
def firstUniqChar(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1
🛠 Why HashMap?
O(1) lookup and insertion

Essential for counting, mapping, and state tracking in strings

🧮 SQL – Regex in SQL (Emails & Hashtags)
📍 Topics:
Pattern-based extraction in SQL using REGEXP_EXTRACT and REGEXP_CONTAINS

Supported in PostgreSQL, Google BigQuery, Snowflake

🔧 Examples
Extracting Emails:

sql
Copy
Edit
SELECT text_column
FROM users
WHERE text_column ~* '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
Extracting Hashtags:

sql
Copy
Edit
SELECT REGEXP_EXTRACT(comment, r'#\w+') AS hashtag
FROM social_comments
💼 FAANG-Style Questions & Answers
Q: Why are Transformers better than RNNs for NLP tasks?
✅ Parallel processing, long-range dependencies, and context-rich attention layers.

Q: What data structure helps optimize string frequency problems?
✅ HashMap (Python Dictionary) provides constant time frequency tracking.

Q: Why is REGEX preferred in SQL for text extraction?
✅ It allows precise pattern-based filtering when LIKE is insufficient.

✅ Daily Takeaways
📘 I understood the core intuition behind Transformers and Attention, and why BERT outperforms traditional models.

🧩 Practiced two classic HashMap-based interview problems on LeetCode.

🧪 Used REGEX in SQL to extract structured patterns, critical for cleaning and mining textual data.


