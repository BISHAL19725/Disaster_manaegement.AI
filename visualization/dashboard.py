import streamlit as st
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), "..", "models", "disaster_model.pkl")

model = pickle.load(open(model_path, "rb"))




st.title("🌍 Disaster Prediction System")

rainfall = st.slider("Rainfall (mm)", 0.0, 300.0, 50.0)
wind_speed = st.slider("Wind Speed (km/h)", 0.0, 150.0, 20.0)
humidity = st.slider("Humidity (%)", 20.0, 100.0, 50.0)
river_level = st.slider("River Level (1-5)", 1.0, 5.0, 2.0)
temperature = st.slider("Temperature (°C)", 10.0, 40.0, 25.0)

if st.button("predict"):
    input_data=[[rainfall,wind_speed,humidity,river_level,temperature]]
    prediction=model.predict(input_data)
    if prediction[0]==1:
        st.error("⚠️ High Disaster Risk!")
    else:
        st.success("✅ Safe Condition")


