![image](https://github.com/user-attachments/assets/b4415ee3-0d38-456c-ae59-ffaccf6f0ca5)


# 🌿 Cassava Leaf Disease Classification – Deep Learning with TensorFlow/Keras

This project tackles the **Cassava Leaf Disease Classification** Kaggle competition using a professional end-to-end deep learning pipeline built with **TensorFlow/Keras**. The goal is to accurately classify cassava leaf images into one of five disease categories using Convolutional Neural Networks (CNNs).

---

## 📌 Project Overview

- ✅ Built and trained a custom CNN from scratch
- ✅ Used `tf.data` pipelines for efficient image loading and preprocessing
- ✅ Visualized model performance and accuracy curves
- ✅ Prepared for Grad-CAM explainability and EfficientNetB0 transfer learning integration
- ✅ Focused on model interpretability, performance monitoring, and scalable pipelines

---

## 🗃 Dataset Description

- `train.csv`: Contains `image_id` and `label` (numeric class)
- `label_num_to_disease_map.json`: Maps label ID to disease name
- `train_images/`: 21,000+ cassava leaf images
- Task: Classify each image into one of the following:
  1. Cassava Bacterial Blight (CBB)
  2. Cassava Brown Streak Disease (CBSD)
  3. Cassava Green Mottle (CGM)
  4. Cassava Mosaic Disease (CMD)
  5. Healthy

---

## 📊 Model Architecture

### ✅ Custom CNN Model Summary

| Layer | Output Shape | Parameters |
|-------|---------------|------------|
| Conv2D (32) | (222, 222, 32) | 896 |
| MaxPooling2D | (111, 111, 32) | 0 |
| Conv2D (64) | (109, 109, 64) | 18,496 |
| MaxPooling2D | (54, 54, 64) | 0 |
| Conv2D (128) | (52, 52, 128) | 73,856 |
| GlobalAveragePooling2D | (128,) | 0 |
| Dense (128) | (128,) | 16,512 |
| Dense (5 – softmax) | (5,) | 645 |

**Total Trainable Params**: 110,405  
**Validation Accuracy after 10 Epochs**: ~70.8%

---

## 🧪 Training Results

- 📈 **Accuracy Curve** shows consistent improvement
- 🧠 No overfitting observed in initial 10 epochs
- 💡 Model ready for transfer learning enhancement and Grad-CAM interpretability

---
## 🧠 Future Improvements

- 🔁 Add Transfer Learning with `EfficientNetB0` for improved accuracy
- 🔍 Integrate `Grad-CAM` for model explainability
- ⚙️ Implement `EarlyStopping` and `ReduceLROnPlateau` callbacks
- 📦 Experiment with class weighting and data augmentation

---

## 📚 Key Concepts Practiced

- Deep Learning CNNs for image classification
- `tf.data` performance-optimized image pipelines
- Keras model architecture design & training
- Metric tracking and model performance visualization
- Real-world dataset application (agriculture + AI4Good)

---

## 🧠 FAANG Interview Takeaways

- ✅ Use `GlobalAveragePooling2D` over `Flatten()` to reduce overfitting
- ✅ Use `tf.data.prefetch()` to improve GPU throughput
- ✅ Visualize both accuracy and loss curves to monitor training behavior
- ✅ Build explainable models — it’s a key interview and production skill

---

## 🧠 Author

**Dilrabo Khidirova**  
https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/
https://www.kaggle.com/code/dilrabonu/cassava-leaf-disease-classification
