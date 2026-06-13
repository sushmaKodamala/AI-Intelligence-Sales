import pandas as pd
from database_connection import get_connection

def insert_sales(df):

    conn = get_connection()

    df.to_sql(
        "sales",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()

def fetch_sales():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM sales",
        conn
    )

    conn.close()

    return df