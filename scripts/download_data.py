"""
Download dataset from Kaggle using Kaggle API.
Ensure you have your Kaggle API credentials in ~/.kaggle/kaggle.json or set up the .kaggle folder.
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    dataset = "sogun3/uspollution"
    dest_path = os.path.join("data", "raw")
    os.makedirs(dest_path, exist_ok=True)
    
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(dataset, path=dest_path, unzip=True)
    print(f"Dataset downloaded to {dest_path}")

if __name__ == "__main__":
    download_dataset()
