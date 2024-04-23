import json
import nav_functions

with open('python_syntax_messages.json','r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def display_python_syntax_library(list):
    for item in list:
        print(f'{nav_functions.indent(4)}{item}:')

def display_list_item_message(user_input, list):
    selected_item = str(list[user_input - 1])
#    print(f'{selected_item}')
    print(f'{nav_functions.indent(4)}{selected_item}:')
    split_message = messages(selected_item).split("Description:")
    print(f'{nav_functions.indent(8)}{split_message[0]}')
    print(f'{nav_functions.indent(8)}Description:{split_message[1]}')

syntax_categories = [
    "Built In Functions",
    "String Methods",
    "List Methods",
    "Dictionary Methods"
]

built_in_functions = [
    '.abs()',
    '.all()',
    '.any()',
    '.bool()',
    '.callable()',
    '.divmod()',
    '.enumerate()',
    '.float()',
    '.frozenset()',
    '.hash()',
    '.id()',
    '.input()',
    '.int()',
    '.isinstance()',
    '.issubclass()',
    '.iter()',
    '.len()',
    '.list()',
    '.map()',
    '.max()',
    '.min()',
    '.next()',
    '.open()',
    '.pow()',
    '.print()',
    '.range()',
    '.reversed()',
    '.round()',
    '.sorted()',
    '.str()',
    '.sum()',
    '.tuple()',
    '.type()',
    '.zip()',
]