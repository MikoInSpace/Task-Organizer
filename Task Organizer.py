import os

# Function to get the user's documents path
def get_documents_path():
    user_home = os.path.expanduser("~")
    documents_path = os.path.join(user_home, "Documents")
    return documents_path

# Function to save tasks to a file
def save_tasks_to_file(tasks):
    documents_path = get_documents_path()
    file_path = os.path.join(documents_path, "tasks.txt")
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"Title: {task['title']}\nDescription: {task['description']}\nTime: {task['time']}\n\n")

# Function to load tasks from a file
def load_tasks_from_file():
    tasks = []
    documents_path = get_documents_path()
    file_path = os.path.join(documents_path, "tasks.txt")
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            title, description, time = "", "", ""
            for line in lines:
                if line.startswith("Title: "):
                    title = line.strip()[7:]
                elif line.startswith("Description: "):
                    description = line.strip()[13:]
                elif line.startswith("Time: "):
                    time = line.strip()[6:]
                    if title and description and time:
                        tasks.append({"title": title, "description": description, "time": time})
                        title, description, time = "", "", ""
    except FileNotFoundError:
        pass
    return tasks

# Load tasks from the file
tasks = load_tasks_from_file()

# Print the welcome message
print("Welcome to Task Organizer!")

# Main loop
while True:
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Edit a task")
    print("4. View all tasks")
    print("5. Exit")

    # Get user's selection
    selection = input("Select a task: ")

    if selection == "1":
        # Add a new task
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        time = input("Enter the task time: ")
        task = {"title": title, "description": description, "time": time}
        tasks.append(task)
        save_tasks_to_file(tasks)
        print("Task added successfully!")

    elif selection == "2":
        # Delete a task
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
        # Edit a task
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
        # View all tasks
        if tasks:
            print("All tasks:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. Title: {task['title']}\nDescription: {task['description']}\nTime: {task['time']}\n")
        else:
            print("No tasks available.")

    elif selection == "5":
        # Exit the program
        print("Exiting the Task Organizer.")
        break

    else:
        # Invalid selection
        print("Invalid selection. Please choose a valid option.")
