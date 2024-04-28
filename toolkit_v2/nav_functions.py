import json

def load_json(file_name):
    with open(file_name,'r') as file:
        MESSAGES = json.load(file)
    return MESSAGES

def messages(file_address, message):
    return file_address[message]

def indent(spaces):
    indent = ' ' * spaces
    return indent

# print a prompt for user input 
def input_prompt():
    return input('==> ')

# prompts user input and check if it is a valid int and contained in selection list
def return_user_input_from_selection(selection):
    while True:
        user_input = input_prompt()
        if user_input == '0':
            print('Goodbye')
            break
        elif user_input.isnumeric() == True:
            user_input = int(user_input)
            if isinstance(selection, list):
                if (user_input - 1) < len(selection):
                    return user_input
                else:
                    print('Not a valid selection. Try again.')
            elif isinstance(selection, dict):
                if (user_input - 1) < len(selection.keys()):
                    iterator = 0
                    for key in selection:
                        iterator += 1
                        if iterator == user_input:
                            return key
                else:
                    print('Not a valid selection. Try again.')
        else:
            print('Not a valid selection. Try again.')

# iterates through a list/dictionary and prints items/keys corresponding to a number
def display_selection(collection, padding):
    iterator = 0
    if isinstance(collection, list):
        while iterator < len(collection):
            print(f'{indent(padding)}{iterator + 1}. {collection[iterator]}')
            iterator += 1
    elif isinstance(collection, dict):
        for key in collection.keys():
            print(f'{indent(padding)}{iterator + 1}. {key}')
            iterator += 1
    print(f'{indent(padding)}0. End program')

#def display_syntax_library():

def display_definition(list, selection, message_library):
    json_file = load_json(message_library)
    selected_item = list[selection - 1]
    try:
        if messages(json_file, selected_item) == "":
            print(f"{indent(4)}{selected_item}: No entry for this topic yet.")
        else:
            print(f'{indent(4)}{selected_item}: {messages(json_file, selected_item)}')
    except:
        print(f"{indent(4)}{selected_item}: No entry for this topic yet. Brutal.")

