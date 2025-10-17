# 🚀 COMPLETE SETUP GUIDE - Pakistan House Price Prediction

## ✅ Project Status: FULLY OPERATIONAL

All components have been successfully implemented and tested!

---

## 📦 What Has Been Completed

### ✓ Environment Setup
- Virtual environment activated
- All dependencies installed (DVC, pandas, scikit-learn, joblib, Flask, PyYAML)
- Python 3.13 configured

### ✓ Version Control
- Git repository initialized
- DVC initialized for data versioning
- Local DVC remote storage configured at `dvc_storage/`
- `.gitignore` configured for proper file exclusion

### ✓ Dataset
- Pakistan House Price dataset tracked with DVC
- 168,446 property listings
- Dataset successfully versioned and pushed to DVC remote

### ✓ ML Pipeline (DVC)
All 4 stages completed successfully:

1. **Prepare Stage** ✓
   - Data cleaning completed
   - 166,673 records after cleaning
   - Output: `data/house_data_cleaned.csv`

2. **Features Stage** ✓
   - Feature engineering complete
   - 10 features extracted
   - Train/test split: 133,338 / 33,335 samples
   - Label encoders created for 5 categorical features
   - Outputs: X_train, X_test, y_train, y_test, encoders

3. **Train Stage** ✓
   - RandomForest Regressor trained
   - Model saved: `models/house_price_model.pkl`
   - Training completed on 133,338 samples

4. **Evaluate Stage** ✓
   - Model evaluated on test set
   - **Metrics achieved:**
     - R² Score: **0.6117** (61% variance explained)
     - MAE: PKR 6,940,042
     - RMSE: PKR 13,875,842
   - Metrics saved: `metrics/eval.json`

### ✓ Flask Web Application
- Complete web interface created
- 3 HTML templates (index, result, error)
- Features:
  - Beautiful responsive UI
  - Form-based input
  - Real-time predictions
  - JSON API endpoint
  - Health check endpoint
- Successfully tested and running

### ✓ Files Created/Updated

**Configuration Files:**
- `params.yaml` - ML hyperparameters ✓
- `dvc.yaml` - Pipeline definition ✓
- `dvc.lock` - Pipeline state ✓
- `.gitignore` - Git exclusions ✓
- `.dvcignore` - DVC exclusions ✓
- `requirements.txt` - Dependencies ✓

**Source Code:**
- `src/prepare.py` - Data cleaning ✓
- `src/features.py` - Feature engineering ✓
- `src/train.py` - Model training ✓
- `src/evaluate.py` - Model evaluation ✓

**Flask Application:**
- `housepk_app.py` - Main Flask app ✓
- `templates/index.html` - Input form ✓
- `templates/result.html` - Prediction display ✓
- `templates/error.html` - Error handling ✓

**Testing & Documentation:**
- `test_api.py` - API test suite ✓
- `README.md` - Complete documentation ✓
- `SETUP_GUIDE.md` - This file ✓

---

## 🎯 How to Run the Complete System

### Step 1: Activate Environment
```powershell
.\.venv\Scripts\activate
```

### Step 2: Run DVC Pipeline (If needed)
```powershell
# Run complete pipeline
python -m dvc repro

# Or run individual stages
python -m dvc repro prepare
python -m dvc repro features
python -m dvc repro train
python -m dvc repro evaluate
```

### Step 3: Check Results
```powershell
# View metrics
python -m dvc metrics show

# Pipeline status
python -m dvc status

# Visualize pipeline
python -m dvc dag
```

### Step 4: Start Flask Application
```powershell
python housepk_app.py
```

**Access the web interface at:** http://127.0.0.1:5000

### Step 5: Test the API (Optional)
Open a new terminal and run:
```powershell
python test_api.py
```

---

## 🌐 Using the Web Application

### Web Interface (Recommended)
1. Open browser: http://127.0.0.1:5000
2. Fill in the property details:
   - Property Type (House, Flat, etc.)
   - City & Province
   - Location (Latitude/Longitude)
   - Bedrooms & Bathrooms
   - Area Type & Size
3. Click "Predict House Price"
4. View instant prediction!

### API Endpoint
**Endpoint:** `POST http://127.0.0.1:5000/api/predict`

**Example Request:**
```python
import requests

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
# Output: {"prediction": 15234567.89, "formatted": "PKR 15,234,568"}
```

---

## 📊 Model Performance

**Current Metrics (on test set of 33,335 samples):**

