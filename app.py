import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("accident_risk_model.pkl", "rb"))

st.title("🚗 Road Accident Risk Predictor")
st.write("Predict the risk of road accidents based on traffic conditions.")

# User Inputs
traffic_density = st.number_input("Enter Traffic Density (vehicles per km):", min_value=0, step=1)
avg_speed = st.number_input("Enter Average Speed (km/h):", min_value=0, step=1)

weather = st.selectbox("Weather Condition", ["Clear", "Rainy", "Foggy", "Snowy"])
time_of_day = st.selectbox("Select Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
road_type = st.selectbox("Select Road Type", ["Highway", "City Road", "Rural Road"])
previous_accidents = st.number_input("Number of Previous Accidents in the Area:", min_value=0, step=1)

# Convert categorical variables into numerical form
weather_mapping = {"Clear": 1, "Rainy": 2, "Foggy": 3, "Snowy": 4}
time_mapping = {"Morning": 1, "Afternoon": 2, "Evening": 3, "Night": 4}
road_mapping = {"Highway": 1, "City Road": 2, "Rural Road": 3}

# Prepare input data
input_data = np.array([[
    traffic_density,
    avg_speed,
    weather_mapping[weather],
    time_mapping[time_of_day],
    road_mapping[road_type],
    previous_accidents
]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Accident Risk: {prediction:.2f}")
