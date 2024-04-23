import nav_functions
import toolkit2_git_menu
import toolkit2_terminal
import python_concept_library
import python_syntax_library

def return_list_selection(list):
	nav_functions.display_list_selection(list, 4)
	selection = nav_functions.return_user_input_from_selection(list)
	return selection


topic_list = ['Terminal', 'Git', 'Python']
options_list = ['Syntax','Concepts']
print('')
print('Welcome to Toolkit. What subject do you need to reference:')
topic_selection = return_list_selection(topic_list)

match topic_selection:
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
				nav_cmds = toolkit2_terminal.terminal_nav_commands
				toolkit2_terminal.display__terminal_syntax_library(nav_cmds)
			case 2:
				print('See below reference commands for interacting with files and directories:')
				dir_cmds = toolkit2_terminal.terminal_file_dir_commands
				toolkit2_terminal.display__terminal_syntax_library(dir_cmds)
			case 3:
				print('See below reference commands for making changes to the Terminal environment:')
				env_cmds = toolkit2_terminal.terminal_env_commands
				toolkit2_terminal.display__terminal_syntax_library(env_cmds)
			case 4:
				print('See below explaination of permissions concepts:')
				print(f'{toolkit2_terminal.terminal_permissions}')
	case 2:
		print('Please see below for list of git commands:')
		toolkit2_git_menu.display__git_syntax_library(toolkit2_git_menu.git_commands)
	case 3:
		python_help_options = ['Syntax Reference','Concept Review']
		print(f'Please select what you need help with:')
		help_selection = return_list_selection(python_help_options)

		match help_selection:
			case 1:
				print('Select from the following categories:')
				syntax_selection = return_list_selection(python_syntax_library.syntax_categories)
				nav_functions.display_list_selection(python_syntax_library.built_in_functions, 4)
				bi_funcs = python_syntax_library.built_in_functions
				bi_func_selection = nav_functions.return_user_input_from_selection(bi_funcs)
				python_syntax_library.display_list_item_message(bi_func_selection, bi_funcs)
			case 2:
				print('Select from the following concept categories:')
				nav_functions.display_dict_selection(python_concept_library.macro_categories_dict, 4)
				macro_cat = python_concept_library.macro_categories_dict
				macro_selection = nav_functions.return_user_input_from_selection(macro_cat)
				sub_cat = python_concept_library.macro_categories_dict[macro_selection]
				print(f'{nav_functions.indent(4)}{macro_selection}:')
				nav_functions.display_list_selection(sub_cat, 8)
				conc_select = nav_functions.return_user_input_from_selection(sub_cat)
				python_concept_library.display_python_concept(sub_cat, conc_select)
