import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
model = joblib.load(BASE_DIR / "fraud_detection_model.pkl")

st.title("Credit Card Fraud Detection")

st.markdown("Enter transaction details")

st.divider()

transaction_type = st.selectbox(
    "Transaction Type",
    ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN']
)

amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    prediction = model.predict(input_data)

    st.subheader(f"Prediction Result: {prediction[0]}")

    if prediction[0] == 1:
        st.error("Fraudulent Transaction")
    else:
        st.success("Legitimate Transaction")