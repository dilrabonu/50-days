
![{017B3C68-4561-41BC-8B43-9A60420C5371}](https://github.com/user-attachments/assets/0c6e18b2-d1b1-41e5-bd06-9fdfb5cce4cb)


# 🧠 Chest X-Ray Pneumonia Detection with TensorFlow vs PyTorch

A complete machine learning project comparing the implementation, training behavior, and evaluation performance of **TensorFlow** and **PyTorch** models on a real-world medical imaging dataset — **Chest X-ray Images (Pneumonia)** from Kaggle.

---

## 📂 Dataset

- **Source:** [Kaggle - Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- **Size:** 5,863 chest X-ray images (JPEG)
- **Classes:**
  - `NORMAL`: Healthy lungs
  - `PNEUMONIA`: Infected lungs

Dataset is structured into:
/train
/test
/val

yaml
Copy
Edit

---

## 🎯 Project Objectives

- Build a binary image classifier to detect pneumonia from chest X-rays
- Implement the **same CNN architecture** in both TensorFlow and PyTorch
- Evaluate training time, convergence, and accuracy
- Visualize and compare learning curves
- Optimize memory usage in Kaggle environment

---

## 🧰 Tools & Frameworks

| Framework   | Version   |
|-------------|-----------|
| TensorFlow  | 2.x       |
| PyTorch     | 2.x       |
| Python      | 3.11      |
| Kaggle GPU  | T4 (with ~16GB RAM) |

---

## 🏗️ Model Architecture (Same in TF & PT)

Conv2D(16, (3,3)) → ReLU → MaxPooling2D(2,2)
→ Flatten → Dense(64) → ReLU
→ Dense(1) → Sigmoid

yaml
Copy
Edit

---

## ✅ Training Results

| Metric           | TensorFlow                         | PyTorch                            |
|------------------|-------------------------------------|------------------------------------|
| Final Val Accuracy | **0.9895**                        | ~0.89 (estimated)                  |
| Final Test Accuracy | ✅ Noted below                   | ✅ **0.7228**                       |
| Training Duration | ~2–3 min                          | ~2–3 min (efficient with DataLoader) |
| Model Saved As    | `chest_xray_tf_model.h5`          | `chest_xray_pt_model.pth`          |

---

## 📊 Training Loss Comparison Plot

![Loss Comparison](loss_comparison.png)

- TensorFlow shows steeper convergence and lower final validation loss
- PyTorch shows stable decrease but lower test accuracy (requires tuning)

---

## 🧪 Evaluation (Test Set)

```text
TensorFlow Test Accuracy: ~0.98+
PyTorch Test Accuracy:    0.7228
💾 Model Saving
✅ TensorFlow:

python
Copy
Edit
model_tf.save("/kaggle/working/chest_xray_tf_model.h5")
✅ PyTorch:

python
Copy
Edit
torch.save(model_pt.state_dict(), "/kaggle/working/chest_xray_pt_model.pth")
💡 Key Takeaways
TensorFlow is faster for prototyping and integrates well with deployment tools.

PyTorch gives more flexibility in training loops and memory control.

Loading full datasets in memory can cause kernel crashes — use DataLoader.

Training on medical data requires careful tuning, augmentation, and metrics beyond accuracy (e.g., recall, AUC).


👩‍💻 Author
Dilrabo Khidirova
AI & Machine Learning Engineer | Master’s Student
🔗 LinkedIn https://www.linkedin.com/in/dilrabo-khidirova-3144b8244/
 | Telegram Channel https://t.me/DilraboAICh


https://www.kaggle.com/code/dilrabonu/chest-x-ray-images
