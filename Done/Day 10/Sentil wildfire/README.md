https://www.kaggle.com/code/dilrabonu/sentinel-wildfire-dataset
# 🔥 Wildfire Detection with Sentinel-2 Satellite Imagery using Deep Learning & Grad-CAM

![banner](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Sentinel-2B_with_open_solar_panel.jpg/800px-Sentinel-2B_with_open_solar_panel.jpg)

## 📌 Project Overview

This project applies deep learning and explainable AI (XAI) techniques to detect wildfire-affected regions using Sentinel-2 MSI multispectral satellite imagery. It includes training a custom CNN model on 6-band GeoTIFF tiles and visualizing class-discriminative regions using **Grad-CAM**.

The model is designed to classify tiles as either:
- **Fire** 🔥
- **No Fire** 🧊

## 🛰️ Dataset

**Source:** [Kaggle - Sentinel-2 MSI Wildfire Data for Research](https://www.kaggle.com/datasets/sentinel-2-msi-wildfire-data-for-research)

- Format: GeoTIFF (512×512 pixels)
- Bands used: 1, 2, 3, 4, 8, 12 (coastal, blue, green, red, NIR, SWIR)
- Classes:
  - `chop_fire/`: 35 images
  - `chop_no_fire/`: 43 images

## 📊 Project Features

- ✅ Load and preprocess multispectral satellite data using `rasterio`
- ✅ Custom PyTorch `Dataset` for GeoTIFF format
- ✅ CNN-based binary classifier (Fire / No Fire)
- ✅ Weighted CrossEntropy loss for class imbalance
- ✅ Grad-CAM implementation for heatmap visualization
- ✅ Image overlay using RGB and NIR/SWIR bands
- ✅ Evaluation: Accuracy, Confusion Matrix, Classification Report

---

## 🧠 Model Architecture

```python
Conv2D(6, 16) ➝ ReLU ➝ MaxPool  
Conv2D(16, 32) ➝ ReLU ➝ MaxPool  
Flatten ➝ Linear ➝ ReLU ➝ Linear(2)
