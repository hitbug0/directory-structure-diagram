import os

NUM_INDENTS = 1
BRANCH = " "*NUM_INDENTS + "├── "
LEAF   = " "*NUM_INDENTS + "└── "
LINE   = " "*NUM_INDENTS + "│   "

def make_branch(item, depth, shape=BRANCH):
    return LINE * depth + shape + item + "\n"

def explore_directory(directory, depth=0):
    result = ""
    items = os.listdir(directory)
    items.sort()
    for index, item in enumerate(items):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            if index == len(items) - 1:
                result += make_branch(item, depth, shape=LEAF)
            else:
                result += make_branch(item, depth)
            result += explore_directory(path, depth + 1)
        else:
            if index == len(items) - 1:
                result += make_branch(item, depth, shape=LEAF)
            else:
                result += make_branch(item, depth)
    return result

def output_directory_structure(directory):
    structure = explore_directory(directory)
    with open("directory_structure.txt", "w", encoding="utf-8") as file:
        file.write(directory + "\n")
        file.write(structure)

current_directory = os.getcwd()
output_directory_structure(current_directory)
