from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)
import os
model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))

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
