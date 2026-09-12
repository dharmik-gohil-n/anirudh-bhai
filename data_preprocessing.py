import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df = df.fillna(0)

    numeric_cols = ['retail_sales', 'retail_transfers', 'warehouse_sales']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)

    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

    return df