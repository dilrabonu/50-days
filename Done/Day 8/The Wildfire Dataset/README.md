https://www.kaggle.com/code/dilrabonu/the-wildfire-dataset


https://www.kaggle.com/datasets/elmadafri/the-wildfire-dataset/data

![image](https://github.com/user-attachments/assets/d54009f8-457b-4ad4-ba6a-e00802a130ad)


# 🔥 AI-Powered Wildfire Detection and Monitoring with Deep Learning

**Capstone Project – Master’s Thesis 2025**  
By [Dilrabo Khidirova](https://www.linkedin.com/in/your-profile) | Task 2 Lead: Model Development & Evaluation

---

## 📌 Project Overview

This project implements a deep learning-based wildfire detection system using RGB aerial imagery. It is a key component of a broader wildfire monitoring pipeline and focuses on designing, training, evaluating, and interpreting machine learning models (CNNs) for binary classification of wildfire presence.

> ✅ This notebook and codebase reflect the practical implementation of **Task 2** in our three-part thesis project:  
> 1. Data Collection & Processing  
> 2. Model Development & Evaluation (**your task**)  
> 3. System Integration & Monitoring Interface

---

## 🎯 Objective

To accurately classify RGB images as `fire` or `nofire` using deep learning while integrating **explainability tools** (Grad-CAM) to visualize model decision-making.

---

## 🧠 Techniques Used

| Component            | Methodology                           |
|----------------------|----------------------------------------|
| 📁 Dataset           | Wildfire Dataset v2 (Kaggle, 2700 images) |
| 🧠 Model             | Transfer Learning with EfficientNetB0  |
| ⚙️ Training          | EarlyStopping + ReduceLROnPlateau      |
| 📊 Evaluation        | Accuracy, Precision, Recall, F1, Confusion Matrix |
| 📈 Visualization     | Grad-CAM for Explainability            |
| 🧪 Augmentation      | Rescaling, flipping, zoom, rotation     |
| 🧾 Documentation     | Markdown cells for reproducibility      |

---

## 🧪 Results

| Metric      | Value   |
|-------------|---------|
| Accuracy    | 61%     |
| Recall (Fire) | 1.00  |
| Precision (Fire) | 0.61 |
| Recall (NoFire) | 0.00 |
| Confusion Matrix | Predicted all as `fire` |

**Interpretation**: The model prioritizes high recall for wildfire detection but misclassifies all `nofire` images. This makes it **safer (no missed fires)** but prone to false alarms. Grad-CAM confirms model attention on bright/hazy sky regions.

---

## 🧠 Explainability with Grad-CAM

Grad-CAM visualizations were used to interpret which regions of an image led to the model's prediction.  
In misclassified `nofire` images, the model focused on cloud or sun glare, which visually resembled smoke or flames.

---

## 🧾 Limitations & Future Work

- ⚠️ NoFire class underfitting due to class imbalance
- 🌈 Similar visual features (haze, clouds) confuse model
- 🔁 Future improvements:
  - Weighted loss function
  - Multispectral or thermal data
  - Use of Vision Transformers or segmentation (U-Net)

---

---

## 👩‍💻 Author

**Dilrabo Khidirova**  
Master’s Student – Data Engineering & AI  
Specializing in Deep Learning & Computer Vision  

