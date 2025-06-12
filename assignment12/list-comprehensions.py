import pandas as pd
employee_df = pd.read_csv("../csv/employees.csv")
employee_names = ["{} {}".format(row['first_name'], row['last_name']) for _, row in employee_df.iterrows()]
print("List of Employees:\n", employee_names)
names_with_letter_e = [name for name in employee_names if 'e' in name.lower()]
print("Employees with 'e' in their names:\n", names_with_letter_e)
