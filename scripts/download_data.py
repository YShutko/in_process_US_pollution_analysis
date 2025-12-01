"""Download dataset from Kaggle using Kaggle API with improved CLI and checks.

This script supports:
- `--dataset` to specify the Kaggle dataset (default: sogun3/uspollution)
- `--dest` to specify destination path (default: data/raw)

Authentication:
- Place `kaggle.json` at the user config dir (Windows: C:\\Users\\<you>\\.kaggle\\kaggle.json)
- OR set environment variables `KAGGLE_USERNAME` and `KAGGLE_KEY`.

On Windows PowerShell you can set env vars for the current session with:
  $env:KAGGLE_USERNAME = "your_username"; $env:KAGGLE_KEY = "your_key"
To set them persistently (user scope) use [Environment]::SetEnvironmentVariable.
"""

import argparse
import os
import sys
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi


def check_credentials():
    """Check for Kaggle credentials either via env vars or kaggle.json file.

    Returns True if a likely credential source is present, False otherwise.
    """
    # Check env vars first
    if os.environ.get("KAGGLE_USERNAME") and os.environ.get("KAGGLE_KEY"):
        return True

    # Check standard config location or KAGGLE_CONFIG_DIR
    config_dir = os.environ.get("KAGGLE_CONFIG_DIR")
    if config_dir:
        kfile = Path(config_dir) / "kaggle.json"
        if kfile.exists():
            return True

    # Default user .kaggle location
    home = Path.home()
    default = home / ".kaggle" / "kaggle.json"
    if default.exists():
        return True

    return False


def download_dataset(dataset: str, dest_path: str):
    dest = Path(dest_path)
    dest.mkdir(parents=True, exist_ok=True)

    api = KaggleApi()
    try:
        api.authenticate()
    except Exception as e:
        print("Failed to authenticate with Kaggle API:", e)
        print("Make sure you have placed kaggle.json in ~/.kaggle/ or set KAGGLE_USERNAME and KAGGLE_KEY environment variables.")
        sys.exit(2)

    try:
        print(f"Downloading dataset '{dataset}' to '{dest.resolve()}'...")
        api.dataset_download_files(dataset, path=str(dest), unzip=True)
        print(f"Dataset downloaded to {dest.resolve()}")
    except Exception as e:
        print("Failed to download dataset:", e)
        sys.exit(3)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Download Kaggle dataset to local folder")
    parser.add_argument("--dataset", "-d", default="sogun3/uspollution", help="Kaggle dataset (owner/dataset)")
    parser.add_argument("--dest", default=os.path.join("data", "raw"), help="Destination folder to save/unzip files")
    args = parser.parse_args(argv)

    if not check_credentials():
        print("Kaggle credentials not found.")
        print("Put your kaggle.json at ~/.kaggle/kaggle.json or set KAGGLE_USERNAME and KAGGLE_KEY environment variables.")
        print("See https://www.kaggle.com/docs/api for details.")
        sys.exit(1)

    download_dataset(args.dataset, args.dest)


if __name__ == "__main__":
    main()
