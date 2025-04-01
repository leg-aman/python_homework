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
print("\n******Task2 employees [employee.csv]  *****\n",task2_employees)

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
print("\n******json employees*****\n",json_employees)

# Combine DataFrames:
more_employees = pd.concat([task2_employees,json_employees], ignore_index=True)
print("\n******More employees*****\n",more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# Use the head() method:
first_three = more_employees.head(3)
print("\n******First three rows*****\n", first_three)

# Use the tail() method:
last_two = more_employees.tail(2)
print("\n******Last two rows*****\n", last_two)

# Get the shape of a DataFrame
employee_shape = more_employees.shape
print("\n******Shape of more_employee*****\n", employee_shape)

# Use the info() method:
print("\n******Info more_employee dataframe*****\n", more_employees.info)

# Task 4: Data Cleaning

# Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')
print("\n***** Dirty Data [csv] *****\n",dirty_data)

clean_data = dirty_data.copy()
clean_data.drop_duplicates(inplace=True)

# Remove any duplicate rows from the DataFrame
print("\n***** Clean Data [Drop Duplicates] *****\n",dirty_data)

# Convert Age to numeric and handle missing values
clean_data['Age'] = clean_data['Age'].replace(['unknown', 'NaN', 'n/a'], pd.NA)
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'NaN', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

mean_age = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(mean_age)
median_salary = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)
clean_data['Department'] = clean_data['Department'].str.upper()
# Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'],errors='coerce')

print("\n***** Clean Data [csv] *****\n",clean_data)