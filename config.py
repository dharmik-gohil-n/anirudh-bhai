import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW = os.path.join(BASE_DIR, "data/raw/data.csv")
DATA_PROCESSED = os.path.join(BASE_DIR, "data/processed/cleaned_data.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models/model.pkl")