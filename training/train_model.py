import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle 

data=pd.read_csv("data/disaster_data.csv")

x=data[[
    "rainfall_mm",
    "windspeed_kmh",
    "humidity_percent",
    "river_level_scale",
    "temparature_c",
    "disaster_risk"    
]]

y=data["disaster_risk"]

x_train, x_test, y_train, y_test = train_test_split(
    x,y,test_size=0.2, random_state=42

)

model=RandomForestClassifier()

with open("models/disaster_model.pkl","wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")