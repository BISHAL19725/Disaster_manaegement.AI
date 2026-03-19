import pandas as pd
import random


rows = 500

data = []

for i in range(rows):

    
    rainfall = random.uniform(0, 300)        # mm
    wind_speed = random.uniform(0, 150)      # km/h
    humidity = random.uniform(20, 100)       # %
    river_level = random.uniform(1, 5)       # scale
    temperature = random.uniform(10, 40)     # °C

    # risk scoring logic
    score = 0

    if rainfall > 180:
        score += 2
    elif rainfall > 120:
        score += 1

    if river_level > 4:
        score += 2
    elif river_level > 3:
        score += 1

    if wind_speed > 100:
        score += 2
    elif wind_speed > 70:
        score += 1

    if humidity > 85:
        score += 1

    # final disaster risk
    if score >= 3:
        risk = 1
    else:
        risk = 0

    data.append([
        rainfall,
        wind_speed,
        humidity,
        river_level,
        temperature,
        risk
    ])


df=pd.DataFrame(
    data,
    columns=[
        "rainfall_mm",
        "windspeed_kmh",
        "humidity_percent",
        "river_level_scale",
        "temparature_c",
        "disaster_risk"
    ]
)

df.to_csv("data/disaster_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())