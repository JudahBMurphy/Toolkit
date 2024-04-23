import json

#with open('python_syntax_messages.json','r') as file:
#    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

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

# iterates through list and prints list corresponding to a number
def display_list_selection(list, padding):
	iterator = 0
	while iterator < len(list):
		print(f'{indent(padding)}{iterator + 1}. {list[iterator]}')
		iterator += 1
	print(f'{indent(padding)}0. End program')

# iterates through dictionary and prints dict correcponding to a number
def display_dict_selection(dict, padding):
    iterator = 0
    for key in dict.keys():
        print(f'{indent(padding)}{iterator + 1}. {key}')
        iterator += 1
    print(f'{indent(padding)}0. End program')