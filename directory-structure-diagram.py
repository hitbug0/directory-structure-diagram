import os

NUM_INDENTS = 1
BRANCH = " "*NUM_INDENTS + "├── "
LEAF   = " "*NUM_INDENTS + "└── "
LINE   = " "*NUM_INDENTS + "│   "
SPACE  = " "*NUM_INDENTS + "    "

def make_line(lst):
    result = ""
    for item in lst:
        if item == 0:
            result += SPACE
        elif item == 1:
            result += LINE
    return result

def make_branch(item, depth, shape=BRANCH):
    return make_line(depth) + shape + item + "\n"

def explore_directory(directory, depth=[]):
    result = ""
    items = os.listdir(directory)
    items.sort()
    for index, item in enumerate(items):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            if index == len(items) - 1:
                result += make_branch(item, depth, shape=LEAF)
                add_depth = 0
            else:
                result += make_branch(item, depth)
                add_depth = 1
            result += explore_directory(path, depth + [add_depth])
        else:
            if index == len(items) - 1:
                result += make_branch(item, depth, shape=LEAF)
                depth = depth[:-1]+[0]
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
