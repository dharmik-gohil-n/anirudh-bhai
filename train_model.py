import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

from .feature_engineering import create_features
from .config import DATA_PROCESSED, MODEL_PATH

def train_model():
    df = pd.read_csv(DATA_PROCESSED, parse_dates=['date'])

    df = create_features(df)

    X = df[['month', 'retail_transfers']]
    y = df['total_sales']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_model()