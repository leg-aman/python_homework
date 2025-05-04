import sqlite3
import pandas as pd

# Connecting to the database
with sqlite3.connect("../db/lesson.db") as conn:
    # SQL statement to join line_items and products tables and select specific columns
    sql_statement = """SELECT li.line_item_id, li.quantity, li.product_id, p.product_name, p.price
                       FROM line_items li
                       JOIN products p ON li.product_id = p.product_id;"""
    
    # Reading the query result into a DataFrame
    df = pd.read_sql_query(sql_statement, conn)
    
    # Printing the DataFrame to view the result
    print(df)
# print all the columns in the dataframe
print(df.columns)

df['total'] = df['quantity'] * df['price']
print(df.head(5))
