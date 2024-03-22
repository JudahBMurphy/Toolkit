# This program serves as a quick reference guide to basic commands 
# and syntax learned so far. Intended to be accessed using Terminal.

import toolkit_python
import toolkit_terminal


def terminal_menu_loop():
	print('''What do you need assistence with?
Choose from list by typing in corresponding number:
	1. Basic Navigation
	2. Files and Directories
	3. Environment Changes
	4. Permissions
	0. End Program''')
	loop_controller = False
	terminal_help_input = int(input())
	while loop_controller != True:
		match terminal_help_input:
			case 0:
				loop_controller = True
			case 1:
				toolkit_terminal.terminal_navigation()
				loop_controller = True
			case 2:
				toolkit_terminal.terminal_files_dir_interaction()
				loop_controller = True
			case 3:
				toolkit_terminal.terminal_environment()
				loop_controller = True
			case 4:
				toolkit_terminal.terminal_permissions()
				loop_controller = True
			case _:
				print('Command not recognized. Try again using specified options.')
				terminal_help_input = int(input())

def git_help():
	print('''See following list of Git commands:
Note: 'x' indicates name of file or directory. 'y' indicates a path.
	git init - Creates git repository in current directory. 
	git status - Display status of files in git repository
	git add x - Stages file for the next commit
	git commit -m ' commit message' - Commits staged files to the repository
	git log - Display the commit history
	git remote add origin https://github.com/GITHUBUSERNAME/REPONAME.git - add a remote repo
	git push -u origin main - push commits to the remote repo
 	git fetch - fetch commits from the remote repo
 	git diff origin/main - Display differences between local and remote repo
 	git pull --ff-only - copy the remote repository into the local repository
 	git clone <remote repository url> <local directory name> - clone a remote repository
	''')

def python_menu_loop():
	print('''What do you need assistence with?
Choose from list by typing in corresponding number:
	1. Data Types
	2. Collections
	3. Loops
	4. Functions and Methods
	5. Concepts
	6. Documentation
	0. End Program''')
	loop_controller = False
	python_help_input = int(input())
	while loop_controller != True:
		match python_help_input:
			case 0:
				loop_controller = True
			case 1:
				loop_controller = True
				toolkit_python.data_type_library()
			case 2:
				loop_controller = True
				toolkit_python.collections_library()
			case 3:
				loop_controller = True
				toolkit_python.loop_library()
			case 5:
				loop_controller = True
				toolkit_python.concept_library()
			case _:
				print('Command not recognized. Try again using specified options.')
				python_help_input = int(input())

print('''What do you need?
Choose from list by typing in corresponding number:
	1. Help with Terminal
	2. Help with Git
	3. Help with Python
	0. End Program''')
help_input = int(input())
main_menu_loop_control = False

while main_menu_loop_control != True:
	match help_input:
		case 0:
			main_menu_loop_control = True
		case 1:
			terminal_menu_loop()
			main_menu_loop_control = True
		case 2:
			main_menu_loop_control = True
			git_help()
		case 3:
			python_menu_loop()
			main_menu_loop_control = True
		case _:
			print('Command not recognized. Try again using specified options.')
			help_input = int(input())
