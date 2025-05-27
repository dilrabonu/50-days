# 🔥 Wildfire Detection Using EfficientNetB0 (Transfer Learning)

Detect wildfires from satellite images using deep learning and transfer learning with EfficientNetB0.  
This project is based on a real-world wildfire dataset and achieves **98% validation accuracy**.

---

## 📌 Project Overview

**Goal**: Automatically classify images into:
- 🔥 Fire
- 🌿 No Fire

**Use Case**: Early wildfire detection for environmental safety, disaster prevention, and alert systems.

---

## 🧠 Model Highlights

| Model            | Train Accuracy | Val Accuracy | Params     |
|------------------|----------------|--------------|------------|
| Custom CNN       | 83.6%          | 88.5%        | 11.9M      |
| EfficientNetB0 ✅ | **99.2%**      | **97.5%**    | 4.85M (frozen) |

We used **Transfer Learning** with EfficientNetB0 pretrained on ImageNet for efficient and accurate classification.

---

## 📁 Dataset

- Source: Kaggle – Wildfire Detection Image Data
- Size: 1900 images
- Format: Image folders with class labels (`Fire`, `No Fire`)
- Train/Validation Split: 80/20

---

## 🔧 Workflow Summary

1. **📦 Data Loading & Visualization**  
   Load 5 sample images from each class using TensorFlow `image_dataset_from_directory`.

2. **🧼 Preprocessing**  
   Resize to 224×224, shuffle, batch, and normalize.

3. **🔨 Modeling**  
   - Built a custom CNN (for baseline comparison)
   - Loaded EfficientNetB0 via `keras.applications`
   - Replaced top layers with GlobalAvgPool → Dropout → Dense(1, sigmoid)

4. **📈 Training**  
   Trained EfficientNetB0 for 10 epochs on ~1.4k training images.

5. **✅ Evaluation**  
   - Final Accuracy: **98%**
   - Precision/Recall/F1 all >95%
   - Confusion matrix shows only 9 misclassifications (1 false positive, 8 false negatives)

6. **📊 Visualization**  
   - Plotted training/validation accuracy and loss
   - Displayed confusion matrix + classification report

---

## 📊 Final Evaluation

### 🧾 Classification Report

| Class     | Precision | Recall | F1-Score |
|-----------|-----------|--------|----------|
| Fire      | 0.95      | 0.99   | 0.97     |
| No Fire   | 0.99      | 0.96   | 0.98     |
| Accuracy  |           |        | **0.98** |

### 📉 Confusion Matrix



![image](https://github.com/user-attachments/assets/2c0170a9-d98f-4aee-823f-1e3dde89d01c)



---

## 💡 Key Learnings

- Transfer learning drastically boosts performance on small datasets
- EfficientNetB0 generalizes well and is fast to train
- Visualization is essential to trust model decisions

---

## 🧠 Future Improvements

- Try Grad-CAM for model explainability
- Train on higher-resolution images (384x384)
- Deploy via Streamlit or Hugging Face Spaces
- Integrate with real-time drone or satellite image streams

**Author**: Dilrabo Khidirova  
- 🎓 Master's in Software Engineering (AI & Data Science focus)  
- 💼 Passionate about building AI-powered real-world systems
https://www.kaggle.com/code/dilrabonu/wildfire-dataset-12
