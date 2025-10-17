"""
Flask Web Application for Pakistan House Price Prediction
Loads the trained model and provides a web interface for predictions
"""
import os
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify

# Paths
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(APP_ROOT, "models")

# Initialize Flask app
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Global variables for model artifacts
model = None
label_encoders = None
feature_names = None

def load_model_artifacts():
    """Load all model artifacts"""
    global model, label_encoders, feature_names
    
    try:
        model = joblib.load(os.path.join(MODEL_DIR, "house_price_model.pkl"))
        label_encoders = joblib.load(os.path.join(MODEL_DIR, "label_encoders.pkl"))
        feature_names = joblib.load(os.path.join(MODEL_DIR, "feature_names.pkl"))
        print("✓ Model artifacts loaded successfully")
        return True
    except Exception as e:
        print(f"✗ Error loading model artifacts: {e}")
        return False

# Feature metadata for form generation
FEATURE_INFO = {
    'property_type': {
        'label': 'Property Type',
        'type': 'categorical',
        'default_options': ['House', 'Flat', 'Upper Portion', 'Lower Portion', 'Farm House', 'Room', 'Penthouse']
    },
    'city': {
        'label': 'City',
        'type': 'categorical',
        'default_options': ['Islamabad', 'Rawalpindi', 'Lahore', 'Karachi', 'Faisalabad', 'Multan']
    },
    'province_name': {
        'label': 'Province',
        'type': 'categorical',
        'default_options': ['Islamabad Capital', 'Punjab', 'Sindh', 'Khyber Pakhtunkhwa', 'Balochistan']
    },
    'latitude': {
        'label': 'Latitude',
        'type': 'numeric',
        'min': 24.0,
        'max': 37.0,
        'default': 33.6844
    },
    'longitude': {
        'label': 'Longitude',
        'type': 'numeric',
        'min': 60.0,
        'max': 78.0,
        'default': 73.0479
    },
    'baths': {
        'label': 'Number of Bathrooms',
        'type': 'numeric',
        'min': 1,
        'max': 10,
        'default': 2
    },
    'bedrooms': {
        'label': 'Number of Bedrooms',
        'type': 'numeric',
        'min': 1,
        'max': 10,
        'default': 3
    },
    'Area Type': {
        'label': 'Area Type',
        'type': 'categorical',
        'default_options': ['Marla', 'Kanal', 'Square Feet', 'Square Yards', 'Square Meter']
    },
    'Area Size': {
        'label': 'Area Size',
        'type': 'numeric',
        'min': 0.5,
        'max': 100.0,
        'default': 5.0
    },
    'Area Category': {
        'label': 'Area Category',
        'type': 'categorical',
        'default_options': ['0-5 Marla', '5-10 Marla', '10-15 Marla', '1-5 Kanal', '5-10 Kanal']
    }
}

@app.route("/", methods=["GET"])
def index():
    """Render the home page with input form"""
    # Prepare feature metadata with actual encoder classes if available
    features_meta = []
    for feat_name in feature_names:
        if feat_name in FEATURE_INFO:
            feat_info = FEATURE_INFO[feat_name].copy()
            feat_info['name'] = feat_name
            
            # If categorical, get actual classes from encoder
            if feat_info['type'] == 'categorical' and label_encoders and feat_name in label_encoders:
                feat_info['options'] = label_encoders[feat_name].classes_.tolist()
            elif feat_info['type'] == 'categorical':
                feat_info['options'] = feat_info.get('default_options', [])
            
            features_meta.append(feat_info)
    
    return render_template("index.html", features=features_meta)

@app.route("/predict", methods=["POST"])
def predict():
    """Handle prediction request from form"""
    try:
        # Build input vector in the same order as feature_names
        input_data = []
        for feat in feature_names:
            value = request.form.get(feat)
            
            if value is None or value == '':
                return render_template("error.html", 
                    error=f"Missing value for: {feat}"), 400
            
            # Handle categorical features
            if feat in label_encoders:
                try:
                    encoded_value = label_encoders[feat].transform([str(value)])[0]
                    input_data.append(encoded_value)
                except Exception as e:
                    return render_template("error.html", 
                        error=f"Invalid value '{value}' for {feat}"), 400
            else:
                # Handle numeric features
                try:
                    input_data.append(float(value))
                except:
                    return render_template("error.html", 
                        error=f"Invalid numeric value '{value}' for {feat}"), 400
        
        # Make prediction
        X = np.array(input_data).reshape(1, -1)
        prediction = model.predict(X)[0]
        
        # Format prediction
        predicted_price = round(float(prediction), 2)
        formatted_price = f"PKR {predicted_price:,.0f}"
        
        # Prepare input summary
        input_summary = {feat: request.form.get(feat) for feat in feature_names}
        
        return render_template("result.html", 
            prediction=formatted_price,
            predicted_value=predicted_price,
            input_data=input_summary)
    
    except Exception as e:
        return render_template("error.html", 
            error=f"Prediction error: {str(e)}"), 500

@app.route("/api/predict", methods=["POST"])
def api_predict():
    """JSON API endpoint for predictions"""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "JSON payload required"}), 400
        
        # Build input vector
        input_data = []
        for feat in feature_names:
            if feat not in data:
                return jsonify({"error": f"Missing field: {feat}"}), 400
            
            value = data[feat]
            
            # Handle categorical features
            if feat in label_encoders:
                try:
                    encoded_value = label_encoders[feat].transform([str(value)])[0]
                    input_data.append(encoded_value)
                except Exception as e:
                    return jsonify({"error": f"Invalid value for {feat}: {value}"}), 400
            else:
                # Handle numeric features
                try:
                    input_data.append(float(value))
                except:
                    return jsonify({"error": f"Invalid numeric value for {feat}: {value}"}), 400
        
        # Make prediction
        X = np.array(input_data).reshape(1, -1)
        prediction = model.predict(X)[0]
        
        return jsonify({
            "prediction": float(prediction),
            "formatted": f"PKR {float(prediction):,.0f}"
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    status = {
        "status": "healthy" if model is not None else "unhealthy",
        "model_loaded": model is not None,
        "encoders_loaded": label_encoders is not None,
        "features_loaded": feature_names is not None
    }
    return jsonify(status)

if __name__ == "__main__":
    print("=" * 60)
    print("Pakistan House Price Prediction - Flask Application")
    print("=" * 60)
    
    # Load model artifacts
    if load_model_artifacts():
        print(f"Features: {len(feature_names)} loaded")
        print(f"Encoders: {len(label_encoders)} loaded")
        print("\nStarting Flask server...")
        print("Access the application at: http://127.0.0.1:5000")
        print("=" * 60)
        app.run(debug=True, host="0.0.0.0", port=5000)
    else:
        print("\n✗ Failed to load model artifacts!")
        print("Please run the DVC pipeline first: python -m dvc repro")
        print("=" * 60)
