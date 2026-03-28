import os
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ✅ Correct model file name
model_path = os.path.join(BASE_DIR, "sales_model.pkl")
model = joblib.load(model_path)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    month = int(data.get("month", 0))
    day = int(data.get("day", 0))

    # Example prediction using your model
    prediction = model.predict([[month, day]])[0] if hasattr(model, "predict") else (month*100 + day*10)
    
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
