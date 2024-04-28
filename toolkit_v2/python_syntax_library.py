import json
import nav_functions

with open('python_syntax_messages.json','r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def display_python_syntax_library(list):
    for item in list:
        print(f'{nav_functions.indent(4)}{item}:')

def display_function_message(user_input, list):
    selected_item = str(list[user_input - 1])
#    print(f'{selected_item}')
    print(f'{nav_functions.indent(4)}{selected_item}:')
    split_message = messages(selected_item).split("Description:")
    print(f'{nav_functions.indent(8)}{split_message[0]}')
    print(f'{nav_functions.indent(8)}Description:{split_message[1]}')

def display_python_syntax(selection, collection, label_str):
        try:
            if isinstance(collection, list):
                selected_item = collection[selection - 1]
                if messages(selected_item) == "":
                    print(f"{nav_functions.indent(4)}{selection}: No entry for this topic yet.")
                else:
                    print(f'{nav_functions.indent(4)}{selected_item}')
                    print(f'{nav_functions.indent(8)}Description: {messages(selected_item)}')

            elif isinstance(collection, dict):
                if messages(selection) == "":
                    print(f"{nav_functions.indent(4)}{selection}: No entry for this topic yet.")
                elif isinstance(collection[selection], list):
                    #print_value = f'{label_str}: '
                    #for item in collection[selection]:
                        #print_value = print_value + item + " "
                    #print(f'{nav_functions.indent(8)}{print_value}')
                    print(f'{nav_functions.indent(4)}{selection}')
                    print(f'{nav_functions.indent(8)}{label_str}: {collection[selection][0]}')
                    if messages(selection) != "":
                        print(f'{nav_functions.indent(8)}Description: {messages(selection)}')
                    print(f'{nav_functions.indent(8)}Documentation: {collection[selection][1]}')
                    print("Great Success!")
                else:
                    #print(f'Test {selection.values()}')
                    print(f'{nav_functions.indent(4)}{selection}')
                    print(f'{nav_functions.indent(8)}{label_str}: {collection[selection]}')
                    print(f'{nav_functions.indent(8)}Description: {messages(selection)}')
        except:
            print(f"{nav_functions.indent(4)}{selection}: No entry found.")

syntax_categories = [
    "Operators",
    "Built In Functions",
    "String Methods",
    "List Methods",
    "Dictionary Methods"
]

operator_dict = {
    "Artithmetic": ["+, -, *, /, //, %, **", ],
    "String/List": ['+'],
    "Comparison": [
        "==, !=, <, >, <=, >=",
        "https://docs.python.org/3/library/stdtypes.html#comparisons"
        ],
    "Logical": ['and', 'or', 'not'],
    "Identity": ['is', 'is not']
}


built_in_functions_dict = {
    '.abs()': ["int, float","https://docs.python.org/3/library/functions.html#abs"],
    '.all()': "iterable",
    '.any()': "iterable",
    '.bool()': "any",
    '.callable()': "object",
    '.divmod()': "x, y",
    '.enumerate()': "iterable, start = index",
    '.float()': "number",
    '.frozenset()': "iterable = set()",
    '.hash()': "object",
    '.id()': "object",
    '.input()': "prompt",
    '.int()': "number",
    '.isinstance()': "object",
    '.issubclass()': "class, classinfo",
    '.iter()': "object",
    '.len()': "anything",
    '.list()': "iterable",
    '.map()': "function, iterable",
    '.max()': "iterable",
    '.min()': "iterable",
    '.next()': "iterator",
    '.open()': "file",
    '.pow()': "base, exp, mod=None",
    '.print()': "anything",
    '.range()': "start index, stop index",
    '.reversed()': "sequence",
    '.round()': "number",
    '.sorted()': "iterable",
    '.str()': "object",
    '.sum()': "iterable",
    '.tuple()': "iterable",
    '.type()': "object",
    '.zip()': "iterable1, iterable2"
}

string_methods = [
    'capitalize',
    'swapcase',
    'upper',
    'lower',
    'isalpha',
    'isdigit',
    'isalnum',
    'islower',
    'isupper',
    'isspace',
    'split',
    'rstrip',
    'lstrip',
    'replace',
    'split',
    'find',
    'rfind'
]

list_methods = [
    "len(list)",
    "list.append()",
    "list.pop()",
    "list.reverse()"
]

dict_methods = [
    "dict.keys()",
    "dict.values()",
    "dict.items()",
    "dict.get()"
]