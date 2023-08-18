import os

def get_documents_path():
    user_home = os.path.expanduser("~")
    documents_path = os.path.join(user_home, "Documents")
    return documents_path

def save_tasks_to_file(tasks):
    documents_path = get_documents_path()
    file_path = os.path.join(documents_path, "tasks.txt")
    with open(file_path, "w") as file:
        file.write("+------------------------------------+------------------------------------+------------------------------------+\n")
        file.write("|              Title                 |            Description              |                Time                |\n")
        file.write("+------------------------------------+------------------------------------+------------------------------------+\n")
        for task in tasks:
            title = task['title']
            description = task['description']
            time = task['time']
            file.write(f"| {title.ljust(34)} | {description.ljust(34)} | {time.ljust(34)} |\n")
            file.write("+------------------------------------+------------------------------------+------------------------------------+\n")

def load_tasks_from_file():
    tasks = []
    documents_path = get_documents_path()
    file_path = os.path.join(documents_path, "tasks.txt")
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            title, description, time = "", "", ""
            for line in lines:
                if line.startswith("| "):
                    parts = line.split("|")[1:-1]
                    title = parts[0].strip()
                    description = parts[1].strip()
                    time = parts[2].strip()
                    tasks.append({"title": title, "description": description, "time": time})
    except FileNotFoundError:
        pass
    return tasks

tasks = load_tasks_from_file()

print("Welcome to Task Organizer!")

while True:
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Edit a task")
    print("4. View all tasks")
    print("5. Exit")

    selection = input("Select a task: ")

    if selection == "1":
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        time = input("Enter the task time: ")
        task = {"title": title, "description": description, "time": time}
        tasks.append(task)
        save_tasks_to_file(tasks)
        print("Task added successfully!")

    elif selection == "2":
        if tasks:
            print("Select a task to delete:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['title']}")
            task_index = int(input()) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                save_tasks_to_file(tasks)
                print(f"Task '{deleted_task['title']}' deleted successfully!")
            else:
                print("Invalid task index.")
        else:
            print("No tasks to delete.")

    elif selection == "3":
        if tasks:
            print("Select a task to edit:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['title']}")
            task_index = int(input()) - 1
            if 0 <= task_index < len(tasks):
                new_title = input("Enter the new task title: ")
                new_description = input("Enter the new task description: ")
                new_time = input("Enter the new task time: ")
                tasks[task_index] = {"title": new_title, "description": new_description, "time": new_time}
                save_tasks_to_file(tasks)
                print("Task edited successfully!")
            else:
                print("Invalid task index.")
        else:
            print("No tasks to edit.")

    elif selection == "4":
        if tasks:
            print("All tasks:")
            print("+------------------------------------+------------------------------------+------------------------------------+")
            print("|              Title                 |            Description             |                Time                |")
            print("+------------------------------------+------------------------------------+------------------------------------+")
            for task in tasks:
                print(f"| {task['title'].ljust(34)} | {task['description'].ljust(34)} | {task['time'].ljust(34)} |")
                print("+------------------------------------+------------------------------------+------------------------------------+")
        else:
            print("No tasks available.")

    elif selection == "5":
        print("Exiting the Task Organizer.")
        break

    else:
        print("Invalid selection. Please choose a valid option.")
