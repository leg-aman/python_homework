#  Advanced SQL and Database Integration
import sqlite3
import os

find = os.path.join(os.path.dirname(__file__), "../db/lesson.db")

# Connect to the database

try:
    # Connect to the SQLite database (or create it if it doesn't exist)
    with sqlite3.connect(find) as conn:
        print("Database connected successfully!")
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = 1")

# Tak 1: Complex JOINs with Aggregation
        cursor.execute("""
                SELECT orders.order_id AS ordered_id,
                    SUM(products.price * line_items.quantity) AS total_order_price 
                FROM orders 
                JOIN line_items ON orders.order_id = line_items.order_id 
                JOIN products ON line_items.product_id = products.product_id 
                GROUP BY orders.order_id 
                ORDER BY orders.order_id LIMIT 5
                """)
        results = cursor.fetchall()
        print("Results of the complex JOINs with Aggregation:")
        for row in results:
            print(row)

# Task 2: Understanding Subqueries
        cursor.execute("""
            SELECT c.customer_name, AVG(order_total.total_price) AS average_total_price
            FROM customers c
            LEFT JOIN (
                SELECT o.customer_id AS customer_id_b,
                       SUM( li.quantity * p.price ) AS total_price
                FROM orders o
                JOIN line_items li ON o.order_id = li.order_id
                JOIN products p ON li.product_id = p.product_id
                GROUP BY o.customer_id
            ) AS order_total
            ON c.customer_id = order_total.customer_id_b
            GROUP BY c.customer_id;
        """)
        res = cursor.fetchall()
        print("Results of the subquery:")
        for row in res:
            print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")