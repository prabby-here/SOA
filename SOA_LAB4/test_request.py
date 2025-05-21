import requests
import json

try:
    data = {"features": [5.1, 3.5, 1.4, 0.2]}
    print("Sending request with data:", data)
    
    response = requests.post(
        "http://localhost:5002/predict",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    
    print("Response status code:", response.status_code)
    print("Response content:", response.text)
    
    if response.status_code == 200:
        result = response.json()
        print("Prediction result:", result)
    else:
        print("Error:", response.text)
except Exception as e:
    print("Error occurred:",str(e))