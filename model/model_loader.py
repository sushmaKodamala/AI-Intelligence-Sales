import joblib

def load_model():

    model = joblib.load(
        "model/sales_forecast_model.pkl"
    )

    return model