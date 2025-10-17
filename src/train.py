"""
Model Training Script
Trains a RandomForest Regressor on house price data
"""
import argparse
import os
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="params.yaml")
    args = parser.parse_args()

    # Load parameters
    with open(args.config) as f:
        params = yaml.safe_load(f)["train"]

    # Load training data
    X_train = np.load("data/X_train.npy")
    y_train = np.load("data/y_train.npy")
    
    print(f"Training with {X_train.shape[0]} samples...")

    # Train RandomForest Regressor
    model = RandomForestRegressor(
        n_estimators=params["n_estimators"],
        max_depth=params["max_depth"],
        min_samples_split=params["min_samples_split"],
        random_state=params["random_state"],
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    
    # Save model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, "models/house_price_model.pkl")
    print("Model saved to models/house_price_model.pkl")
