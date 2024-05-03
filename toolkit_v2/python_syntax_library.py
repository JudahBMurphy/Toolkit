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
    "Artithmetic": {
        "Operators": "+, -, *, /, //, %, **"
        },
    "String/List": {
        "Operators": "+"
        },
    "Comparison": {
        "Operators": "==, !=, <, >, <=, >=",
        "Documentaion": "https://docs.python.org/3/library/stdtypes.html#comparisons"
        },
    "Logical": {
        "Operators": "and, or, not",
        },
    "Identity": {
        "Operators": "is, is not"
        }
}


built_in_functions_dict = {
    '.abs()': {
        'Arguments': 'int, float',
        'Documentation': 'https://docs.python.org/3/library/functions.html#abs',
        'Example': ''
        },
    '.all()': {
        'Arguments': 'iterable',
        'Documentation': 'https://docs.python.org/3/library/functions.html#all',
        'Example': ''
        },
    '.any()': {
        'Arguments': "iterable",
        'Documentation': 'https://docs.python.org/3/library/functions.html#any',
        'Example': ''
        },
    '.bool()': {
        'Arguments': "any",
        'Documentation': 'https://docs.python.org/3/library/functions.html#bool',
        'Example': ''
        },
    '.callable()': {
        'Arguments': "object",
        'Documentation': 'https://docs.python.org/3/library/functions.html#callable',
        'Example': ''
        },
    '.divmod()': {
        'Arguments': "x, y",
        'Documentation': 'https://docs.python.org/3/library/functions.html#divmod',
        'Example': ''
        },
    '.enumerate()': {
        'Arguements': "iterable, start = index",
        'Documentation': 'https://docs.python.org/3/library/functions.html#enumerate',
        'Example': ''
        },
    '.float()': {
        'Arguments': "number",
        'Documentation': 'https://docs.python.org/3/library/functions.html#float',
        'Example': ''
        },
    '.frozenset()': {
        'Arguements': "iterable = set()",
        'Documentation': 'https://docs.python.org/3/library/functions.html#func-frozenset',
        'Example': ''
        },
    '.hash()': {
        'Arguements': "object",
        'Documentation': 'https://docs.python.org/3/library/functions.html#hash',
        'Example': ''
        },
    '.id()': {
        'Arguements': "object",
        'Documentation': 'https://docs.python.org/3/library/functions.html#id',
        'Example': ''
        },
    '.input()': {
        'Arguements': "prompt",
        'Documentation': 'https://docs.python.org/3/library/functions.html#input',
        'Example': ''
        },
    '.int()': {
        'Arguements': "number",
        'Documentation': 'https://docs.python.org/3/library/functions.html#input',
        'Example': ''
        },
    '.isinstance()': {
        'Arguements': "object",
        'Documentation': 'https://docs.python.org/3/library/functions.html#isinstance',
        'Example': ''
        },
    '.issubclass()': {
        'Arguements': "class, classinfo",
        'Documentation': 'https://docs.python.org/3/library/functions.html#issubclass',
        'Example': ''
        },
    '.iter()': {
        'Arguements': "object",
        'Documentation': 'https://docs.python.org/3/library/functions.html#iter',
        'Example': ''
        },
    '.len()': {
        'Arguements': "anything",
        'Documentation': 'https://docs.python.org/3/library/functions.html#len',
        'Example': ''
        },
    '.list()': {
        'Arguements': "iterable",
        'Documentation': 'https://docs.python.org/3/library/functions.html#func-list',
        'Example': ''
        },
    '.map()': {
        'Arguements': "function, iterable",
        'Documentation': 'https://docs.python.org/3/library/functions.html#map',
        'Example': ''
        },
    '.max()': {
        'Arguements': "iterable",
        'Documentation': 'https://docs.python.org/3/library/functions.html#max',
        'Example': ''
        },
    '.min()': {
        'Arguements': "iterable",
        'Documentation': 'https://docs.python.org/3/library/functions.html#min',
        'Example': ''
        },
    '.next()': {
        'Arguements': "iterator",
        'Documentation': 'https://docs.python.org/3/library/functions.html#next',
        'Example': ''
        },
    '.open()': {
        'Arguements': "file",
        'Documentation': 'https://docs.python.org/3/library/functions.html#open',
        'Example': ''
        },
    '.pow()': {
        'Arguements': "base, exp, mod=None",
        'Documentation': 'https://docs.python.org/3/library/functions.html#pow',
        'Example': ''
        },
    '.print()': {
        'Arguements': "anything",
        'Documentation': 'https://docs.python.org/3/library/functions.html#print',
        'Example': ''
        },
    '.range()': {
        'Arguements': "start index, stop index",
        'Documentation': 'https://docs.python.org/3/library/functions.html#func-range',
        'Example': ''
        },
    '.reversed()': {
        'Arguements': "sequence",
        'Documentation': 'https://docs.python.org/3/library/functions.html#reversed',
        'Example': ''
        },
    '.round()': {
        'Arguements': "number",
        'Documentation': 'https://docs.python.org/3/library/functions.html#round',
        'Example': ''
        },
    '.sorted()': {
        'Arguements': "iterable",
        'Documentation': 'https://docs.python.org/3/library/functions.html#sorted',
        'Example': ''
        },
    '.str()': {
        'Arguements': "object",
        'Documentation': 'https://docs.python.org/3/library/functions.html#func-str',
        'Example': ''
        },
    '.sum()': {
        'Arguements': "iterable",
        'Documentation': 'https://docs.python.org/3/library/functions.html#sum',
        'Example': ''
        },
    '.tuple()': {
        'Arguements': "iterable",
        'Documentation': 'https://docs.python.org/3/library/functions.html#func-tuple',
        'Example': ''
        },
    '.type()': {
        'Arguements': "object",
        'Documentation': 'https://docs.python.org/3/library/functions.html#type',
        'Example': ''
        },
    '.zip()': {
        'Arguements': "iterable1, iterable2",
        'Documentation': 'https://docs.python.org/3/library/functions.html#zip',
        'Example': ''
        }
}

