import json
import nav_functions

with open('python_concept_messages.json','r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def display_python_concept(list, selection):
        selected_item = list[selection - 1]
        try:
            print(f'{nav_functions.indent(4)}{selected_item}: {messages(selected_item)}')
        except:
            print("No entry for this topic yet.")

#def return_user_input_from_dict(dict):

macro_categories = [
    "Conventions",
    "Functions",
    "Numbers",
    "Strings",
    "Boolean",
    "Ranges",
    "Compiler Logic",
    "Variables",
    "Conditionals and Loops"
]

macro_categories_dict = {
    "Conventions": ["Naming Conventions"],
    "Functions": [
        "Type Coercions",
        "Definitions and calls",
        "Return Values",
        "Parameters vs. Arguements",
        "Nested Functions",
        "Output vs. Return Values",
        "Side Effects"
    ],
    "Numbers": ["Exceptions", "Operators"],
    "Strings": ["f-strings", "String Methods"],
    "Boolean": ["Truthiness"],
    "Ranges": ["Ranges", "List Methods"],
    "Compiler Logic": ["Mutability", "Expressions vs. Statements"],
    "Variables": [
        "Intialization and Assignment",
        "Scope",
        "Variables As Pointers",
        "Variable Shadowing"],
    "Conditionals and Loops": ["if", "while","for"]
}

