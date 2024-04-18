import nav_functions
import toolkit2_git_menu
import toolkit2_terminal

topic_list = ['Terminal', 'Git', 'Python']
options_list = ['Syntax','Concepts']
print('')
print('Welcome to Toolkit. What subject do you need to reference:')
nav_functions.display_list_selection(topic_list)
topic_selection = nav_functions.return_user_input_from_selection(topic_list)

match topic_selection:
	case 1:
		terminal_options = ['Navigation', 'Files and Directories', 'Environment Changes', 'Permissions']
		print(f'Please select a category for reference material:')
		nav_functions.display_list_selection(terminal_options)
		category_selection = nav_functions.return_user_input_from_selection(terminal_options)

		match category_selection:
			case 1:
				print('See below reference commands for navigating the terminal:')
				toolkit2_terminal.display__terminal_syntax_library(toolkit2_terminal.terminal_nav_commands)
			case 2:
				print('See below reference commands for interacting with files and directories:')
				toolkit2_terminal.display__terminal_syntax_library(toolkit2_terminal.terminal_file_dir_commands)
			case 3:
				print('See below reference commands for making changes to the Terminal environment:')
				toolkit2_terminal.display__terminal_syntax_library(toolkit2_terminal.terminal_env_commands)
			case 4:
				print('See below explaination of permissions concepts:')
				print(f'{toolkit2_terminal.terminal_permissions}')
	case 2:
		print('Please see below for list of git commands:')
		toolkit2_git_menu.display__git_syntax_library(toolkit2_git_menu.git_commands)
	case 3:
		print(f'Accessing {topic_list[topic_selection - 1]} toolkit')
