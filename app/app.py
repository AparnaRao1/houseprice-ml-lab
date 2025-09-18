import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("../model.pkl")
locality_options = ["BTM Layout", "K R Puram", "Marathahalli", "Indiranagar", "Electronic","Yalahanka","Malleshwaram","Jayanagar"]
facing_options = ["North", "South", "East", "West", "North-East", "North-West", "South-East", "South-West"]
parking_options = ["None", "Bike", "Car", "Both"]
with st.form("predict"):
    locality = st.selectbox("Locality", locality_options)
    area = st.number_input("Square Feet", value=1000)
    rent = st.number_input("Monthly Rent", value=15000)
    facing = st.selectbox("Facing", facing_options)
    BHK = st.number_input("Bedrooms", value=2, min_value=0, max_value=10, step=1)
    bathrooms=st.number_input("Number of bathrooms",value=1)
    parking = st.selectbox("Parking", parking_options)
    submitted = st.form_submit_button("Predict")

if submitted:
    X = pd.DataFrame([{
        "locality": locality if locality else "Missing",
        "area": area,
        "rent": rent,
        "facing":facing,
        "BHK": BHK,
        "bathrooms":bathrooms,
        "parking": parking if parking else "Missing"
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
