import os
from datetime import datetime
import schedule
import time
from plyer import notification

def get_documents_path():
    user_home = os.path.expanduser("~")
    documents_path = os.path.join(user_home, "Documents")
    return documents_path

def save_tasks_to_file(tasks):
    documents_path = get_documents_path()
    file_path = os.path.join(documents_path, "tasks.txt")
    with open(file_path, "w") as file:
        file.write("+------------------------------------+------------------------------------+-------------------+\n")
        file.write("|              Title                 |            Description             |        Time       |\n")
        file.write("+------------------------------------+------------------------------------+-------------------+\n")
        for task in tasks:
            title = task['title']
            description = task['description']
            time = task['time']
            file.write(f"| {title.ljust(34)} | {description.ljust(34)} | {time.ljust(17)} |\n")
            file.write("+------------------------------------+------------------------------------+-------------------+\n")

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

# Function to send desktop notification
def send_notification(task):
    notification_title = "Task Due Soon"
    notification_message = f"The task '{task['title']}' is due in 5 minutes or less."
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=10  # Notification timeout in seconds
    )

# Function to check for due tasks and send notifications
def check_due_tasks():
    now = datetime.now()
    for task in tasks:
        task_time = datetime.strptime(task['time'], "%d-%m-%Y %H:%M")
        time_difference = task_time - now
        print(f"Task: {task['title']} | Time difference: {time_difference.total_seconds()} seconds")
        if 0 <= time_difference.total_seconds() <= 300:  # 5 minutes (300 seconds)
            send_notification(task)

# Schedule the task checker to run every minute
schedule.every(1).minutes.do(check_due_tasks)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Edit a task")
    print("4. View all tasks")
    print("5. Exit")

    selection = input("Select a task: ")

    if selection == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        while True:
            try:
                time_input = input("Enter the task time (DD-MM-YYYY HH:MM): ")
                time = datetime.strptime(time_input, "%d-%m-%Y %H:%M")
                break
            except ValueError:
                print("Invalid date and time format. Please use DD-MM-YYYY HH:MM format.")
        task = {"title": title, "description": description, "time": time.strftime("%d-%m-%Y %H:%M")}
        tasks.append(task)
        save_tasks_to_file(tasks)
        print("Task added successfully!")

    elif selection == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        if tasks:
            print("Select a task to delete:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['title']}")
            try:
                task_index = int(input()) - 1
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    save_tasks_to_file(tasks)
                    print(f"Task '{deleted_task['title']}' deleted successfully!")
                else:
                    print("Invalid task index.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        else:
            print("No tasks to delete.")

    elif selection == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        if tasks:
            print("Select a task to edit:")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['title']}")
            try:
                task_index = int(input()) - 1
                if 0 <= task_index < len(tasks):
                    new_title = input("Enter the new task title: ")
                    new_description = input("Enter the new task description: ")
                    new_time = input("Enter the new task time (DD-MM-YYYY HH:MM): ")
                    try:
                        new_time = datetime.strptime(new_time, "%d-%m-%Y %H:%M")
                        tasks[task_index] = {"title": new_title, "description": new_description, "time": new_time.strftime("%d-%m-%Y %H:%M")}
                        save_tasks_to_file(tasks)
                        print("Task edited successfully!")
                    except ValueError:
                        print("Invalid date and time format. Please use DD-MM-YYYY HH:MM format.")
                else:
                    print("Invalid task index.")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        else:
            print("No tasks to edit.")

    elif selection == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        if tasks:
            print("All tasks:")
            print("+------------------------------------+------------------------------------+------------------------------------+")
            print("|              Title                 |            Description             |                Time                |")
            print("+------------------------------------+------------------------------------+------------------------------------+")
            for task in tasks:
                print(f"| {task['title'].ljust(34)} | {task['description'].ljust(34)} | {task['time'].ljust(34)} |")
                print("+------------------------------------+------------------------------------+------------------------------------+")
                time.sleep(5)
        else:
            print("No tasks available.")

    elif selection == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Exiting the Task Organizer.")
        break

    else:
        print("Invalid selection. Please choose a valid option.")

    # Run pending scheduled tasks
    schedule.run_pending()
