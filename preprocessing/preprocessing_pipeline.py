from data_cleaning import clean_data
from feature_engineering import create_features

def run_pipeline(df):

    df = clean_data(df)

    df = create_features(df)

    return df