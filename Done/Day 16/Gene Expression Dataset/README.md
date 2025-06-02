
![{303F9127-0AE6-4E80-8AB5-6EEA34B2E5A7}](https://github.com/user-attachments/assets/61762649-9a31-4a77-975a-8bcdd3dd63c1)

🧬 Gene Expression Classification – Leukemia (ALL vs AML)
This project explores molecular classification of cancer using gene expression data, specifically distinguishing between Acute Lymphoblastic Leukemia (ALL) and Acute Myeloid Leukemia (AML). The dataset is based on the classic Golub et al. study and demonstrates a full ML pipeline for high-dimensional biomedical data analysis.

📁 Dataset
Source: Gene Expression Dataset (Golub et al.)

Samples: 72 leukemia patients

Genes per patient: 7129 gene expression measurements

Labels: ALL or AML for each patient

🎯 Project Goals
🧼 Clean and preprocess high-dimensional genomic data

📉 Apply dimensionality reduction (PCA, t-SNE, UMAP)

🧪 Train classification models (Logistic Regression, SVM)

📊 Evaluate with confusion matrix, precision, recall, and F1-score

🔬 Pipeline Overview
1. Preprocessing
Removed metadata columns (gene descriptions/accession)

Transposed data → samples as rows, genes as columns

Merged expression data with patient labels

Dropped non-numeric rows with noise flags (A, P, etc.)

2. Visualization
Applied three dimensionality reduction techniques to visualize class separability:

PCA	t-SNE	UMAP
		

(Replace with your image links if hosting visualizations)

3. Modeling
Trained:

🔹 Logistic Regression

🔸 Support Vector Machine (Linear Kernel)

Used train_test_split with stratification

Evaluated using:

Confusion matrix

Classification report (Precision, Recall, F1-Score)

⚠️ Results
Metric	Logistic Regression	SVM
Accuracy	~62%	~62%
ALL F1-score	0.73	0.73
AML F1-score	0.40	0.40

⚠️ Note: Low results are due to small dataset (n=36 clean samples) + extreme dimensionality (7129 genes). PCA-based modeling and class weighting recommended for future improvement.

📌 Key Takeaways
Gene expression data is extremely high-dimensional — feature selection or dimensionality reduction is essential.

Class imbalance and small sample sizes severely affect classifier performance.

Visualizing data with t-SNE and UMAP reveals useful cluster structures.


https://www.kaggle.com/code/dilrabonu/gene-expression-dataset
