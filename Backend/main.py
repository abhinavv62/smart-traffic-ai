from fastapi import FastAPI
from model import predict_congestion
from signal_logic import calculate_signal_time
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Traffic AI Running 🚦"}

@app.get("/traffic-data")
def get_traffic_data():
    vehicle_count = random.randint(10, 150)
    
    congestion = predict_congestion(vehicle_count)
    signal_time = calculate_signal_time(congestion)

    return {
        "vehicle_count": vehicle_count,
        "congestion_level": congestion,
        "recommended_signal_time": signal_time
    }

@app.get("/emergency")
def emergency_mode():
    return {
        "message": "Emergency Green Corridor Activated 🚑",
        "signal_time": 120
    }
