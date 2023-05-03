def write_todos_to_file(todos):
    """Adds todos to a text file."""
    with open("todos.txt", "w") as file:
        file.writelines(todos)


def check_list_is_empty(todos):
    """Takes a list and returns True if it is empty and prints a warning message,
    otherwise returns False."""
    if len(todos) < 1:
        print("You don't have any todos in your list yet.\n")
        return True
    return False


def display_todos(todos):
    """Prints all todos from the list."""
    todos_print = [item.strip() for item in todos]
    for index, item in enumerate(todos_print):
        row = f"{index + 1} - {item}"
        print(row)
    print("\n")


if __name__ == "__main__":
    print("Hello from functions")
