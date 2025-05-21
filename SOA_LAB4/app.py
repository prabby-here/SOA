# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np
import sys

try:
    print("Loading model...")
    model = joblib.load("iris_model.pkl")
    print("Model loaded successfully")
except Exception as e:
    print("Error loading model:", str(e), file=sys.stderr)
    sys.exit(1)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)  # Debug print
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        response = {"prediction": int(prediction[0])}
        print("Sending response:", response)  # Debug print
        return jsonify(response)
    except Exception as e:
        print("Error:", str(e), file=sys.stderr)  # Debug print
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5002,debug=True)