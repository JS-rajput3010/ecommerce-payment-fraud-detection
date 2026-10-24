import streamlit as st
import pandas as pd
import joblib

# ==========================
# Load Model & Preprocessor
# ==========================

model = joblib.load("xgboost_optuna.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="E-Commerce Payment Fraud Detection",
    page_icon="💳",
    layout="centered"
)

st.title("💳 E-Commerce Payment Fraud Detection")

st.markdown("Enter the transaction details below.")

# ==========================
# User Inputs
# ==========================

transaction_amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=1000.0
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "paypal",
        "credit card",
        "debit card",
        "bank transfer"
    ]
)

product_category = st.selectbox(
    "Product Category",
    [
        "electronics",
        "toys & games",
        "clothing",
        "home & garden",
        "health & beauty"
    ]
)

quantity = st.number_input(
    "Quantity",
    min_value=1,
    value=1
)

customer_age = st.number_input(
    "Customer Age",
    min_value=18,
    max_value=100,
    value=25
)

customer_location = st.text_input(
    "Customer Location",
    "Delhi"
)

device_used = st.selectbox(
    "Device Used",
    [
        "desktop",
        "tablet",
        "mobile"
    ]
)
account_age_days = st.number_input(
    "Account Age (Days)",
    min_value=0,
    value=100
)

transaction_hour = st.slider(
    "Transaction Hour",
    0,
    23,
    12
)

is_address_mismatch = st.selectbox(
    "Address Mismatch",
    [0, 1]
)

# ==========================
# Predict Button
# ==========================

if st.button("Predict Fraud"):

    # Create DataFrame
    new_transaction = pd.DataFrame({

        "Transaction Amount":[transaction_amount],
        "Payment Method":[payment_method],
        "Product Category":[product_category],
        "Quantity":[quantity],
        "Customer Age":[customer_age],
        "Customer Location":[customer_location],
        "Device Used":[device_used],
        "Account Age Days":[account_age_days],
        "Transaction Hour":[transaction_hour],
        "Is_Address_Mismatch":[is_address_mismatch]

    })

    # Apply Preprocessing
    processed_data = preprocessor.transform(new_transaction)

    # Prediction
    prediction = model.predict(processed_data)[0]

    probability = model.predict_proba(processed_data)[0][1]

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("🚨 Fraud Transaction Detected")
    else:
        st.success("✅ Genuine Transaction")

    st.metric(
        "Fraud Probability",
        f"{probability*100:.2f}%"
    )

    if probability >= 0.75:
        st.error("🔴 High Risk")

    elif probability >= 0.40:
        st.warning("🟠 Medium Risk")

    else:
        st.success("🟢 Low Risk")