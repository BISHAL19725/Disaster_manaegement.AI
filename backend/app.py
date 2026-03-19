from fastapi import FastAPI
import pickle

app=FastAPI()
model=pickle.load(open("models/disaster_model.pkl","rb"))

@app.get("/")
def home():
    return{"message": "Disaster prediction API is running"}

@app.get("/predict")
def predict(
    rainfall: float,
    wind_speed: float,
    humidity: float,
    river_level: float,
    temperature: float
):
    input_data=[[
        rainfall,
        wind_speed,
        humidity,
        river_level,
        temperature
    ]]

    result=model.predict(input_data)

    return {"disaster_risk": int(result[0])}