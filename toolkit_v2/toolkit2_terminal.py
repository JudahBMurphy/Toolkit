import json
import nav_functions

with open('toolkit2_terminal_messages.json','r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def display__terminal_syntax_library(list):
    for item in list:
        print(f'{nav_functions.indent(4)}{item}: {messages(item)}')

terminal_nav_commands = [
    "man x",
    "cd x",
    "cd",
    "cd /",
    "cd ../",
    "cd ../..",
    "cd ~",
    "ls",
    "ls *",
    "pwd"
]

terminal_file_dir_commands = [
    "man x",
    "touch x",
    "mkdir x",
    "rm x",
    "cp x",
    "mv x y",
    "echo:",
    "cat x",
    "more x",
    "less x",
    "head x",
    "tail x",
    "source x"
]

terminal_env_commands = [
    "man x",
    "ls -a ~",
    "VARIABLE=\"value\"",
    "source ~/.venv/ENVIROMENT_NAME/bin/activate",
    "deactivate"
]

terminal_permissions = '''
Permissions structure:
        +-------- Directory or not
        |  +------- User Read, Write, Execute
        |  |   +------- Group Read, Write, Execute
        |  |   |   +----- Other Read, Write, Execute
        |  |   |   |   +--- The name of the user
        |  |   |   |   |     +--- The name of the group
        |  |   |   |   |     |
        d|rwx|rwx|rwx user group

Permissions commands:
    chmod +w filename.py - Change file permissions
    chmod xxx filename.py - Change file permissions
        0   No permission granted.
        1   Can execute.
        2   Can write.
        3   Can write and execute (2 + 1 = 3).
        4   Can read.
        5   Can read and execute (4 +1 = 5).
        6   Can read and write (4 + 2 = 6).
        7   Can read and write and execute (4 + 2 + 1 = 7).
    '''