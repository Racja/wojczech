import os

def get_current_path():
    return os.path.dirname(os.path.realpath(__file__))

def tree(directory, depth):
    elements_list = os.listdir(directory)
    for element in elements_list:
        full_path = os.path.join(directory, element)
        print(depth * "   " + element)
        if os.path.isdir(full_path):
            tree(full_path, depth + 1)

tree(get_current_path(), 0)
