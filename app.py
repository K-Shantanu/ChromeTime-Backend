from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)

# Allow requests from your extension's origin
CORS(app, origins=["chrome-extension://ffpllnbcpmollbjcpgfmhkecdnpohjpf"])

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    prediction = model.predict([url])[0]
    return jsonify({"category": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
