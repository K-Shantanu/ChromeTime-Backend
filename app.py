from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)
model = joblib.load("C:/Users/kshan/OneDrive/Desktop/ChromeTime/backend/model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    prediction = model.predict([url])[0]
    return jsonify({'category': prediction})

if __name__ == '__main__':
    app.run(debug=True)