string_methods = {
    'capitalize': {
        'Syntax': 'str.capitalize()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.capitalize',
        'Example': '''
            string = "Follow the White Rabbit."
            print(string.capitalize())
            #Follow the white rabbit.'''
        },
    'swapcase': {
        'Syntax': 'str.swapcase()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.swapcase',
        'Example': '''
            string = "Follow the White Rabbit."
            print(string.swapcase())
            #fOLLOW THE wHITE rABBIT
            '''
        },
    'upper': {
        'Syntax': 'str.upper()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.upper',
        'Example': '''
            string = "Follow the White Rabbit."
            print(string.upper())
            #FOLLOW THE WHITE RABBIT
            '''
        },
    'lower': {
        'Syntax': 'str.lower()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.lower',
        'Example': '''
            string = "Follow the White Rabbit."
            print(string.lower())
            #follow the white rabbit
            '''
        },
    'isalpha': {
        'Syntax': 'str.isalpha()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.isalpha',
        'Example': '''
            string = "Follow the White Rabbit."
            print(string.isalpha())
            #False
            '''
        },
    'isdigit': {
        'Syntax': 'str.isdigit()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.isdigit',
        'Example': '''
            string = "42"
            print(string.isdigit())
            #True
            '''
        },
    'isalnum': {
        'Syntax': 'str.isalnum()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.isalnum',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.isalnum())
            #False
            '''
        },
    'islower': {
        'Syntax': 'str.islower()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.islower',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.islower())
            #False
            '''
        },
    'isupper': {
        'Syntax': 'str.isupper()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.isupper',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.isupper())
            #False
            '''
        },
    'isspace': {
        'Syntax': 'str.isspace()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.isspace',
        'Example': '''
            string = " "
            print(string.isspace())
            #true
            '''
        },
    'strip': {
        'Syntax': 'str.strip([chars])',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.strip',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.strip('Foit'))
            #llow the White Rabb
            '''
        },
    'rstrip': {
        'Syntax': 'str.rstrip([chars])',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.rstrip',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.rstrip('Rabbit'))
            #Follow the White
            '''
        },
    'lstrip': {
        'Syntax': 'str.lstrip([chars])',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.rstrip',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.lstrip('Follow the'))
            #White Rabbit
            '''
        },
    'replace': {
        'Syntax': 'str.replace(old, new[, count])',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.replace',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.replace('White Rabbit', 'Golden Path'))
            #Follow the Golden Path
            '''
        },
    'split': {
        'Syntax': 'str.split(sep=None, maxsplit=-1)',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.split',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.split(' '))
            #['Follow', 'the', 'White', 'Rabbit']
            '''
        },
    'find': {
        'Syntax': 'str.find(sub[, start[, end]])',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.find',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.find('b'))
            #19
            '''
        },
    'rfind': {
        'Syntax': 'str.rfind(sub[, start[, end]])',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#str.rfind',
        'Example': '''
            string = "Follow the White Rabbit"
            print(string.rfind('b'))
            #20
            '''
        },
}

list_methods = {
    "len(list)": {
        'Syntax': 'len(s)',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#common-sequence-operations',
        'Example': '''
            my_list = [1, 2, 3]
            print(len(my_list))
            #3
            '''
        },
    "list.append()": {
        'Syntax': 's.append(x)',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types',
        'Example': '''
            my_list = [1, 2, 3]
            my_list.append(4)
            print(my_list)
            #[1, 2, 3, 4]
            '''
        },
    "list.pop()": {
        'Syntax': 's.pop(i)',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types',
        'Example': '''
            my_list = [1, 2, 3]
            new_list = my_list.pop(2)
            print(my_list)
            print(new_list)
            #[1, 2]
            #3
            '''
        },
    "list.reverse()": {
        'Syntax': 's.reverse()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types',
        'Example': '''
            my_list = [1, 2, 3]
            my_list.reverse()
            print(my_list)
            #[3, 2, 1]
            '''
        },
}

dict_methods = {
    "dict.keys()": {
        'Syntax': 'dict.keys()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#dict.keys',
        'Example': '''
            my_dict = {'key_1': 'value_1', 'key_2': 'value_2'}
            print(my_dict.keys())
            #dict_keys(['key_1', 'key_2'])
            '''
        },
    "dict.values()": {
        'Syntax': 'dict.values()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#dict.values',
        'Example': '''
            my_dict = {'key_1': 'value_1', 'key_2': 'value_2'}
            print(my_dict.values())
            #dict_values(['value_1', 'value_2'])
            '''
        },
    "dict.items()": {
        'Syntax': 'dict.items()',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#dict.items',
        'Example': '''
            my_dict = {'key_1': 'value_1', 'key_2': 'value_2'}
            print(my_dict.items())
            #dict_items([('key_1', 'value_1'), ('key_2', 'value_2')])
            '''
        },
    "dict.get()": {
        'Syntax': 'dict.get(key[, default])',
        'Documentation': 'https://docs.python.org/3/library/stdtypes.html#dict.get',
        'Example': '''
            my_dict = {'key_1': 'value_1', 'key_2': 'value_2'}
            print(my_dict.get('key_2'))
            #value_2
            '''
        },
}