# 🤖 Loan Default Prediction – Automating Bank Credit Processes Using AI

This project applies AI and machine learning to predict whether a customer is likely to default on a loan, enabling banks to make informed and automated credit decisions.

---

## 📊 Problem Statement

Banks often struggle to accurately assess credit risk and loan default probability. This project automates that process by using classification models to predict default based on applicant data.

---

## 🧠 Key Features

- Predicts loan defaults using historical banking data
- Compares multiple ML algorithms (Logistic Regression, Random Forest, XGBoost, etc.)
- Evaluates models via ROC-AUC, F1 score, Precision, and Recall
- Provides explainability with **SHAP** (SHapley Additive exPlanations)
- Visualization of feature importance and model decisions
- End-to-end pipeline from data preprocessing to model interpretation

---

## 🧰 Tech Stack

- **Python**
- **scikit-learn**
- **XGBoost**
- **SHAP**
- **pandas**, **matplotlib**, **seaborn**

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/aimaster-dev/default_loan_prediction.git
cd default_loan_prediction
````

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Notebook**

Open `loan_default_prediction.ipynb` in Jupyter or run it using:

```bash
jupyter notebook loan_default_prediction.ipynb
```

---

## 📈 Model Evaluation

* **Best Model:** XGBoost
* **ROC-AUC:** High discriminative power
* **SHAP Values:** Used to interpret individual predictions and global feature impact

---

## 📌 Highlights

* Automated model selection and tuning
* Transparent credit risk scoring using SHAP
* Business-focused evaluation for banking applications

---

## 📎 Resources

* 📄 [Project Report (PDF)](https://github.com/aimaster-dev/default_loan_prediction/blob/main/Automating_bank_credit_processes_using_AI.pdf)

---

## 📜 License

MIT License. See `LICENSE` for details.

---

## 🙌 Acknowledgments

Thanks to aimaster-dev for sharing this impactful project in AI-driven finance.
