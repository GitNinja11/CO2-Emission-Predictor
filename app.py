# app.py
import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline (preprocessor + model)
model = joblib.load("model.pkl")

# App title
st.set_page_config(page_title="CO₂ Emission Predictor", layout="centered")
st.title("🚗 CO₂ Emission Predictor")
st.markdown("Predict CO₂ emissions (g/km) based on vehicle specifications.")

# --- User Input Fields ---
engine_size = st.number_input("Engine Size(L)", min_value=0.0, format="%.1f")
cylinders = st.number_input("Cylinders", min_value=2, step=1)
transmission = st.selectbox("Transmission", ["Automatic", "Manual"])
fuel_type = st.selectbox("Fuel Type", ["Z", "D", "X", "E", "N"])  # Replace with real codes from dataset
fuel_city = st.number_input("Fuel Consumption City (L/100 km)", min_value=0.0, format="%.1f")
fuel_hwy = st.number_input("Fuel Consumption Hwy (L/100 km)", min_value=0.0, format="%.1f")
fuel_comb = st.number_input("Fuel Consumption Comb (L/100 km)", min_value=0.0, format="%.1f")
fuel_mpg = st.number_input("Fuel Consumption Comb (mpg)", min_value=0.0, format="%.1f")

# --- Make Prediction ---
if st.button("Predict CO₂ Emissions"):
    input_data = pd.DataFrame([{
        "Engine Size(L)": engine_size,
        "Cylinders": cylinders,
        "Transmission": transmission,
        "Fuel Type": fuel_type,
        "Fuel Consumption City (L/100 km)": fuel_city,
        "Fuel Consumption Hwy (L/100 km)": fuel_hwy,
        "Fuel Consumption Comb (L/100 km)": fuel_comb,
        "Fuel Consumption Comb (mpg)": fuel_mpg
    }])

    prediction = model.predict(input_data)
    st.success(f"🚘 Estimated CO₂ Emission: **{prediction[0]:.2f} g/km**")
