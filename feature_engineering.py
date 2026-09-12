def create_features(df):
    df['month_name'] = df['date'].dt.month_name()
    df['quarter'] = df['date'].dt.quarter

    def get_season(month):
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        else:
            return "Fall"

    df['season'] = df['month'].apply(get_season)

    df['total_sales'] = df['retail_sales'] + df['warehouse_sales']

    return df