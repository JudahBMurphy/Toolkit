def indent(spaces):
    indent = ' ' * spaces
    return indent

# print a prompt for user input 
def input_prompt():
	return input('==> ')

# prompts user input and check if it is a valid int and contained in selection list
def return_user_input_from_selection(list):
	while True:
		user_input = input_prompt()
		if user_input == '0':
			print('Goodbye')
			break
		elif user_input.isnumeric() == True:
			user_input = int(user_input)
			if (user_input - 1) < len(list):
				return user_input
			else:
				print('Not a valid selection. Try again.')
		else:
			print('Not a valid selection. Try again.')

# iterates through list and prints list corresponding to a number
def display_list_selection(list):
	iterator = 0
	while iterator < len(list):
		print(f'{indent(4)}{iterator + 1}. {list[iterator]}')
		iterator += 1
	print(f'{indent(4)}0. End program')