| Metric | Value | Interpretation |
|--------|-------|----------------|
| R² Score | 0.6117 | Model explains 61% of price variance |
| MAE | PKR 6.9M | Average error of 6.9 million rupees |
| RMSE | PKR 13.9M | Root mean squared error |

**Model Specifications:**
- Algorithm: RandomForest Regressor
- Number of Trees: 100
- Max Depth: 10
- Min Samples Split: 5
- Training Samples: 133,338
- Test Samples: 33,335

---

## 🔄 Git & DVC Workflow

### Commit Changes
```powershell
git add .
git commit -m "Your message"
```

### Push to Remote
```powershell
# Push DVC files
python -m dvc push

# Push Git commits (requires GitHub repo)
git push origin main
```

### Pull from Remote
```powershell
# Pull code
git pull origin main

# Pull data/models
python -m dvc pull
```

---

## 🎨 Experiment with Hyperparameters

Edit `params.yaml` to try different configurations:

```yaml
train:
  n_estimators: 200      # Try more trees
  max_depth: 15          # Deeper trees
  min_samples_split: 2   # More aggressive splitting
  random_state: 42
```

Then rerun:
```powershell
python -m dvc repro
```

---

## 📁 Project Structure

```
lab_task/
├── data/
│   ├── zameen-updated.csv          # Raw dataset (DVC tracked)
│   ├── house_data_cleaned.csv      # Cleaned data
│   └── *.npy                        # Train/test splits
│
├── models/
│   ├── house_price_model.pkl       # Trained model
│   ├── label_encoders.pkl          # Categorical encoders
│   └── feature_names.pkl           # Feature list
│
├── src/
│   ├── prepare.py                  # Data cleaning
│   ├── features.py                 # Feature engineering
│   ├── train.py                    # Model training
│   └── evaluate.py                 # Model evaluation
│
├── templates/
│   ├── index.html                  # Web form
│   ├── result.html                 # Prediction page
│   └── error.html                  # Error page
│
├── metrics/
│   └── eval.json                   # Model metrics
│
├── dvc_storage/                    # Local DVC remote
│
├── housepk_app.py                  # Flask application
├── test_api.py                     # API tests
├── params.yaml                     # Hyperparameters
├── dvc.yaml                        # Pipeline definition
├── dvc.lock                        # Pipeline state
├── requirements.txt                # Dependencies
├── README.md                       # Documentation
└── SETUP_GUIDE.md                  # This file
```

---

## 🐛 Troubleshooting

### Issue: Flask app won't start
**Solution:** Make sure the pipeline has run successfully
```powershell
python -m dvc repro
```

### Issue: DVC commands not recognized
**Solution:** Use Python module execution
```powershell
python -m dvc <command>
```

### Issue: Port 5000 in use
**Solution:** Edit `housepk_app.py` line 237, change port:
```python
app.run(debug=True, host="0.0.0.0", port=5001)
```

### Issue: Import errors
**Solution:** Ensure virtual environment is activated
```powershell
.\.venv\Scripts\activate
```

---

## 🎓 What You've Accomplished

✅ Built a complete end-to-end ML pipeline
✅ Implemented data version control with DVC
✅ Created a reproducible workflow
✅ Trained a machine learning model (R²=0.61)
✅ Deployed a web application with Flask
✅ Set up local and remote storage
✅ Committed everything to Git
✅ Created comprehensive documentation
✅ Built API endpoints for integration
✅ Implemented beautiful web UI

---

## 📈 Next Steps (Optional Improvements)

1. **Improve Model Performance:**
   - Add more features (property age, amenities)
   - Try different algorithms (XGBoost, LightGBM)
   - Tune hyperparameters with GridSearch

2. **Deploy to Cloud:**
   - Set up DVC remote on S3/GCS
   - Deploy Flask app to Heroku/AWS
   - Configure CI/CD pipeline

3. **Enhance Application:**
   - Add data visualization
   - Implement user authentication
   - Create admin dashboard
   - Add model comparison features

4. **Push to GitHub:**
   ```powershell
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

---

## 🎉 Congratulations!

You have successfully completed the entire ML Operations workflow:
- ✅ Data versioning
- ✅ Pipeline automation
- ✅ Model training & evaluation
- ✅ Web deployment
- ✅ API creation
- ✅ Documentation

**The system is ready to use!**

To start the application:
```powershell
python housepk_app.py
```

Then visit: **http://127.0.0.1:5000**

---

**Need Help?** Check README.md for detailed documentation!
