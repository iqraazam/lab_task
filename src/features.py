"""
Feature Engineering Script
Prepares features for model training
"""
import argparse
import pandas as pd
import numpy as np
import yaml
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def engineer_features(df, params):
    """Engineer features from the cleaned dataset"""
    selected_features = params['selected_features']
    target = params['target']
    
    # Select relevant columns
    feature_cols = selected_features.copy()
    df_model = df[feature_cols + [target]].copy()
    
    # Initialize label encoders dictionary
    label_encoders = {}
    
    # Encode categorical features
    categorical_features = ['property_type', 'city', 'province_name', 'Area Type', 'Area Category']
    
    for col in categorical_features:
        if col in df_model.columns:
            le = LabelEncoder()
            df_model[col] = le.fit_transform(df_model[col].astype(str))
            label_encoders[col] = le
    
    # Separate features and target
    X = df_model.drop(columns=[target])
    y = df_model[target]
    
    return X, y, label_encoders, X.columns.tolist()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="params.yaml")
    args = parser.parse_args()
    
    # Load parameters
    with open(args.config) as f:
        config = yaml.safe_load(f)
    
    features_params = config['features']
    prepare_params = config['prepare']
    
    # Load cleaned data
    print(f"Loading cleaned data from {prepare_params['output_file']}")
    df = pd.read_csv(prepare_params['output_file'])
    
    # Engineer features
    print("Engineering features...")
    X, y, label_encoders, feature_names = engineer_features(df, features_params)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=features_params['test_size'],
        random_state=features_params['random_state']
    )
    
    print(f"Training set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}")
    
    # Save splits
    os.makedirs('data', exist_ok=True)
    np.save('data/X_train.npy', X_train.values)
    np.save('data/X_test.npy', X_test.values)
    np.save('data/y_train.npy', y_train.values)
    np.save('data/y_test.npy', y_test.values)
    
    # Save label encoders and feature names
    os.makedirs('models', exist_ok=True)
    joblib.dump(label_encoders, 'models/label_encoders.pkl')
    joblib.dump(feature_names, 'models/feature_names.pkl')
    
    print("Feature engineering complete!")
