from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

pipe = joblib.load("output/realestate_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    row = pd.DataFrame([{
        "area": data["area"],
        "bhk": data["bhk"],
        "bathrooms": data["bathrooms"],
        "location": data.get("location", "Adyar")
    }])

    pred = pipe.predict(row)[0]
    return jsonify({"predicted_price": float(pred)})

if __name__ == "__main__":
    app.run(debug=True)