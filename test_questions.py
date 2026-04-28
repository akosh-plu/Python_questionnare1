# test_questions.py
# DO NOT SHARE THIS FILE WITH STUDENTS

# Updated test_questions.py for the full curriculum
QUESTIONS = [
    # --- BASICS & TYPES ---
    {"id": 1, "topic": "variables", "question": "Which of these is an invalid variable name?", "type": "multiple_choice", "options": ["A) user_name", "B) 2nd_user", "C) _total", "D) price2"], "correct": "B"},
    {"id": 2, "topic": "integers", "question": "What is the result of 10 // 3 in Python?", "type": "short_answer", "correct": "3"},
    {"id": 3, "topic": "strings", "question": "What method is used to remove whitespace from both ends of a string?", "type": "short_answer", "correct": "strip"},
    
    # --- CONTROL FLOW ---
    {"id": 4, "topic": "if_else", "question": "Which keyword is used to check multiple conditions after an 'if'?", "type": "short_answer", "correct": "elif"},
    {"id": 5, "topic": "cycles", "question": "Which loop is best used when you know exactly how many times you need to iterate?", "type": "multiple_choice", "options": ["A) while", "B) if", "C) for", "D) repeat"], "correct": "C"},
    {"id": 6, "topic": "cycles", "question": "What statement is used to exit a loop immediately?", "type": "short_answer", "correct": "break"},

    # --- DATA STRUCTURES ---
    {"id": 7, "topic": "lists", "question": "How do you access the last element of a list named 'my_list'?", "type": "multiple_choice", "options": ["A) my_list[0]", "B) my_list[last]", "C) my_list[-1]", "D) my_list[1]"], "correct": "C"},
    {"id": 8, "topic": "tuples", "question": "True or False: Tuples are mutable (can be changed after creation).", "type": "short_answer", "correct": "False"},
    {"id": 9, "topic": "dictionaries", "question": "What do you call the 'key:value' pairs in a Python dictionary?", "type": "short_answer", "correct": "items"},
    {"id": 10, "topic": "dictionaries", "question": "Which method returns all the keys in a dictionary?", "type": "multiple_choice", "options": ["A) get_keys()", "B) keys()", "C) all()", "D) list_keys()"], "correct": "B"},

    # --- FUNCTIONS ---
    {"id": 11, "topic": "functions", "question": "What keyword is used to create a function?", "type": "short_answer", "correct": "def"},
    {"id": 12, "topic": "functions", "question": "What do you call the values passed into a function inside the parentheses?", "type": "short_answer", "correct": "arguments"},

    # --- MODULES (Random, Time, sys) ---
    {"id": 13, "topic": "random", "question": "Which function in the random module returns a random integer between two numbers (inclusive)?", "type": "short_answer", "correct": "randint"},
    {"id": 14, "topic": "time", "question": "Which function is used to pause the execution of a program for a few seconds?", "type": "multiple_choice", "options": ["A) time.wait()", "B) time.pause()", "C) time.sleep()", "D) time.stop()"], "correct": "C"},
    {"id": 15, "topic": "sys", "question": "Which sys attribute is used to get a list of command-line arguments passed to a script?", "type": "short_answer", "correct": "argv"},

    # --- ADVANCED TOPICS ---
    {"id": 16, "topic": "zip", "question": "What is the output of: list(zip([1,2], ['a', 'b']))?", "type": "multiple_choice", "options": ["A) [1, 2, 'a', 'b']", "B) [(1, 'a'), (2, 'b')]", "C) [[1, 'a'], [2, 'b']]", "D) {(1, 'a'), (2, 'b')}"], "correct": "B"},
    {"id": 17, "topic": "regex", "question": "In Regular Expressions, which character matches 'any single character except a newline'?", "type": "short_answer", "correct": "."},
    {"id": 18, "topic": "files", "question": "Which mode is used to open a file for WRITING and creates the file if it doesn't exist?", "type": "short_answer", "correct": "w"},

    # --- TURTLE & OOP ---
    {"id": 19, "topic": "turtle", "question": "Which command moves the Turtle forward?", "type": "multiple_choice", "options": ["A) fd()", "B) move()", "0) go()", "D) step()"], "correct": "A"},
    {"id": 20, "topic": "turtle", "question": "What command stops the Turtle window from closing immediately after finishing?", "type": "short_answer", "correct": "done"},
    {"id": 21, "topic": "oop", "question": "In a class, what is the special name for the constructor method?", "type": "short_answer", "correct": "__init__"},
    {"id": 22, "topic": "oop", "question": "What does the 'self' parameter refer to in a class method?", "type": "multiple_choice", "options": ["A) The class itself", "B) The parent class", "C) The specific instance of the object", "D) The global scope"], "correct": "C"},
    {"id": 23, "topic": "oop", "question": "What is it called when a class takes methods and attributes from another class?", "type": "short_answer", "correct": "inheritance"},

    # --- FINAL REVIEW ---
    {"id": 24, "topic": "data_types", "question": "What type of data is: {'name': 'Python', 'version': 3}?", "type": "short_answer", "correct": "dict"},
    {"id": 25, "topic": "general", "question": "What is the name of the integrated development environment (IDE) we used in class?", "type": "short_answer", "correct": "PyCharm"}
]


def check_answer(question_id, user_answer):
    """Check if the user's answer is correct"""
    question = next((q for q in QUESTIONS if q["id"] == question_id), None)
    if not question:
        return False
    
    if question["type"] == "short_answer":
        return user_answer.strip().lower() == question["correct"].lower()
    else:
        return user_answer.strip().upper() == question["correct"].upper()

def get_question_for_display(question_id):
    """Get question without the answer"""
    question = next((q for q in QUESTIONS if q["id"] == question_id), None)
    if not question:
        return None
    
    display_q = {
        "id": question["id"],
        "topic": question["topic"],
        "question": question["question"],
        "type": question["type"]
    }
    
    if "options" in question:
        display_q["options"] = question["options"]
    
    return display_q
