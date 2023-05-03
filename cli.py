from datetime import datetime
import os
import time

from functions import write_todos_to_file, check_list_is_empty, display_todos
from time_format_functions import custom_date_format

# creates todos.txt if it doesn't exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", "a+") as file:
        pass

# creates a list with todos from the text file
with open("todos.txt", "r") as file:
    todos = file.readlines()

date_str = time.strftime("%Y-%m-%d")
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
formatted_date = custom_date_format(date_obj)
print(f"Today is {formatted_date}")

while True:
    user_action = input("\nType add, show, complete, edit or exit: ")
    user_action = user_action.lower().strip()
    print(user_action)

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)
            write_todos_to_file(todos)
        case "show" | "display":
            # if the to-do list is empty user will be asked to make a different action
            if check_list_is_empty(todos):
                continue
            display_todos(todos)
        case "edit":
            # if the to-do list is empty user will be asked to make a different action
            if check_list_is_empty(todos):
                continue
            while True:
                display_todos(todos)
                try:
                    number = int(input("Number of the todo to edit: ")) - 1
                    if number < 0:
                        print("\nPlease input a valid todo number from the list.\n")
                        continue
                    todos[number]
                    break
                except (IndexError, ValueError):
                    print("\nPlease input a valid todo number from the list.\n")
                    continue
            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo
            write_todos_to_file(todos)
        case "complete":
            if check_list_is_empty(todos):
                continue

            while True:
                display_todos(todos)
                try:
                    index_to_remove = int(input("Number of the todo to complete: ")) - 1
                    if index_to_remove < 0:
                        print("\nPlease input a valid todo number from the list.\n")
                        continue
                    removed_task = todos.pop(index_to_remove).strip()
                    break
                except (IndexError, ValueError):
                    print("\nPlease input a valid todo number from the list:")
                    continue
            write_todos_to_file(todos)
            message = f"Task '{removed_task}' was completed and removed from the list.\n"
            print(message)
            if len(todos) < 1:
                print("***Congratulations you've completed all your tasks! 🎉🎉🎉***\n")
        case "exit" | "quit":
            print("Bye!")
            break
        case _:
            print("No such action")
