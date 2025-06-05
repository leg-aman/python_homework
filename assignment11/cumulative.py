
# Task 2: A Line Plot with Pandas
import sqlite3
from matplotlib import pyplot as plt
import pandas as pd
conn = sqlite3.connect('../db/lesson.db')
query = '''
SELECT 
    o.order_id,
    SUM(p.price * li.quantity) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
'''
df = pd.read_sql_query(query, conn)

conn.close()
def cumulative(row):
    totals_above = df['total_price'][0:row.name + 1]
    return totals_above.sum()

df['cumulative_cumsum'] = df['total_price'].cumsum()
# print(df)

# Line plot
df.plot(x="order_id", y="cumulative_cumsum", kind="line", title="Cumulative Revenue", color='green', marker='o', markersize=1, linewidth=0.1)
plt.show()