# 🚀 Day 11 – FAANG Preparation Roadmap

## 🧠 Machine Learning: Bias-Variance, Overfitting & Cross-Validation

### 🔍 Bias-Variance Tradeoff
- **Bias**: Error from overly simplistic assumptions (underfitting).
- **Variance**: Error from high sensitivity to training data (overfitting).
- **Goal**: Achieve low bias and low variance for optimal generalization.

### 🔥 Overfitting
Occurs when a model learns noise in the training data, leading to poor performance on unseen data.

**Solutions to Overfitting:**
- Regularization (L1, L2)
- Pruning (for trees)
- Cross-validation
- Early stopping
- Simplify the model

### 🔁 Cross-Validation
A technique to evaluate model generalization.

**K-Fold Cross-Validation:**
- Split the dataset into `k` parts.
- Train the model on `k-1` parts and validate on the remaining part.
- Average the performance across all `k` runs.

**Variants:**
- Stratified K-Fold: Maintains class proportions (for classification tasks).
- Leave-One-Out CV: Special case of K-Fold with `k = n`.

---

## 📘 Data Structures & Algorithms: Binary Search Variants

### 1️⃣ Find Peak Element
Binary search approach to locate an element greater than its neighbors.

```python
def findPeak(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

2️⃣ First/Last Position in Sorted Array
Locate the first or last occurrence of a target in a sorted list.


def findFirst(nums, target):
    left, right, result = 0, len(nums) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1  # search left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
