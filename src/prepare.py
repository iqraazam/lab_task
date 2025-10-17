"""
Data Preparation Script
Cleans and preprocesses the raw Pakistan House Price dataset
"""
import argparse
import pandas as pd
import yaml
import os

def clean_data(df):
    """Clean and preprocess the dataset"""
    # Remove any duplicates
    df = df.drop_duplicates(subset=['property_id'])
    
    # Remove rows with missing critical values
    df = df.dropna(subset=['price', 'bedrooms', 'baths', 'Area Size'])
    
    # Remove outliers (price > 0 and reasonable values)
    df = df[df['price'] > 0]
    df = df[df['price'] < df['price'].quantile(0.99)]  # Remove top 1% outliers
    
    # Remove unreasonable bedrooms/baths
    df = df[df['bedrooms'] <= 20]
    df = df[df['baths'] <= 20]
    
    # Fill missing agency/agent with 'Unknown'
    df['agency'] = df['agency'].fillna('Unknown')
    df['agent'] = df['agent'].fillna('Unknown')
    
    print(f"Dataset shape after cleaning: {df.shape}")
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="params.yaml")
    args = parser.parse_args()
    
    # Load parameters
    with open(args.config) as f:
        params = yaml.safe_load(f)['prepare']
    
    # Load raw data
    print(f"Loading data from {params['input_file']}")
    df = pd.read_csv(params['input_file'])
    print(f"Original dataset shape: {df.shape}")
    
    # Clean data
    df_cleaned = clean_data(df)
    
    # Save cleaned data
    os.makedirs(os.path.dirname(params['output_file']), exist_ok=True)
    df_cleaned.to_csv(params['output_file'], index=False)
    print(f"Cleaned data saved to {params['output_file']}")
