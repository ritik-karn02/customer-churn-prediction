import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")
st.title("Customer Churn Prediction Dashboard")

# Sidebar Inputs
st.sidebar.header("Customer Inputs")

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 70.0)

contract = st.sidebar.selectbox("Contract Type",
                               ["Month-to-month", "One year", "Two year"])

internet_service = st.sidebar.selectbox("Internet Service",
                                        ["DSL", "Fiber optic", "No"])

payment_method = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check",
     "Bank transfer (automatic)", "Credit card (automatic)"]
)

tech_support = st.sidebar.selectbox("Tech Support", ["Yes", "No"])
online_security = st.sidebar.selectbox("Online Security", ["Yes", "No"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", ["Yes", "No"])

# Create input
input_dict = {
    'Tenure Months': tenure,
    'Monthly Charges': monthly_charges,
    'Contract': contract,
    'Internet Service': internet_service,
    'Payment Method': payment_method,
    'Tech Support': tech_support,
    'Online Security': online_security,
    'Paperless Billing': paperless_billing,
    'Senior Citizen': 1 if senior_citizen == "Yes" else 0
}

input_data = pd.DataFrame([input_dict])

# Encoding
input_data = pd.get_dummies(input_data)
input_data = input_data.reindex(columns=model_columns, fill_value=0)

# Layout
col1, col2 = st.columns(2)

# Prediction
with col1:
    st.subheader("Prediction")

    if st.button("Predict Churn"):
        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            st.error(f"⚠️ Customer likely to CHURN\nChurn Probability: {round(prob*100,2)}%")
        else:
            st.success(f"✅ Customer NOT likely to churn\nChurn Probability: {round(prob*100,2)}%")

# Summary
with col2:
    st.subheader("Customer Summary")
    st.write(input_data)

# Sidebar Info
st.sidebar.subheader("Model Info")
st.sidebar.write("""
Model: XGBoost  
Dataset: IBM Telco Customer Churn  
Features: Behavioral + Service + Billing  
""")

# Footer
st.markdown("---")
st.markdown("Developed by Ritik Karn")