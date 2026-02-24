import streamlit as st
import joblib
import pandas as pd

pipe = joblib.load("output/realestate_model.pkl")

st.title("🏠 Real Estate Price Prediction")

area = st.number_input("Area (sqft)", min_value=200, step=10)
bhk = st.number_input("BHK", min_value=1, step=1)
bath = st.number_input("Bathrooms", min_value=1, step=1)

locations = [
    "MVP Colony",
    "Dwaraka Nagar",
    "Gajuwaka",
    "Madhurawada",
    "Seethammadhara",
    "Akkayyapalem",
    "Yendada",
    "Pendurthi",
    "NAD Junction",
    "Rushikonda",
    "Simhachalam",
    "PM Palem",
    "Steel Plant Township",
    "Anakapalli"
]

location = st.selectbox("Location", locations)

if st.button("Predict Price"):
    row = pd.DataFrame([{
        "area": area,
        "bhk": bhk,
        "bathrooms": bath,
        "location": location
    }])

    pred = pipe.predict(row)[0]
    st.success(f"Predicted Price: ₹ {pred:,.0f}")