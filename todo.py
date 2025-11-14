# todo.py  - Simple Console To-Do List Application

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # If file doesn't exist, just start with an empty list
    return tasks


# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Display menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("===========================\n")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    remove_index = int(input("Enter task number to remove: "))
                    if 1 <= remove_index <= len(tasks):
                        removed = tasks.pop(remove_index - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Enter a valid number.")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please select from 1–4.")


if __name__ == "__main__":
    main()