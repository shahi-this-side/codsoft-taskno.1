import json
import os

FILE_NAME = "tasks.json"
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i+1}. {task['task']} [{status}]")

# Complete task
def complete_task(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number to mark complete: "))
    tasks[num-1]["done"] = True
    save_tasks(tasks)
    print("Task marked as completed!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    num = int(input("Enter task number to delete: "))
    tasks.pop(num-1)
    save_tasks(tasks)
    print("Task deleted!")

# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n----- TO DO LIST -----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()