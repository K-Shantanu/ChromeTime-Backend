from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")
    prediction = model.predict([url])[0]
    return jsonify({"category": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
