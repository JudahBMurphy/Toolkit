def terminal_navigation():
	print('''See following list of basic Terminal navigation commands:
Note: 'x' indicates name of file or directory. 'y' indicates a path.
	man x - Display documentation about a command.
	cd x - Change directory.
		cd - /home/username
		cd / - /
		cd ../ - Go up one directory.
		cd ../.. - Go up two directories.
		cd ~ - Go to home directory.
	ls - List files and directories in current directory.
		ls * - List all files in directory.
	pwd - Display the path of the current directory.
	''')

def terminal_files_dir_interaction():
	print('''See following list of Terminal commands for files and directories:
Note: 'x' indicates name of file or directory. 'y' indicates a path.
	man x - Display documentation about a command.
	touch x - Create a file.
	mkdir x - Create a directory
	rm x - Remove a file. Use 'rm -r' to remove a directory.
	cp x - Copy a file or directory.
	mv x y - Move or rename a file or directory.
	echo - Print text to STDOUT.
	cat x - Display contents of a file.
	more x - Display contents of a file. Lets the user scroll down.
	less x - Display contents of a file in an even more interactive way.
	head x - Display the first part of a file.
	tail x - Display the last part of a file.
	source x - read and execute commands from a file in current shell environment
	''')

def terminal_environment():
	print('''See following list of Terminal commands for modifying the Terminal environment:
Note: 'x' indicates name of file or directory. 'y' indicates a path.
	man x - Display documentation about a command.
	ls -a ~ - Display hidden files in home directory
	VARIABLE="value" - create an environment variable
	source ~/.venv/ENVIROMENT_NAME/bin/activate - activate a virtual python environment (env_py3.11)
	deactivate - deactivate the current virtual environment
	''')

def terminal_permissions():
	print('''See following list of Terminal commands for permissions:
Note: 'x' indicates name of file or directory. 'y' indicates a path.
	man x - Display documentation about a command.

	Permissions structure:
		+-------- Directory or not
		|  +------- User Read, Write, Execute
		|  |   +------- Group Read, Write, Execute
		|  |   |   +----- Other Read, Write, Execute
		|  |   |   |   +--- The name of the user
		|  |   |   |   |     +--- The name of the group
		|  |   |   |   |     |
		d|rwx|rwx|rwx user group

	chmod +w filename.py - Change file permissions
	chmod xxx filename.py - Change file permissions
		0	No permission granted.
		1	Can execute.
		2	Can write.
		3	Can write and execute (2 + 1 = 3).
		4	Can read.
		5	Can read and execute (4 +1 = 5).
		6	Can read and write (4 + 2 = 6).
		7	Can read and write and execute (4 + 2 + 1 = 7).
	''')

#def cmd_ln_help():
	
