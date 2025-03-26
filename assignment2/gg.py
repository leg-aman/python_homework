import csv
import traceback

# Task 2: Read a CSV File
def read_employees ():
    column_header = {}
    list_of_rows = []
    try:
        with open('../csv/employees.csv','r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            column_header['fields'] = header
            for row in reader:
                list_of_rows.append(row)
            column_header['rows'] = list_of_rows
    except Exception as e:
        handle_exception(e)
    return column_header
employees = read_employees()
# print(employees)

# Task 3: Find the Column Index
def column_index(args):
        return employees["fields"].index(str(args))
employee_id_column = column_index("employee_id")

# Task 4: Find the Employee First Name
def first_name(row_num):
    employee_first_name_column = column_index("first_name")
    return employees['rows'][row_num][employee_first_name_column]

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
       return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees['rows'].sort(key=lambda row: row[last_name_index])
    # print(employees['rows'])
sort_by_last_name()
# Task 8: Create a dict for an Employee
def employee_dict(args):
     sort_by_last_name()
     zipped = dict(zip(employees['fields'],args))
     return (zipped["last_name"])
print(employee_dict(employees['rows'][0]))

def handle_exception(e):
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")