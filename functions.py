
def get_todos(filename="todos"):
    """
    Read a text file and return the list of
    to-do items.
    """
    # using context manager
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos"):
    """
    Write the to-do list to text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#if __name__ == "__main__":
