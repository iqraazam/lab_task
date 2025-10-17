# 🎯 QUICK START COMMANDS

## Everything is Ready! Here's How to Run It:

### 1️⃣ Start the Flask Application
```powershell
python housepk_app.py
```

**Then open your browser:** http://127.0.0.1:5000

---

## ✅ What's Already Done

✓ Environment activated
✓ All libraries installed (DVC, pandas, sklearn, Flask, etc.)
✓ Git & DVC initialized
✓ Dataset tracked with DVC (168,446 properties)
✓ Complete pipeline executed:
  - Data cleaned (166,673 records)
  - Features engineered (10 features)
  - Model trained (RandomForest)
  - Model evaluated (R² = 0.61)
✓ Model and artifacts saved
✓ Flask app with templates created
✓ DVC remote storage configured
✓ All changes committed to Git
✓ DVC files pushed to remote

---

## 🌐 Web Application Features

The Flask app includes:
- **Beautiful Web UI** - Responsive form interface
- **Instant Predictions** - Real-time house price estimates
- **JSON API** - RESTful endpoint for integrations
- **Error Handling** - User-friendly error messages
- **Health Check** - Status monitoring endpoint

**Input Fields:**
- Property Type (House, Flat, etc.)
- City & Province
- Latitude & Longitude
- Number of Bedrooms
- Number of Bathrooms
- Area Type (Marla, Kanal, etc.)
- Area Size
- Area Category

---

## 📊 Model Performance

**Achieved Metrics:**
- **R² Score:** 0.6117 (explains 61% of price variance)
- **MAE:** PKR 6,940,042 (average error)
- **RMSE:** PKR 13,875,842

**Model Details:**
- Algorithm: RandomForest Regressor
- Training Samples: 133,338
- Test Samples: 33,335
- Features: 10
- Hyperparameters in `params.yaml`

---

## 🔄 Optional: Rerun Pipeline

If you want to retrain the model with different parameters:

```powershell
# 1. Edit params.yaml with new hyperparameters
# 2. Run the pipeline
python -m dvc repro

# 3. View new metrics
python -m dvc metrics show
```

---

## 🧪 Test the API

Open a new PowerShell terminal and run:

```powershell
python test_api.py
```

Or test manually with curl/Postman:
```powershell
# Example prediction
curl -X POST http://127.0.0.1:5000/api/predict `
-H "Content-Type: application/json" `
-d '{
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
}'
```

---

## 📝 View Pipeline Status

```powershell
# Pipeline status
python -m dvc status

# View metrics
python -m dvc metrics show

# Show pipeline DAG
python -m dvc dag

# List DVC tracked files
python -m dvc list . --dvc-only
```

---

## 🎨 Experiment with Different Parameters

1. Edit `params.yaml`:
```yaml
train:
  n_estimators: 200    # Change from 100
  max_depth: 15        # Change from 10
  min_samples_split: 2 # Change from 5
```

2. Rerun pipeline:
```powershell
python -m dvc repro
```

3. Compare results:
```powershell
python -m dvc metrics diff
```

---

## 📦 Version Control Commands

### Commit Changes
```powershell
git add .
git commit -m "Your message"
```

### Push to DVC Remote
```powershell
python -m dvc push
```

### Push to GitHub (when you create a repo)
```powershell
git remote add origin <your-github-url>
git push -u origin main
```

### Pull from Remote (for team collaboration)
```powershell
git pull origin main
python -m dvc pull
```

---

## 📁 Important Files

| File | Description |
|------|-------------|
| `housepk_app.py` | Flask web application |
| `params.yaml` | ML hyperparameters |
| `dvc.yaml` | Pipeline definition |
| `dvc.lock` | Pipeline execution state |
| `src/*.py` | Pipeline scripts |
| `templates/*.html` | Web UI templates |
| `models/house_price_model.pkl` | Trained model |
| `metrics/eval.json` | Model metrics |
| `README.md` | Full documentation |

---

## 🎯 Main Use Cases

### 1. Make Predictions (Web UI)
```powershell
python housepk_app.py
# Visit: http://127.0.0.1:5000
```

### 2. Make Predictions (API)
```python
import requests
response = requests.post('http://127.0.0.1:5000/api/predict', json={
    "property_type": "House",
    "city": "Islamabad",
    # ... other fields
})
print(response.json()["formatted"])
```

### 3. Retrain Model
```powershell
# Edit params.yaml then:
python -m dvc repro
```

### 4. View Experiment History
```powershell
git log --oneline
python -m dvc metrics show
```

---

## 🚀 You're All Set!

Everything is configured and working. Just run:

```powershell
python housepk_app.py
```

And start predicting house prices! 🏠💰

---

**For detailed documentation, see:**
- `README.md` - Complete project documentation
- `SETUP_GUIDE.md` - Detailed setup guide
- `test_api.py` - API usage examples

**Questions?** All code is documented and ready to use!
