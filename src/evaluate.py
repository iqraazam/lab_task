"""
Model Evaluation Script
Evaluates the trained model on test data
"""
import argparse
import os
import joblib
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import json
import yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="params.yaml")
    args = parser.parse_args()

    # Load test data
    X_test = np.load("data/X_test.npy")
    y_test = np.load("data/y_test.npy")

    # Load model
    model = joblib.load("models/house_price_model.pkl")
    
    # Make predictions
    preds = model.predict(X_test)

    # Calculate metrics
    r2 = r2_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)

    metrics = {
        "r2_score": float(r2),
        "mean_absolute_error": float(mae),
        "mean_squared_error": float(mse),
        "root_mean_squared_error": float(rmse)
    }

    # Save metrics
    os.makedirs("metrics", exist_ok=True)
    with open("metrics/eval.json", "w") as f:
        json.dump(metrics, f, indent=2)
    
    print("Evaluation Metrics:")
    print(f"  R² Score: {r2:.4f}")
    print(f"  MAE: {mae:.2f}")
    print(f"  RMSE: {rmse:.2f}")
    print(f"\nMetrics saved to metrics/eval.json")
