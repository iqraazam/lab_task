# Pakistan House Price Prediction - DVC ML Pipeline

A complete end-to-end reproducible machine learning project for predicting house prices in Pakistan using DVC (Data Version Control), Git, and Flask.

## 🎯 Project Overview

This project implements a complete ML workflow with:
- **Data Version Control** using DVC
- **Reproducible ML Pipeline** with automated stages
- **RandomForest Regression Model** for price prediction
- **Flask Web Application** for easy predictions
- **Git Integration** for code versioning

## 📋 Dataset

**Pakistan House Price Dataset** (Zameen.com)
- Source: `data/zameen-updated.csv`
- 168,000+ property listings
- Features: property type, location, city, bedrooms, bathrooms, area, etc.
- Target: Property price (PKR)

## 🚀 Quick Start

### 1. Environment Setup

```powershell
# Activate virtual environment
.\.venv\Scripts\activate

# Install dependencies (already done)
pip install dvc pandas scikit-learn joblib flask pyyaml
```

### 2. Run the DVC Pipeline

The pipeline consists of 4 stages: prepare → features → train → evaluate

```powershell
# Run the complete pipeline
python -m dvc repro

# Or run individual stages
python -m dvc repro prepare
python -m dvc repro features
python -m dvc repro train
python -m dvc repro evaluate
```

### 3. View Results

```powershell
# Show pipeline status
python -m dvc status

# Show metrics
python -m dvc metrics show

# Visualize pipeline
python -m dvc dag
```

### 4. Deploy Flask Application

```powershell
# Run the Flask web server
python housepk_app.py
```

Then open your browser at: **http://127.0.0.1:5000**

## 📁 Project Structure

```
lab_task/
│
├── data/                          # Data directory
│   ├── zameen-updated.csv         # Raw dataset (tracked by DVC)
│   ├── house_data_cleaned.csv     # Cleaned data (DVC output)
│   ├── X_train.npy                # Training features
│   ├── X_test.npy                 # Test features
│   ├── y_train.npy                # Training labels
│   └── y_test.npy                 # Test labels
│
├── src/                           # Source code
│   ├── prepare.py                 # Data cleaning & preprocessing
│   ├── features.py                # Feature engineering
│   ├── train.py                   # Model training
│   └── evaluate.py                # Model evaluation
│
├── models/                        # Model artifacts (DVC outputs)
│   ├── house_price_model.pkl      # Trained model
│   ├── label_encoders.pkl         # Categorical encoders
│   └── feature_names.pkl          # Feature list
│
├── metrics/                       # Evaluation metrics
│   └── eval.json                  # Model performance metrics
│
├── templates/                     # Flask HTML templates
│   ├── index.html                 # Input form
│   ├── result.html                # Prediction result
│   └── error.html                 # Error page
│
├── dvc_storage/                   # Local DVC remote storage
│
├── params.yaml                    # ML hyperparameters
├── dvc.yaml                       # DVC pipeline definition
├── dvc.lock                       # DVC pipeline lock file
├── housepk_app.py                 # Flask web application
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🔧 Pipeline Stages

### Stage 1: Prepare
- **Script**: `src/prepare.py`
- **Input**: `data/zameen-updated.csv`
- **Output**: `data/house_data_cleaned.csv`
- **Purpose**: Clean data, remove duplicates, handle outliers

### Stage 2: Features
- **Script**: `src/features.py`
- **Input**: Cleaned data
- **Output**: Train/test splits, encoders, feature names
- **Purpose**: Feature engineering, encoding, train/test split

### Stage 3: Train
- **Script**: `src/train.py`
- **Input**: Training data
- **Output**: `models/house_price_model.pkl`
- **Purpose**: Train RandomForest regression model

### Stage 4: Evaluate
- **Script**: `src/evaluate.py`
- **Input**: Model + test data
- **Output**: `metrics/eval.json`
- **Purpose**: Evaluate model performance (R², MAE, RMSE)

## 📊 Model Features

The model uses the following features:
- **property_type**: Type of property (House, Flat, etc.)
- **city**: City location
- **province_name**: Province
- **latitude**: Geographic latitude
- **longitude**: Geographic longitude
- **baths**: Number of bathrooms
- **bedrooms**: Number of bedrooms
- **Area Type**: Unit of area measurement (Marla, Kanal, etc.)
- **Area Size**: Numeric area size
- **Area Category**: Area range category

## 🌐 Flask Web Application

The Flask app provides:
- **Web UI**: Beautiful form-based interface for predictions
- **REST API**: JSON endpoint at `/api/predict`
- **Health Check**: Status endpoint at `/health`

### API Usage Example

```python
import requests

# Prediction request
response = requests.post('http://127.0.0.1:5000/api/predict', json={
    "property_type": "House",
    "city": "Islamabad",
    "province_name": "Islamabad Capital",
    "latitude": 33.6844,
    "longitude": 73.0479,
    "baths": 3,
    "bedrooms": 4,
    "Area Type": "Marla",
    "Area Size": 10.0,
    "Area Category": "10-15 Marla"
})

print(response.json())
# Output: {"prediction": 15000000.0, "formatted": "PKR 15,000,000"}
```

## 🔄 Git & DVC Workflow

### Track Data with DVC

```powershell
# Track the dataset
python -m dvc add data/zameen-updated.csv

# Commit DVC metadata
git add data/zameen-updated.csv.dvc .gitignore
git commit -m "Track dataset with DVC"
```

### Push to Remote

```powershell
# Push DVC tracked files
python -m dvc push

# Push Git commits
git push origin main
```

### Pull from Remote

```powershell
# Pull code from Git
git pull origin main

# Pull DVC tracked data/models
python -m dvc pull
```

## 📈 Experiment Tracking

Change parameters in `params.yaml` and rerun:

```powershell
# Edit params.yaml
# Change train.n_estimators to 200

# Reproduce pipeline
python -m dvc repro

# Compare experiments
python -m dvc metrics diff
```

## 🎨 Hyperparameters

Edit `params.yaml` to customize:

```yaml
train:
  n_estimators: 100          # Number of trees
  max_depth: 10              # Maximum tree depth
  min_samples_split: 5       # Minimum samples to split
  random_state: 42           # Random seed
```

## 🐛 Troubleshooting

### Model not found error
```powershell
# Run the pipeline first
python -m dvc repro
```

### DVC commands not working
```powershell
# Use module execution
python -m dvc status
python -m dvc repro
```

### Port 5000 already in use
```python
# Edit housepk_app.py, change port in last line:
app.run(debug=True, host="0.0.0.0", port=5001)
```

## 📚 Documentation

- [DVC Documentation](https://dvc.org/doc)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Documentation](https://scikit-learn.org/)

## 👨‍💻 Author

ML Operations Lab Task - House Price Prediction with DVC

## 📄 License

This project is for educational purposes.

---

**Happy Predicting! 🎉**
