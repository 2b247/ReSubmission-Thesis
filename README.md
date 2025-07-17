# Where Did the Students Go?  
### A Machine Learning Approach to Student Dropout Prediction

## 🔍 Overview

This repository contains all code, data processing pipelines, and modeling scripts used in the master's thesis titled **“Where Did the Students Go? A Machine Learning Approach to Student Dropout Prediction”** by Tobias Benavides, completed as part of the MSc in Data Science & Society at Tilburg University.

The thesis explores how different machine learning models perform on the task of predicting student dropout from a Portuguese university, with a special focus on the impact of oversampling techniques on imbalanced classification.

## 🎓 Thesis Abstract

University dropout is a phenomenon with far-reaching implications for individuals and societies. This study investigates how machine learning algorithms combined with oversampling methods can improve predictive performance on dropout classification tasks using a real-world educational dataset. Nine model configurations were tested by combining three algorithms—Random Forest, CatBoost, and Artificial Neural Networks (ANN)—with three oversampling settings (None, SMOTE, ADASYN). CatBoost combined with ADASYN yielded the best performance (F1 = 0.9224). The study highlights the importance of selecting appropriate oversampling strategies tailored to specific models.

## 📁 Project Structure

ReSubmission-Thesis/
│
├── data/ # Contains raw and preprocessed datasets
├── models/ # Trained model files (optional if shared)
├── notebooks/ # Jupyter Notebooks with EDA and modeling
├── figures/ # Visuals used in the thesis (e.g., SHAP, PCA)
├── thesis/ # LaTeX source files of the thesis
├── requirements.txt # List of Python packages used
├── FinalVersion.ipynb # Final notebook with full pipeline
└── README.md # You are here


## 🧠 Models Used

- **Random Forest** (via `scikit-learn`)
- **CatBoost** (via `catboost`)
- **Artificial Neural Networks** (via `Keras` and `TensorFlow`)

## ⚖️ Oversampling Techniques

- **SMOTE** (Synthetic Minority Oversampling Technique)
- **ADASYN** (Adaptive Synthetic Sampling)

These were implemented using the `imbalanced-learn` Python package.

## 📊 Key Findings

- CatBoost + ADASYN achieved the best F1 Score (0.9224) and lowest Log Loss (0.2670).
- SMOTE yielded more stable improvements across most models.
- ANN performance degraded under ADASYN, likely due to sensitivity to synthetic noise.
- Oversampling should be selected based on model type—no one-size-fits-all.

## 📌 Dataset

- Source: UCI Machine Learning Repository  
- Name: **Predict Students Dropout and Academic Success**  
- Link: [https://archive.ics.uci.edu/ml/datasets/Predict+Students+Dropout+and+Academic+Success](https://archive.ics.uci.edu/ml/datasets/Predict+Students+Dropout+and+Academic+Success)  
- Size: ~4,424 records (post-cleaning: 3,630 samples)

## 🧪 Evaluation Metrics

- F1-Score (Primary Metric)
- Accuracy
- Precision
- Recall
- ROC-AUC
- Log Loss
- Confusion Matrix
- SHAP Interpretability

## 🔧 Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/2b247/ReSubmission-Thesis.git
cd ReSubmission-Thesis
