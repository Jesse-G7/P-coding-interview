import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = """
    -- WRITE YOUR SQL HERE
    """

    SELECT sku
    FROM Order_Items o
    WHERE SUM(o.quantity)>1
    GROUND BY sku;
    
    cursor.execute(query)
    return cursor.fetchall()
