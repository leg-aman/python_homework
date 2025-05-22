# Task 1: Diary
import traceback
try:
    user_input = str(input("what happened today?\n"))
    while user_input != "done for now":
        try:
            with open('diary.txt','a') as file:
                file.write(user_input + "\n")
            user_input = str(input("what else?\n"))
        except Exception as e:
            print(f"An error occurred writting to the file: {e}")
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")