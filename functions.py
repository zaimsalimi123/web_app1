FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Get the existing todos from the file.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    """Write the Entered todos in the file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
