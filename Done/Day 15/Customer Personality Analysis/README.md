
# 🧠 Customer Personality Segmentation with KMeans Clustering

This project performs an end-to-end customer segmentation pipeline using unsupervised learning on the [Customer Personality Analysis dataset](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis). The goal is to cluster customers into distinct groups based on their demographics, spending habits, and lifestyle attributes — enabling targeted marketing strategies and deeper customer understanding.

---

## 📌 Objective

To segment customers using **KMeans clustering** and identify meaningful customer personas such as:
- 🏆 Elite Big Spenders
- 💼 High-Income Loyalists
- 🛒 Middle-Class Families
- 🧺 Low-Income Low Spenders

---

## 💼 Business Value

Understanding customer groups allows marketing teams to:
- Run personalized campaigns
- Design product bundles by segment
- Allocate marketing budget based on customer value
- Improve retention and ROI

---

## 🧪 Machine Learning Techniques Used

- **Feature Engineering**: `Age`, `Customer_Tenure`, `Total_Spent`, `Kids`
- **Data Cleaning**: Removed nulls, filtered outliers
- **Encoding**: One-hot encoding for categorical features
- **Scaling**: StandardScaler for normalization
- **Clustering Algorithm**: KMeans
- **Dimensionality Reduction**: PCA for visualization
- **Evaluation**: Elbow Method, visual inspection

---

## 📊 Visualizations

- ✅ Correlation Heatmap
- ✅ Income vs Total Spend (colored by Education)
- ✅ Age vs Total Spend
- ✅ Spending by Marital Status
- ✅ Spending by Number of Kids
- ✅ PCA plot of customer clusters

---

## 📁 Dataset Overview

| Column | Description |
|--------|-------------|
| ID | Unique customer ID |
| Year_Birth | Year of birth |
| Education | Education level |
| Marital_Status | Marital status |
| Income | Annual income |
| Dt_Customer | Customer registration date |
| Kidhome, Teenhome | Number of kids and teens in household |
| MntWines, MntFruits, ... | Amount spent on each product category |
| NumWebPurchases | Online purchases |
| Response | Accepted marketing campaign |

---

## 📈 Results: Cluster Profiles

| Cluster | Income ($) | Total Spend ($) | Age (yrs) | Kids | Segment |
|---------|------------|------------------|-----------|------|---------|
| 0 | 20,306 | 81.8 | 47.5 | 0.7 | Low Income |
| 1 | 58,449 | 761.0 | 60.4 | 1.2 | Premium Loyalist |
| 2 | 76,789 | 1,369.5 | 56.7 | 0.2 | Elite Big Spender |
| 3 | 36,458 | 112.6 | 54.1 | 1.3 | Family-Oriented Shopper |

---

📚 Learnings & Takeaways
Customer data must be cleaned, engineered, and scaled before clustering.

PCA is extremely helpful for interpreting clusters visually.

Clustering isn't just technical — the business value lies in interpreting the output and suggesting actionable insights.

Real-world segmentation is often fuzzy — overlap between segments is expected.
https://www.kaggle.com/code/dilrabonu/customer-personality-analysis-analysis
