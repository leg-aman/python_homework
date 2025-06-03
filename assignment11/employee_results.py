import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
# loading the employee results from the database
def load_employee_results():
    conn = sqlite3.connect('../db/lesson.db')
    query = "SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id"
# convert the query results into a pandas DataFrame
    employee_results = pd.read_sql_query(query, conn)
    conn.close()
    return employee_results
# print(load_employee_results())

emp_res = load_employee_results()
# bar chart of employee results
emp_res.plot(x="last_name", y="revenue", color=['#8cc5e3', '#1a80bb'], kind="bar", title="Employee Revenue Results")
plt.show()