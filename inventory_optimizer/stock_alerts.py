def stock_alert(current_stock,
                reorder_point):

    if current_stock <= reorder_point:
        return "REORDER REQUIRED"

    return "SUFFICIENT STOCK"