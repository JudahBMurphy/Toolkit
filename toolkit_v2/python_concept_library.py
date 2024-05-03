import json
import nav_functions

with open('python_concept_messages.json','r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def display_python_concept(list, selection):
        selected_item = list[selection - 1]
        try:
            if messages(selected_item) == "":
                print(f"{nav_functions.indent(4)}{selected_item}: No entry for this topic yet.")
            else:
                print(f'{nav_functions.indent(4)}{selected_item}: {messages(selected_item)}')
        except:
            print(f"{nav_functions.indent(4)}{selected_item}: No entry for this topic yet.")

#def return_user_input_from_dict(dict):

macro_categories_dict = {
    "Conventions": [
        "Naming Conventions"
        ],
    "Functions": [
        "Type Coercions",
        "Definitions and Calls",
        "Return Values",
        "Parameters vs. Arguements",
        "Scope",
        "Nested Functions",
        "Output vs. Return Values",
        "Side Effects"
        ],
    "Numbers": [
        "Operators",
        "ValueError",
        "ZeroDivisionError"
        ],
    "Strings": [
        "f-strings"
        ],
    "Boolean": [
        "Truthiness"
        ],
    "Ranges": [
        "Ranges"
        ],
    "Compiler Logic": [
        "Mutability",
        "Expressions",
        "Statements",
        "Shallow vs. Deep Copies"
        ],
    "Variables": [
        "Intialization and Assignment",
        "Scope",
        "Variables As Pointers",
        "Variable Shadowing"
        ],
    "Conditionals and Loops": [
        "if", 
        "while",
        "for"
        ]
}

