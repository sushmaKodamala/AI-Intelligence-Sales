import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("dataset/sales_data.csv")

X = df[["sales"]]
y = df["revenue"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(
    model,
    "model/sales_forecast_model.pkl"
)

print("Model Saved Successfully")