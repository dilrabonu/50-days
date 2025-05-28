# 🚀 FAANG Preparation Day 13

## 📅 Date: Day 13 – Mock ML System Design, Backtracking, SQL Set Operations

---

### 🎯 Machine Learning – Mock ML System Design Interview (CV + Inference Pipeline)

Today’s focus was on designing an end-to-end Computer Vision (CV) system for real-world use cases like product defect detection on an assembly line.

#### 🔧 System Design Components:
- **Data Collection**: Camera feeds, cloud storage (e.g., S3)
- **Preprocessing**: Resize, Normalize, Augment, Convert (NumPy/TFRecords)
- **Model Training**: Transfer learning (EfficientNet, ResNet), metrics (AUC, accuracy)
- **Validation**: Holdout or stratified k-fold, Grad-CAM for explainability
- **Model Packaging**: Export as `.pt`, `.h5`, ONNX, or TensorRT
- **Inference Pipeline**: FastAPI/Flask backend, Kafka streaming, real-time predictions
- **Monitoring**: Latency tracking, accuracy drift alerts, dashboard via Grafana
- **MLOps**: DVC, MLflow, CI/CD with GitHub Actions

✅ **Goal**: Build robust, scalable, real-time AI pipelines ready for production.

---

### 📘 Data Structures & Algorithms – Backtracking

We explored **backtracking**, a powerful technique for solving constraint-based problems using recursion and pruning.

#### 🔲 Problem 1: N-Queens
- Goal: Place N queens on an N×N board with no two attacking each other.
- Concept: Recursion + constraint validation + backtrack on conflict

#### 🔢 Problem 2: Subsets
- Goal: Generate all possible subsets (power set) from a list of integers
- Idea: Include/exclude element recursively to explore solution space

✅ Backtracking Template:
```python
def backtrack(index, path):
    if base_case:
        result.append(path[:])
        return
    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(next_index, path)
            path.pop()


🧮 SQL – Set Operations: UNION, INTERSECT, EXCEPT
Today we practiced SQL set operators to analyze customer overlaps across different platforms.

Operator	Description
UNION	Combines and removes duplicates
UNION ALL	Combines and keeps duplicates
INTERSECT	Returns only rows that exist in both sets
EXCEPT	Returns rows from first set not in second
