# 🧠 LFW Face Recognition using CNN (TensorFlow & PyTorch)

This project performs face recognition using Convolutional Neural Networks (CNNs) on the **Labeled Faces in the Wild (LFW)** dataset. We trained and evaluated models using both **TensorFlow** and **PyTorch** to compare performance on the same dataset.

---

## 📁 Dataset: Labeled Faces in the Wild (LFW)

- ✅ **13,000+ images** of faces collected from the web.
- ✅ 5,749 unique people (each folder is one class).
- ✅ Preprocessed using `lfw-funneled.tgz`.
- ✅ Used only identities with **2+ images** for reliable training.

---

## 🧠 Objectives

- Build a CNN-based face classification model.
- Train and compare **TensorFlow** and **PyTorch** implementations.
- Visualize accuracy and loss curves.
- Evaluate prediction performance.
- Prepare for embedding extraction and face matching (Step 9).

---

## 📦 Models Used

| Framework   | Model          | Notes                          |
|-------------|----------------|--------------------------------|
| TensorFlow  | Custom CNN     | Trained with ImageDataGenerator (split 80/20) |
| PyTorch     | Custom CNN     | Manual training & validation loop |

---

## 🧪 Results

| Metric           | TensorFlow ✅ | PyTorch 🔸  |
|------------------|--------------|-------------|
| Epochs           | 15           | 10          |
| Final Accuracy   | **25.28%**   | 7.86%       |
| Val Classes      | 1680         | 1680        |
| Total Images     | 13,233       | 13,233      |

✅ TensorFlow model outperformed in both **accuracy** and **training stability**.

---

## 📊 Visualizations
![{95E31449-E7EA-4B37-B09E-D2E7D180ACA4}](https://github.com/user-attachments/assets/c6e14c9a-0240-409b-871f-eddc793092fe)


### ✅ TensorFlow Accuracy Plot

- Validation accuracy improved from 8% → **25%** across 15 epochs.
- Clear learning trend without overfitting.

### 🔸 PyTorch Accuracy Plot

- Accuracy rose from 4% → **8%**.
- Model struggled with high class imbalance and limited data per class.

---

## 🧰 Tools & Frameworks

- Python 🐍
- TensorFlow/Keras
- PyTorch
- OpenCV
- Matplotlib, NumPy
- Google Kaggle GPU Notebook


---

## 🔥 Author & Acknowledgments

**Author:** [Dilrabo Khidirova] https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/
**Special Thanks:** Kaggle Datasets, LFW dataset creators, and the AI/ML learning community!

---

## 📌 Usage

Clone this repo, open the notebook in https://www.kaggle.com/datasets/atulanandjha/lfwpeople/code, and run the cells in order to:

1. Load & preprocess the data
2. Train CNN using TensorFlow or PyTorch
3. Evaluate & visualize performance
4. Extend with embedding extraction & matching



