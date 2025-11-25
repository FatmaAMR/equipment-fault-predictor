# client/ui.py

import streamlit as st
import requests

st.title("Anomaly/Fault Detector")

st.markdown("Enter the equipment parameters to predict failure:")

# Input fields
temperature = st.number_input("Temperature", value=0.0)
pressure = st.number_input("Pressure", value=0.0)
vibration = st.number_input("Vibration", value=0.0)
humidity = st.number_input("Humidity", value=0.0)
equipment = st.selectbox("Equipment Type", ["Compressor", "Pump", "Turbine"])

if st.button("Predict Failure"):
    # Prepare payload for FastAPI
    payload = {
        "temperature": temperature,
        "pressure": pressure,
        "vibration": vibration,
        "humidity": humidity,
        "equipment": equipment
    }

    try:
        # Call the FastAPI endpoint
        response = requests.post("http://127.0.0.1:8000/predict-failure", json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction Result: {result}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Failed to connect to API: {e}")
