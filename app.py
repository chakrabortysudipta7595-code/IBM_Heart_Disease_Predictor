"""
Heart Disease Prediction Flask Application
This is the main Flask app that serves the web interface and provides prediction API
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os
from pathlib import Path

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model, scaler, and feature names
MODEL_PATH = 'models/heart_disease_model.pkl'
SCALER_PATH = 'models/scaler.pkl'
FEATURES_PATH = 'models/feature_names.pkl'

# Check if model files exist
if not os.path.exists(MODEL_PATH):
    print(f"Error: Model file not found at {MODEL_PATH}")
    print("Please run train_model.py first to train the model")

# Load model and preprocessing objects
try:
    model = pickle.load(open(MODEL_PATH, 'rb'))
    scaler = pickle.load(open(SCALER_PATH, 'rb'))
    with open(FEATURES_PATH, 'rb') as f:
        feature_names = pickle.load(f)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    scaler = None
    feature_names = None


@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint for predictions
    Expects JSON with the following fields:
    - age: int (age of patient)
    - sex: int (0=female, 1=male)
    - cp: int (chest pain type: 0-3)
    - trestbps: int (resting blood pressure)
    - chol: int (serum cholesterol in mg/dl)
    - fbs: int (fasting blood sugar > 120 mg/dl: 0=no, 1=yes)
    - restecg: int (resting electrocardiographic result: 0-2)
    - thalach: int (maximum heart rate achieved)
    - exang: int (exercise induced angina: 0=no, 1=yes)
    - oldpeak: float (ST depression)
    - slope: int (slope of ST segment: 0-2)
    - ca: int (number of major vessels colored: 0-4)
    - thal: int (thalassemia: 0-3)
    """
    
    if model is None:
        return jsonify({
            'success': False,
            'error': 'Model not loaded. Please ensure the model file exists.'
        }), 500
    
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Extract features in the correct order
        features = [
            float(data.get('age', 0)),
            float(data.get('sex', 0)),
            float(data.get('cp', 0)),
            float(data.get('trestbps', 0)),
            float(data.get('chol', 0)),
            float(data.get('fbs', 0)),
            float(data.get('restecg', 0)),
            float(data.get('thalach', 0)),
            float(data.get('exang', 0)),
            float(data.get('oldpeak', 0)),
            float(data.get('slope', 0)),
            float(data.get('ca', 0)),
            float(data.get('thal', 0))
        ]
        
        # Validate input ranges
        validation = validate_inputs(data)
        if not validation['valid']:
            return jsonify({
                'success': False,
                'error': validation['message']
            }), 400
        
        # Convert to numpy array and scale
        features_array = np.array(features).reshape(1, -1)
        features_scaled = scaler.transform(features_array)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        
        # Prepare response
        result = {
            'success': True,
            'prediction': int(prediction),
            'disease_probability': float(probability[1]) * 100,
            'no_disease_probability': float(probability[0]) * 100,
            'diagnosis': 'Heart Disease Detected' if prediction == 1 else 'No Heart Disease',
            'confidence': float(max(probability)) * 100
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error making prediction: {str(e)}'
        }), 500


@app.route('/api/info')
def info():
    """Return information about the model"""
    return jsonify({
        'model_name': 'Heart Disease Prediction',
        'algorithm': 'Logistic Regression',
        'features_count': len(feature_names) if feature_names else 0,
        'features': feature_names if feature_names else []
    })


def validate_inputs(data):
    """Validate input parameters"""
    try:
        age = float(data.get('age', 0))
        sex = float(data.get('sex', 0))
        cp = float(data.get('cp', 0))
        trestbps = float(data.get('trestbps', 0))
        chol = float(data.get('chol', 0))
        thalach = float(data.get('thalach', 0))
        ca = float(data.get('ca', 0))
        thal = float(data.get('thal', 0))
        
        if not (20 <= age <= 100):
            return {'valid': False, 'message': 'Age must be between 20 and 100'}
        
        if sex not in [0, 1]:
            return {'valid': False, 'message': 'Sex must be 0 (Female) or 1 (Male)'}
        
        if cp not in [0, 1, 2, 3]:
            return {'valid': False, 'message': 'Chest pain type must be 0-3'}
        
        if not (80 <= trestbps <= 200):
            return {'valid': False, 'message': 'Resting blood pressure must be between 80 and 200'}
        
        if not (100 <= chol <= 600):
            return {'valid': False, 'message': 'Cholesterol must be between 100 and 600'}
        
        if not (60 <= thalach <= 220):
            return {'valid': False, 'message': 'Max heart rate must be between 60 and 220'}
        
        if ca not in [0, 1, 2, 3, 4]:
            return {'valid': False, 'message': 'Major vessels must be 0-4'}
        
        if thal not in [0, 1, 2, 3]:
            return {'valid': False, 'message': 'Thalassemia type must be 0-3'}
        
        return {'valid': True}
    
    except ValueError:
        return {'valid': False, 'message': 'Invalid input format'}


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'success': False, 'error': 'Page not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'success': False, 'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
