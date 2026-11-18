import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    -- WRITE YOUR SQL HERE
    """
    SELECT SUM(o.price * o.quantity) AS totalspend
    FROM Order_Items order
    JOIN Orders o ON order.order_id = o.order_id
    JOIN Customers c ON order.customer_id = c.customer_id
    GROUP BY c.Name;


    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
