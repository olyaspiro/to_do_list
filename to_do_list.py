options = ["View Tasks", "Add Task", "Delete Task", "Quit"]

tasks = []  

def welcome():
    """Display a welcome message."""
    print("==================================")
    print("  Welcome to Your To-Do List App  ")
    print("==================================")

def show_menu():
    """Display the main menu options."""
    print("\nMain Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Quit")

def view_tasks():
    """Display the current list of tasks."""
    if not tasks:
        print(" No tasks to display.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Prompt user to add a new task."""
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def delete_task():
    """Delete a task based on user input."""
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    finally:
        print("Returning to main menu...")

def main():
    """Run the To-Do List application."""
    welcome()
    while True:
        show_menu()
        try:
            choice = input("Enter your choice (1-4): ").strip()
            if choice == "1":
                view_tasks()
            elif choice == "2":
                add_task()
            elif choice == "3":
                delete_task()
            elif choice == "4":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please select a valid option (1-4).")
        except Exception as e:
            print(f" An unexpected error occurred: {e}")
        finally:
            print(f"\nYou can {options[0]}, {options[1]}, {options[2]}, or {options[3]}.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
