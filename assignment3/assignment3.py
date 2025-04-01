# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
import pandas as pd

# Create a DataFrame from a dictionary:
data ={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# Add a new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# Modify an existing column:
task1_older = task1_with_salary.copy()
for key in task1_older:
    if key == 'Age':
        task1_older[key] += 1
print(task1_older)

# Save the DataFrame as a CSV file:
task1_older.to_csv("employees.csv", index=False)

# Task 2: Loading Data from CSV and JSON

# Read data from a CSV file:
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

# Read data from a JSON file:
json_data = {
    'Name':['Eve', 'Frank'],
    'Age':[28,40],
    'City':['Miami','Seattle'],
    'Salary':[60000,95000]
}
json_data_df = pd.DataFrame(json_data)
json_data_df.to_json("additional_employees.json",index=False)
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# Combine DataFrames:
more_employees = pd.concat([task2_employees,json_employees], ignore_index=True)
print(more_employees)