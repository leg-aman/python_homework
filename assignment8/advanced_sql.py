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
# Task 3: An Insert Transaction Based on Data
# Problem Statement:

# You want to create a new order for the customer named Perez and Sons.  The employee creating the order is Miranda Harris.  The customer wants 10 of each of the 5 least expensive products.  You first need to do a SELECT statement to retrieve the customer_id, another to retrieve the product_ids of the 5 least expensive products, and another to retrieve the employee_id.  Then, you create the order record and the 5 line_item records comprising the order.  You have to use the customer_id, employee_id, and product_id values you obtained from the SELECT statements. You have to use the order_id for the order record you created in the line_items records. The inserts must occur within the scope of one transaction. Then, using a SELECT with a JOIN, print out the list of line_item_ids for the order along with the quantity and product name for each.

# You want to make sure that the foreign keys in the INSERT statements are valid.  So, add this line to your script, right after the database connection:

# conn.execute("PRAGMA foreign_keys = 1")
# In general, when creating a record, you don't want to specify the primary key.  So leave that column name off your insert statements.  SQLite will assign a unique primary key for you.  But, you need the order_id for the order record you insert to be able to insert line_item records for that order.  You can have this value returned by adding the following clause to the INSERT statement for the order:

# RETURNING order_id

        # Task 3: An Insert Transaction Based on Data
        cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
        customer_id = cursor.fetchone()[0]

        cursor.execute("SELECT employee_id FROM employees WHERE employees.first_name = 'Miranda Harris'")
        employee_id = cursor.fetchone()[0]

        cursor.execute("""
            SELECT product_id FROM products 
            ORDER BY price ASC 
            LIMIT 5
        """)
        product_ids = [row[0] for row in cursor.fetchall()]

        # Start a transaction
        conn.execute("BEGIN;")

        try:
            # Insert the order record and get the order_id
            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id) 
                VALUES (?, ?)
                RETURNING order_id;
            """, (customer_id, employee_id))
            order_id = cursor.fetchone()[0]

            # Insert line_item records for each product
            for product_id in product_ids:
                cursor.execute("""
                    INSERT INTO line_items (order_id, product_id, quantity) 
                    VALUES (?, ?, ?);
                """, (order_id, product_id, 10))
            # Commit the transaction    
            conn.commit()
        except sqlite3.Error as e:
            # Rollback the transaction in case of error
            conn.rollback()
            print(f"Transaction failed: {e}")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")