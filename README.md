# 🎓 Thesis Project: Predicting University Dropout with Machine Learning

This repository contains the code, data structure, and experimental setup for my MSc thesis:  
**"Beyond Questionnaires: Using Physiological Markers to Enhance Mental Health Predictions."**

## 📌 Abstract

This thesis investigates the use of physiological markers as predictors for mental health conditions such as anxiety and depression. Using the NIMH Healthy Research Volunteer Dataset, we compare the predictive performance of various machine learning models trained on:

- Self-report questionnaire data  
- Physiological markers (e.g., heart rate variability, skin conductance)  
- Combined inputs

The results show that models using physiological data can match or outperform traditional methods, suggesting that biometric signals may enhance mental health screening and intervention strategies.

---

## 🗂 Repository Structure

```plaintext
.
├── data/                       # Data files and processing scripts (excluded in .gitignore)
├── notebooks/                 # Jupyter notebooks with experiments
├── scripts/                   # Python modules (preprocessing, training, evaluation, etc.)
├── results/                   # Model outputs and performance logs
├── configs/
│   └── hyperparameters.yaml   # Tuned hyperparameters for all models
├── main.py                    # Main experiment runner
├── requirements.txt           # Environment dependencies
├── README.md                  # Project overview (this file)
└── .gitignore                 # Files to ignore in Git
⚙️ Models Implemented
Random Forest

Support Vector Machine (SVM)

CatBoost

Artificial Neural Network (ANN)

ANN + SMOTE

ANN + ADASYN

LLM (Zero-shot & Few-shot prompting)

📈 Evaluation Metrics
F1 Score

Accuracy

ROC AUC

Confusion Matrix

Price Quantile Error Analysis

🔧 Getting Started
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/thesis-project.git
cd thesis-project
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the main experiment pipeline:

bash
Copy
Edit
python main.py
🧪 Dependencies
See requirements.txt for full package list. Main libraries include:

scikit-learn

tensorflow

catboost

shap

matplotlib

seaborn

pandas

numpy

📄 License
This project is part of the MSc in Data Science and Society at Tilburg University.
© 2025 Tobias Benavides. All rights reserved.

📬 Contact
Feel free to reach out via LinkedIn or open an issue in this repository.

yaml
Copy
Edit

---

Let me know if you'd like to tailor the tone more formally, or adapt this for Overleaf, GitHub Pages, or an academic CV site.