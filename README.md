#  Breast Cancer Detection Web App

## 📁 Project Overview

This is a user-friendly web application that uses machine learning to predict whether a breast tumor is **benign (not cancerous)** or **malignant (cancerous)** based on key tumor features. It was built using Python and Streamlit for an interactive and accessible user interface.

---

## 🚀 Features

* Predicts breast cancer type using 10 key features
* Simple, intuitive interface built with Streamlit
* Sidebar with interpretation guide for each input
* Instant prediction with positive/negative feedback

---

## 📊 Dataset

**Source**: Breast Cancer Wisconsin Diagnostic Dataset

* 569 samples
* 30 total features (we use the top 10)
* Diagnosis labels: `0 = Malignant`, `1 = Benign`

---

## 💪 Top 10 Features Used

These were selected based on feature importance in Logistic Regression:

1. Worst texture
2. Radius error
3. Worst symmetry
4. Mean concave points
5. Worst radius
6. Worst concavity
7. Worst concave points
8. Worst area
9. Area error
10. Mean concavity

---

##

---

## 🚀 Technologies Used

* Python
* scikit-learn (Logistic Regression, Scaler)
* Streamlit
* Pandas, NumPy
* Pickle (for saving model & scaler)

---

## 📃 Sample Input

```python
[22.5, 1.1, 0.25, 0.145, 22.2, 0.4, 0.36, 880.0, 120.0, 0.3]
```

**Prediction**: Malignant

---

## 💥 Prediction Feedback

* If **benign**: ✅ You're fine! The tumor is not cancerous.
* If **malignant**: ⚠️ Please consult a doctor. The tumor may be cancerous.

---

## 🔍 Feature Interpretation Sidebar

Each input is explained with:

* Min/Max range from dataset
*

---

## 📊 Model Summary

* **Model**: Logistic Regression
* **Target**: Binary classification (0 or 1)
* **Preprocessing**: StandardScaler used for input normalization

---

##

---

##

---

##

---
