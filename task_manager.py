import json  # For saving and loading tasks
from prettytable import PrettyTable  # For improved task display

# Initialize an empty list to store tasks
tasks = []

# Load tasks from file (if any)
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            global tasks
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []  # Start with an empty list if the file is missing or invalid

# Save tasks to file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task():
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    deadline = input("Enter the task deadline (YYYY-MM-DD): ")
    priority = input("Enter the task priority (High, Medium, Low): ")

    task = {
        "title": title,
        "description": description,
        "completed": False,
        "deadline": deadline,
        "priority": priority
    }
    tasks.append(task)
    print(f"Task '{title}' added!")
    save_tasks()

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    table = PrettyTable()
    table.field_names = ["#", "Title", "Description", "Completed", "Deadline", "Priority"]

    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        table.add_row([index, task["title"], task["description"], status, task["deadline"], task["priority"]])

    print(table)

# Mark a task as completed
def mark_task_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        tasks[task_num - 1]["completed"] = True
        print(f"Task '{tasks[task_num - 1]['title']}' marked as completed!")
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number.")

# Delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        deleted_task = tasks.pop(task_num - 1)
        print(f"Task '{deleted_task['title']}' deleted!")
        save_tasks()
    except (ValueError, IndexError):
        print("Invalid task number.")

# Sort tasks by deadline or priority
def sort_tasks():
    print("\nSort by:")
    print("1. Deadline")
    print("2. Priority")
    choice = input("Choose an option: ")

    if choice == "1":
        tasks.sort(key=lambda x: x["deadline"])
        print("Tasks sorted by deadline!")
    elif choice == "2":
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        tasks.sort(key=lambda x: priority_order[x["priority"]])
        print("Tasks sorted by priority!")
    else:
        print("Invalid choice.")
    save_tasks()

# Main menu
def main_menu():
    load_tasks()  # Load tasks from file at the start
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Sort Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            sort_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()