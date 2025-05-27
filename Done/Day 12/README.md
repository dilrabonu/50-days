# 📦 Day 12 – Modular Deep Learning Project + FAANG DSA + SQL Subqueries

Welcome to Day 12 of my **FAANG Preparation Roadmap**!  
Today’s focus is on building a modular Machine Learning project with professional GitHub structure, mastering a classic FAANG-style DSA problem (Search in Rotated Array), and practicing SQL subqueries with real-world applications.

---

## 🔗 Machine Learning: Modular GitHub Project Structure



![image](https://github.com/user-attachments/assets/7b71b400-ea21-48a0-8999-75a986c5a236)



### 📈 Techniques Used
- Transfer Learning (EfficientNetB0, ResNet50)
- Data Augmentation with `Albumentations`
- Model Evaluation: Accuracy, Confusion Matrix, Grad-CAM

---

## 🧪 DSA: Search in Rotated Sorted Array

### 🎯 Problem
Search an element in a rotated sorted array in **O(log n)** time.

### ✅ Why It Matters
A common **FAANG interview** question testing binary search, edge case handling, and logical reasoning.

### 🧩 Python Implementation
```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
