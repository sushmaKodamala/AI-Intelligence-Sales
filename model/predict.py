import pandas as pd
from model_loader import load_model

def predict_sales(value):

    model = load_model()

    prediction = model.predict(
        pd.DataFrame([[value]],
        columns=["sales"])
    )

    return prediction[0]