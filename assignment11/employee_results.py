import pandas as pd
import sqlite3
# loading the employee results from the database
def load_employee_results():
    conn = sqlite3.connect('../db/lesson.db')
    query = "SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id"
    employee_results = pd.read_sql_query(query, conn)
    conn.close()
    return employee_results
# print(load_employee_results())

