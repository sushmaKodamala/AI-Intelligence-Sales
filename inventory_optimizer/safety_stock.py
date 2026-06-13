def calculate_safety_stock(
        max_daily_sales,
        avg_daily_sales,
        lead_time):

    return (
        (max_daily_sales * lead_time)
        -
        (avg_daily_sales * lead_time)
    )