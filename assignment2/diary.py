user_input = str(input("what happened today?\n"))
while user_input != "done for now":
    try:
        with open('diary.txt','a') as file:
            file.write(user_input + "\n")
        user_input = str(input("what else?\n"))
    except Exception as e:
        print(f"An error occurred writting to the file: {e}")