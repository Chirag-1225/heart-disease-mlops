from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

# Point Flask to the correct folder structure
app = Flask(__name__, template_folder='../templates')

# Load the saved model and scaler
with open('best_model.pkl', 'rb') as m_file:
    model = pickle.load(m_file)

with open('scaler.pkl', 'rb') as s_file:
    scaler = pickle.load(s_file)

# ROUTE 1: Render the web interface front page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# ROUTE 2: API endpoint for health monitoring
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "heart-disease-prediction"}), 200

# ROUTE 3: API endpoint handling ML calculations
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features sent by the web page form
        features = np.array([[
            data['age'], data['sex'], data['cp'], 
            data['trestbps'], data['chol'], data['thalach']
        ]])
        
        # Apply normalization scaling transformations
        scaled_features = scaler.transform(features)
        
        # Run inference logic
        prediction = model.predict(scaled_features)[0]
        
        # Calculate uncertainty confidence metric
        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(scaled_features)[0][1])
        else:
            probability = 1.0 if prediction == 1 else 0.0
        
        return jsonify({
            "heart_disease_predicted": int(prediction),
            "probability": probability
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)