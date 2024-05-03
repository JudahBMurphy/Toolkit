import nav_functions
import toolkit2_git_menu
import toolkit2_terminal
import python_concept_library
import python_syntax_library

def return_list_selection(collection):
	nav_functions.display_selection(collection, 4)
	selection = nav_functions.return_user_input_from_selection(collection)
	return selection


topic_list = ['Terminal', 'Git', 'Python']
options_list = ['Syntax','Concepts']
print('')
print('Welcome to Toolkit. What subject do you need to reference:')
topic_selection = return_list_selection(topic_list)

match topic_selection:
	# Terminal help menu
	case 1:
		terminal_options = [
			'Navigation',
			'Files and Directories',
			'Environment Changes',
			'Permissions'
		]
		print(f'Please select a category for reference material:')
		category_selection = return_list_selection(terminal_options)
		
		match category_selection:
			case 1:
				print('See below reference commands for navigating the terminal:')
				terminal_list = toolkit2_terminal.terminal_nav_commands
				terminal_selection = return_list_selection(terminal_list)
				nav_functions.display_definition(terminal_list, terminal_selection,'toolkit2_terminal_messages.json')
			case 2:
				print('See below reference commands for interacting with files and directories:')
				terminal_list = toolkit2_terminal.terminal_file_dir_commands
				terminal_selection = return_list_selection(terminal_list)
				nav_functions.display_definition(terminal_list, terminal_selection,'toolkit2_terminal_messages.json')
			case 3:
				print('See below reference commands for making changes to the Terminal environment:')
				terminal_list = toolkit2_terminal.terminal_env_commands
				terminal_selection = return_list_selection(terminal_list)
				nav_functions.display_definition(terminal_list, terminal_selection,'toolkit2_terminal_messages.json')
			case 4:
				print('See below explaination of permissions concepts:')
				print(f'{toolkit2_terminal.terminal_permissions}')
				
	# Git help menu		
	case 2:
		print('Please see below for list of git commands:')
		git_list = toolkit2_git_menu.git_commands
		git_selection = return_list_selection(git_list)
		nav_functions.display_definition(git_list, git_selection,'toolkit2_git_messages.json')
	# Python help menu
	case 3:
		python_help_options = ['Syntax Reference','Concept Review']
		print(f'Please select what you need help with:')
		help_selection = return_list_selection(python_help_options)

		match help_selection:
			# Python syntax reference menu
			case 1:
				print('Select from the following categories:')
				syntax_selection = return_list_selection(python_syntax_library.syntax_categories)

				match syntax_selection:
					# Operators
					case 1:
						method_loc = python_syntax_library.operator_dict
						method_selection = return_list_selection(method_loc)
						#python_syntax_library.display_python_syntax(method_selection, method_loc, "Operators")
						nav_functions.display_library_dict(method_loc, method_selection, 'python_syntax_messages.json')
					# Built in functions
					case 2:
						method_loc = python_syntax_library.built_in_functions_dict
						print(f'{nav_functions.indent(4)}Official documentation for built-in functions:')
						print(f'{nav_functions.indent(4)}https://docs.python.org/3/library/functions.html')
						method_selection = return_list_selection(method_loc)
						#python_syntax_library.display_python_syntax(method_selection, method_loc, "Arguments")
						nav_functions.display_library_dict(method_loc, method_selection, 'python_syntax_messages.json')
					# String methods
					case 3:
						method_loc = python_syntax_library.string_methods
						print(f'{nav_functions.indent(4)}Official documentation for string methods:')
						print(f'{nav_functions.indent(4)}https://docs.python.org/3/library/stdtypes.html#string-methods')
						method_selection = return_list_selection(method_loc)
						nav_functions.display_library_dict(method_loc, method_selection, 'python_syntax_messages.json')
						#python_syntax_library.display_python_syntax(method_selection, method_loc, "")
					# List methods
					case 4:
						method_loc = python_syntax_library.list_methods
						method_selection = return_list_selection(method_loc)
						nav_functions.display_library_dict(method_loc, method_selection, 'python_syntax_messages.json')
					# Dictionary Methods
					case 5:
						method_loc = python_syntax_library.dict_methods
						method_selection = return_list_selection(method_loc)
						nav_functions.display_library_dict(method_loc, method_selection, 'python_syntax_messages.json')
					case _:
						print("Option not currently available.")
			# Python concept reference menu
			case 2:
				print('Select from the following concept categories:')
				method_loc = python_concept_library.macro_categories_dict
				method_selection = return_list_selection(method_loc)
				sub_cat = python_concept_library.macro_categories_dict[method_selection]

				print(f'{nav_functions.indent(4)}{method_selection}:')
				nav_functions.display_selection(sub_cat, 8)
				conc_select = nav_functions.return_user_input_from_selection(sub_cat)
				nav_functions.display_definition(sub_cat, conc_select, 'python_concept_messages.json')
