# Health-Care-Premium-Prediction-app
# 🏥 Health Insurance Premium Prediction App

A machine learning-powered web application that predicts an individual's health insurance premium based on demographic, lifestyle, medical, and financial factors. The application is built using **Python**, **Scikit-learn**, and **Streamlit**, and employs a segmented modeling approach to improve prediction accuracy across different age groups.

---

## 📌 Project Overview

Health insurance premiums are influenced by several factors such as age, income, medical history, lifestyle choices, and genetic risk. This project develops an end-to-end machine learning solution that predicts health insurance premiums using historical insurance data.

To improve prediction performance, the population was segmented into two groups:

* **Young Individuals (≤ 25 years)**
* **General Population (> 25 years)**

Separate machine learning models were trained for each segment, allowing the application to capture age-specific premium patterns more effectively.

---

## 🚀 Live Application Features

The Streamlit application allows users to:

✅ Enter demographic information
✅ Provide lifestyle and medical history details
✅ Specify insurance plan preferences
✅ Calculate normalized medical risk scores
✅ Predict insurance premium instantly
✅ Reset inputs dynamically

---

## 🛠️ Technology Stack

| Category              | Technologies          |
| --------------------- | --------------------- |
| Programming Language  | Python                |
| Frontend              | Streamlit             |
| Data Analysis         | Pandas, NumPy         |
| Visualization         | Matplotlib, Seaborn   |
| Machine Learning      | Scikit-learn, XGBoost |
| Model Serialization   | Joblib                |
| Hyperparameter Tuning | RandomizedSearchCV    |

---

## 📊 Input Features

The model predicts premiums using the following features:

### Numerical Features

* Age
* Income (Lakhs)
* Number of Dependents
* Genetic Risk Score

### Categorical Features

* Gender
* Region
* Marital Status
* BMI Category
* Smoking Status
* Employment Status
* Insurance Plan
* Medical History

---

## 🧠 Feature Engineering

Several feature engineering techniques were applied:

* Missing value treatment
* Duplicate removal
* One-hot encoding
* Label encoding for insurance plans
* Feature scaling using MinMaxScaler
* Medical risk normalization
* Feature selection and reduction

### Medical Risk Score Calculation

A custom normalized medical risk score was created based on combinations of diseases:

| Disease             | Risk Score |
| ------------------- | ---------- |
| Diabetes            | 6          |
| High Blood Pressure | 6          |
| Heart Disease       | 8          |
| Thyroid             | 5          |
| No Disease          | 0          |

The total medical risk score is normalized between **0 and 1** before model training.

---

## 🤖 Machine Learning Models Evaluated

The following regression models were explored:

* Linear Regression
* Ridge Regression
* XGBoost Regressor

Hyperparameter tuning was performed using:

* RandomizedSearchCV
* Cross-validation

---

## 🎯 Final Model Architecture

This project adopts a **two-model prediction strategy**:

### Model 1: Young Population (Age ≤ 25)

* Dedicated model trained specifically on younger individuals
* Separate feature scaling pipeline

### Model 2: General Population (Age > 25)

* Dedicated model trained on the remaining population
* Optimized using hyperparameter tuning

At prediction time, the application automatically selects the appropriate model based on the user's age.

---

## 📂 Project Structure

```bash
Health-Insurance-Premium-Prediction/
│
├── artifacts/
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   └── scaler_rest.joblib
│
├── notebooks/
│   ├── project_premium_predict_young.ipynb
│   └── project_premium_predict_rest.ipynb
│
├── Main.py
├── predict_helper.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/health-insurance-premium-prediction.git
cd health-insurance-premium-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit application:

```bash
streamlit run Main.py
```

The application will launch in your browser at:

```text
http://localhost:8501
```

---

## 📈 Workflow

```text
Data Collection
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Feature Scaling
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Model Serialization
        ↓
Streamlit Deployment
```

---

## 💡 Key Learnings

Through this project, I gained hands-on experience in:

* End-to-end machine learning project development
* Exploratory Data Analysis (EDA)
* Feature engineering techniques
* Regression modeling
* Hyperparameter optimization
* Model serialization using Joblib
* Building interactive ML applications with Streamlit
* Production-oriented inference pipelines

---

## 🔮 Future Improvements

* Deploy the application to cloud platforms
* Add SHAP-based explainability
* Integrate user authentication
* Implement premium confidence intervals
* Add model monitoring and retraining pipelines
* Explore ensemble learning approaches

---

## 👩‍💻 Author

**Induja P**

Data Analyst | Machine Learning Enthusiast | Analytics Professional

If you found this project useful, feel free to ⭐ star the repository.
