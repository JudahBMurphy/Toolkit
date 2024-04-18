import json
import nav_functions

with open('toolkit2_git_messages.json','r') as file:
    MESSAGES = json.load(file)

def messages(message):
    return MESSAGES[message]

def display__git_syntax_library(list):
    for item in list:
        print(f'{nav_functions.indent(4)}{item}: {messages(item)}')

git_commands = [
    "git init",
    "git status",
    "git add x",
    "git commit -m ' commit message'",
    "git log",
    "git remote add origin https://github.com/GITHUBUSERNAME/REPONAME.git",
    "git push -u origin main",
    "git fetch",
    "git diff origin/main",
    "git pull --ff-only",
    "git clone <remote repository url> <local directory name>",
    "git checkout branch_name",
    "git checkout -b branch_name",
    "git merge branch_name"
]