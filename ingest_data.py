#!/usr/bin/env python3
"""
NYC Taxi Data Ingestion Script

This script automates the process of downloading and processing NYC taxi trip data.
It handles the complete ETL pipeline from Kaggle to S3, including:
- Downloading data from Kaggle using their API
- Extracting files from the downloaded archive
- Uploading CSV files to a specified S3 bucket

Required Environment:
    - Python 3.x'
    - Kaggle API credentials in ~/.kaggle/kaggle.json
    - AWS credentials configured for S3 access
    - Required packages: boto3, tqdm

Usage:
    python ingest_data.py
"""

import subprocess
import pathlib
import boto3
import os
import logging
import shutil
from tqdm import tqdm

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
DATASET_NAME = "microize/newyork-yellow-taxi-trip-data-2020-2019"
ZIP_FILE = pathlib.Path("newyork-yellow-taxi-trip-data-2020-2019.zip")
RAW_DIR = pathlib.Path("raw")
BUCKET_NAME = "taxi-demo-data-bucket"
AWS_REGION = "us-east-2"

def create_s3_bucket():
    """Create an S3 bucket for storing taxi data if it doesn't exist.

    Returns:
        boto3.client: Configured S3 client object

    Raises:
        boto3.exceptions.S3OperationError: If bucket creation fails
        boto3.exceptions.BotoCoreError: If AWS credentials are invalid
    """
    s3 = boto3.client("s3", region_name=AWS_REGION)
    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
        logger.info(f"Bucket {BUCKET_NAME} already exists")
    except:
        logger.info(f"Creating bucket {BUCKET_NAME} in region {AWS_REGION}")
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': AWS_REGION}
        )
        logger.info(f"Bucket {BUCKET_NAME} created successfully in {AWS_REGION}")
    return s3

def download_dataset():
    """Download the NYC taxi dataset using Kaggle API.
    
    Downloads the dataset specified by DATASET_NAME using the Kaggle CLI.
    Requires Kaggle API credentials to be configured in ~/.kaggle/kaggle.json.
    Skips download if the file already exists locally.

    Raises:
        subprocess.CalledProcessError: If Kaggle CLI command fails
        FileNotFoundError: If Kaggle credentials are not configured
    """
    if ZIP_FILE.exists():
        logger.info(f"File {ZIP_FILE} already exists, skipping download")
        return
    
    logger.info(f"Downloading dataset {DATASET_NAME}")
    try:
        subprocess.run(
            ["kaggle", "datasets", "download", "-d", DATASET_NAME],
            check=True
        )
        logger.info("Download completed successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to download dataset: {e}")
        raise

def extract_data():
    """Extract the downloaded zip file to the raw directory.
    
    Creates the raw directory if it doesn't exist and extracts all files
    from the ZIP_FILE into it. If data already exists in the raw directory,
    it will be cleaned up first to ensure a fresh extraction.

    Raises:
        FileNotFoundError: If the zip file is not found
        subprocess.CalledProcessError: If unzip command fails
    """
    if not ZIP_FILE.exists():
        raise FileNotFoundError(f"Zip file {ZIP_FILE} not found")
    
    # Check if raw directory exists and has data
    if RAW_DIR.exists():
        existing_files = list(RAW_DIR.glob("**/*"))
        if existing_files:
            logger.info(f"Found {len(existing_files)} existing files in {RAW_DIR}, cleaning up...")
            shutil.rmtree(RAW_DIR)
            logger.info("Existing raw directory cleaned up")
    
    RAW_DIR.mkdir(exist_ok=True)
    
    logger.info(f"Extracting {ZIP_FILE} to {RAW_DIR}")
    try:
        subprocess.run(
            ["unzip", "-o", str(ZIP_FILE), "-d", str(RAW_DIR)],
            check=True
        )
        logger.info("Extraction completed successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to extract data: {e}")
        raise

def upload_to_s3():
    """Upload CSV files from the raw directory to S3.
    
    Searches for all CSV files in the raw directory and its subdirectories,
    then uploads them to the S3 bucket under the 'raw/' prefix. Shows a
    progress bar during upload.

    Raises:
        FileNotFoundError: If raw directory doesn't exist
        boto3.exceptions.S3UploadFailedError: If file upload fails
        boto3.exceptions.BotoCoreError: If AWS credentials are invalid
    """
    if not RAW_DIR.exists():
        raise FileNotFoundError(f"Raw directory {RAW_DIR} not found")
    
    s3 = create_s3_bucket()
    # Find only CSV files
    files = list(RAW_DIR.glob("**/*.csv"))
    
    logger.info(f"Found {len(files)} CSV files to upload")
    for file_path in tqdm(files):
        key = f"raw/{file_path.name}"
        try:
            s3.upload_file(str(file_path), BUCKET_NAME, key)
            logger.info(f"Uploaded {key}")
        except Exception as e:
            logger.error(f"Failed to upload {key}: {e}")
            raise

def main():
    """Execute the complete data ingestion pipeline.
    
    Orchestrates the download, extraction, and upload process.
    The pipeline consists of three main steps:
    1. Download the dataset from Kaggle
    2. Extract the files to a local directory
    3. Upload CSV files to S3

    Raises:
        Exception: If any step in the pipeline fails
    """
    try:
        download_dataset()
        extract_data()
        upload_to_s3()
        logger.info("Data ingestion pipeline completed successfully")
    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise

if __name__ == "__main__":
    main()
