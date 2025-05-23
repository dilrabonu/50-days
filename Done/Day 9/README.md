# 🚀 Day 9 – FAANG Preparation Roadmap

## 📅 Topics Covered:
- **Machine Learning:** Ensemble Learning – Stacking & Voting
- **Data Structures & Algorithms (DSA):** Recursion vs Iteration – Climbing Stairs
- **SQL:** LEFT JOIN & RIGHT JOIN – Orders with Missing Customers

---

## 🧠 Machine Learning – Ensemble Learning (Stacking & Voting)

### ✅ Concepts:
- **Voting Classifier:**
  - Combines predictions of multiple models.
  - Can be hard voting (majority class) or soft voting (average probabilities).
- **Stacking Classifier:**
  - Uses a meta-model to combine base model predictions for improved performance.
  - Powerful in real-world tabular datasets.

### 🔍 Real-World Use Case:
In wildfire detection tasks, stacking CNN models (on satellite imagery) with tabular models (e.g., XGBoost on weather and location data) can significantly improve fire prediction accuracy.




---

## 💻 DSA – Recursion vs Iteration

### 🧩 Problem: Climbing Stairs
Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?

### 📌 Concepts:
- **Recursive Approach:** Elegant but inefficient (O(2^n))
- **Iterative Dynamic Programming Approach:** Memory efficient and fast (O(n))

### ✅ Leetcode Problems:
- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

---

## 🗃️ SQL – LEFT JOIN & RIGHT JOIN

### 🔍 Concepts:
- **LEFT JOIN:** Returns all rows from the left table, even if there are no matches in the right.
- **RIGHT JOIN:** Returns all rows from the right table, even if there are no matches in the left.

### 📌 Real-World Example:
Querying **orders with or without associated customers** (e.g., missing customer info).

### ✅ HackerRank Practice:
- [LEFT JOIN Practice](https://www.hackerrank.com/challenges/earnings-of-employees/problem)
- [RIGHT JOIN Practice](https://www.hackerrank.com/challenges/weather-observation-station-5/problem)

---

## ✅ Summary
| Area | Topic | Practice Resources |
|------|-------|---------------------|
| ML | Stacking + Voting | Wildfire Detection (Kaggle) |
| DSA | Recursion vs Iteration | Leetcode (Climbing Stairs) |
| SQL | LEFT JOIN / RIGHT JOIN | HackerRank Challenges |


LeNet CNN on CIFAR-10 with PyTorch
This project demonstrates the implementation of a Convolutional Neural Network (CNN) based on the LeNet architecture using PyTorch for image classification on the CIFAR-10 dataset. It was completed as part of an advanced machine learning lab task.

📌 Project Objectives
Build a CNN using the LeNet architecture with PyTorch

Train the model on CIFAR-10 (10-class image dataset)

Evaluate performance using accuracy and classification report

Visualize predictions on random test images

📁 Dataset
CIFAR-10:

60,000 color images (32x32 pixels)

10 classes: plane, car, bird, cat, deer, dog, frog, horse, ship, truck

50,000 for training, 10,000 for testing

🔧 Model Architecture (LeNet)
text
Copy
Edit
Input: (3, 32, 32)
→ Conv2D → ReLU → AvgPool2D → (6, 14, 14)
→ Conv2D → ReLU → AvgPool2D → (16, 5, 5)
→ Flatten
→ Linear → ReLU → Linear → ReLU → Linear
→ Output: 10 classes
📊 Results
Test Accuracy: 63.57%

Loss Function: CrossEntropyLoss

Optimizer: Adam (learning rate: 0.001)

Epochs: 10

Batch Size: 64

🔍 Sample Classification Output:
plaintext
Copy
Edit
GroundTruth: cat ship ship plane  
Predicted:   cat car  ship plane
📈 Evaluation Metrics (from sklearn.classification_report)
Macro Avg F1-score: 0.64

Weighted Avg Accuracy: 0.64

Some classes like ship and frog performed better, while cat and dog were more difficult for the model to distinguish.

🧪 How to Run
bash
Copy
Edit
# Install dependencies
pip install torch torchvision matplotlib scikit-learn

# Run notebook in Google Colab or Jupyter
📌 Lessons Learned
LeNet is a good starting point for understanding CNNs but may not generalize well for more complex datasets like CIFAR-10.

Data normalization and architecture tuning are key to improving model performance.

Visualization helped interpret misclassifications and guide future improvements.

📚 Future Work
Try deeper CNNs like VGG16 or ResNet

Use data augmentation techniques (flip, crop, color jitter)

Apply transfer learning using pre-trained models

👩‍💻 Author
Dilrabo Khidirova
Data Science & Machine Learning Student
Passionate about AI for vision and deep learning applications.
