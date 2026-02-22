import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy training data (vehicles count -> congestion level)
X = np.array([[10], [30], [50], [80], [120]])
y = np.array([1, 2, 3, 4, 5])  # 1=Low, 5=Very High

model = LinearRegression()
model.fit(X, y)

def predict_congestion(vehicle_count):
    prediction = model.predict([[vehicle_count]])
    return round(float(prediction[0]), 2)
