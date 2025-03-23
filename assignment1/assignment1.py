# Write your code here.

# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

# Task 3: Calculator
def calc(arg1,arg2,arg3="multiply"):
    if type(arg1) == str or type(arg2) == str:
        return "You can't multiply those values!"
    if arg3 == "add":
        return arg1 + arg2
    if arg3 == "subtract":
        return arg1 - arg2
    if arg3 == "multiply":
        return arg1 * arg2
    if arg3 == "divide":
        if arg2 == 0:
            return "You can't divide by 0!"
        elif type(arg1) == int and type(arg2) == int:
            return arg1//arg2
        else:
            return arg1 / arg2
    if arg3 == "modulo":
        return arg1 % arg2
    if arg3 == "power":
        return arg1 ** arg2
    
# Task 4: Data Type Conversion
def data_type_conversion(arg1,arg2):
    if arg2 == "int":
        try:
            int(arg1)
        except ValueError:
            return f"You can't convert {str(arg1)} into a {str(arg2)}."
        else:
            return int(arg1)
    if arg2 == "float":
        try:
            float(arg1)
        except ValueError:
            return f"You can't convert {str(arg1)} into a {str(arg2)}."
        else:
            return float(arg1)
    if arg2 == "str":
        return str(arg1)
    
# Task 5: Grading System, Using *args
def grade(*args):
    try:
        result = sum(args)//len(args)    
    except TypeError:
        return "Invalid data was provided."
    else:
        result = sum(args)//len(args)
        if result >= 90:
            return "A"
        elif result >= 80 or result <= 89:
            return "B"
        elif result >= 70 or result <= 79:
            return "C"
        elif result >= 60 or result <= 69:
            return "D"
        elif result <60:
            return "F"
        
# Task 6: Use a For Loop with a Range
def repeat(word, count):
    repeatedWord = ''
    for i in range(count):
        repeatedWord += word
    return repeatedWord
# Task 7: Student Scores, Using **kwargs
def student_scores(*args,**kwargs):
    if "best" in args:
        for key, value in kwargs.items():
            if value == max(kwargs.values()):
                return key
    elif "mean" in args:
        return sum(list(kwargs.values()))/len(kwargs.values()) 
    
# Task 8: Titleize, with String and List Operations
def titleize(words):
    word_list = words.split()
    book_title = ""
    for i,word in enumerate(word_list):
        if i == 0 or i == len(word_list) - 1:
            book_title += word[0].capitalize() + word[1:] + " "
        elif word in "a on an the of and is in":
            book_title += word + " "
        else:
             book_title += word[0].capitalize() + word[1:] + " "
    return book_title.strip()

# Task 9: Hangman, with more String Operations
def hangman(secret_word,guessed_word):
    guessed_letter = ''
    for i in secret_word:
        if i in guessed_word:
            guessed_letter += i
        else:
            guessed_letter += "_"
    return guessed_letter

def pig_latin(sentence):
    def convert_word(word):
        if word[0] in 'aeiou':
            return word + 'ay'
    
        if word[:2] == 'qu':
            return word[2:] + 'qu' + 'ay'
        
        for i in range(len(word)):
            if word[i] in 'aeiou':
                new_word = word[i:] + word[:i] 
                if new_word[:2] == 'qu':
                    return new_word[2:] + 'qu' + 'ay'
                return new_word + 'ay'
    words = sentence.split()
    pig_latin_words = [convert_word(word) for word in words]
    return ' '.join(pig_latin_words)









