import sqlite3
import pandas as pd

with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print(df)

# connect to a new SQLite database
with sqlite3.connect("../db/school.db") as conn:
    # create the file here, so that it is not pushed to GitHub!
    print("Database created and connected successfully!")

# The "with" statement closes the connection at the end of that block. You could close it explicitly with conn.close(),
# but it this case the "with" statement takes care of that.