import streamlit as st
import pandas as pd
from predict_helper import predict_premium

defaults = {
    "gender": "Select",
    "region": "Select",
    "marital_status": "Select",
    "bmi_category": "Select",
    "smoking_status": "Select",
    "employment_status": "Select",
    "income_level": "Select",
    "medical_history": "Select",
    "insurance_plan": "Select",
    "age": 18,
    "income_lakhs": 0.0,
    "genetical_risk": 0,
    "number_of_dependants": 0,
}

for key, value in defaults.items():
    st.session_state.setdefault(key, value)

st.title("Health Insurance Premium Prediction App")
# Store all user inputs
user_inputs = {}

#Row 1

col1, col2, col3, col4 = st.columns(4)

with col1:
    user_inputs["age"] = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=18,
        step=1,
        key="age"
    )

with col2:
    user_inputs["income_lakhs"] = st.number_input(
        "Income in Lakhs",
        min_value=0.0,
        value=0.0,
        step=0.1,
        format="%.1f",
        key="income_lakhs"
    )

with col3:
    user_inputs["genetical_risk"] = st.number_input(
        "Genetical Risk",
        min_value=0,
        max_value=5,
        value=0,
        step=1,
        key="genetical_risk"
    )

with col4:
    user_inputs["number_of_dependants"] = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=3,
        value=0,
        step=1,
        key="number_of_dependants"
    )

# Row 2
col1, col2, col3, col4 = st.columns(4)

with col1:
    user_inputs["gender"] = st.selectbox(
        "Gender",
        ["Select", "Male", "Female"],
        key="gender"
    )

with col2:
    user_inputs["region"] = st.selectbox(
        "Region",
        ["Select", "Northeast", "Northwest", "Southeast", "Southwest"],
        key="region"
    )

with col3:
    user_inputs["marital_status"] = st.selectbox(
        "Marital Status",
        ["Select", "Unmarried", "Married"],
        key="marital_status"
    )

with col4:
    user_inputs["bmi_category"] = st.selectbox(
        "BMI Category",
        ["Select", "Overweight", "Underweight", "Normal", "Obesity"],
        key="bmi_category"
    )

# Row 2
col1, col2, col3, col4 = st.columns(4)

with col1:
    user_inputs["smoking_status"] = st.selectbox(
        "Smoking Status",
        ["Select", "Regular", "No Smoking", "Occasional"],
        key="smoking_status"
    )

with col2:
    user_inputs["employment_status"] = st.selectbox(
        "Employment Status",
        ["Select", "Self-Employed", "Freelancer", "Salaried"],
        key="employment_status"
    )

with col3:
    user_inputs["insurance_plan"] = st.selectbox(
        "Insurance Plan",
        ["Select", "Silver", "Bronze", "Gold"],
        key="insurance_plan"
    )

with col4:
    user_inputs["Medical History"] = st.selectbox(
        "Medical History",
        [
            "Select",
            "High blood pressure",
            "No Disease",
            "Diabetes & High blood pressure",
            "Diabetes & Heart disease",
            "Diabetes",
            "Diabetes & Thyroid",
            "Heart disease",
            "Thyroid",
            "High blood pressure & Heart disease"
        ],
        key="medical_history"
    )

    
    
_, col1, col2, _ = st.columns([2, 1, 1, 2])   
with col1:
    predict = st.button("🔮 Predict", use_container_width=True)

with col2:
    reset = st.button("🔄 Reset", use_container_width=True)

if predict:
    if "Select" in user_inputs.values():
        st.error("Please select a value for all fields.")
    else:
        print('Predicting Premium')
        prediction = predict_premium(user_inputs)
        st.success(f"Predicted Premium: ₹{prediction:,.2f}")
        
if reset:
    print('Resetting Inputs')
    for key in defaults:
        st.session_state.pop(key, None)

    st.rerun()