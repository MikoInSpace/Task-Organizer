# Task Organizer
The Task Organizer is a simple command-line application that allows you to manage and organize your tasks. It provides functionalities to add, edit, delete, and view tasks. The tasks are stored in a text file for persistence between sessions.

## Features
**Add a new task**: You can add tasks by providing a title, description, and time.
**Delete a task**: Choose a task to delete from the list of existing tasks.
**Edit a task**: Edit the details of an existing task, including the title, description, and time.
**View all tasks**: Display a list of all tasks with their titles, descriptions, and times.
**Exit**: Terminate the Task Organizer program.
## Usage
**Add a Task**: Select option 1 from the main menu. Enter the task's title, description, and time when prompted. The task will be added to the list of tasks.

**Delete a Task**: Select option 2 from the main menu. Choose a task to delete from the list by entering its corresponding number.

**Edit a Task**: Select option 3 from the main menu. Choose a task to edit from the list by entering its corresponding number. Provide the new title, description, and time for the task.

**View All Tasks**: Select option 4 from the main menu. All tasks will be displayed, including their titles, descriptions, and times.

**Exit**: To exit the program, select option 5 from the main menu.

## Desktop Notifications
If a task is due within 10 minutes the script will automatically send a desktop notification to the user stating that [TASK TITLE] is due within 10 minutes.

### __STATUS: Broken__

## Getting Started
Clone this repository to your local machine using:

__git clone https://github.com/MikoInSpace/task-organizer.git__
Navigate to the project directory:

cd task-organizer
Run the Task Organizer:

__python task_organizer.py__

## Requirements
Python 3.x

### Note
Tasks are stored in a text file named tasks.txt located in your user's Documents folder. Make sure you have appropriate read and write permissions for the Documents folder.

Feel free to contribute to the project by submitting pull requests or opening issues. If you encounter any bugs or have suggestions for improvements, please let us know.

Happy task organizing!
