
tasks = []

def add_task(title, description, due_date):
    tasks.append({'title': title, 'description': description, 'due_date': due_date})

def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['description']} (Due: {task['due_date']})")

def update_task(index, title=None):
    if 0 <= index < len(tasks):
        task = tasks[index]
        if title:
            task['title'] = title
        if description:
            task['description'] = description
        if due_date:
            task['due_date'] = due_date
    else:
        print("Invalid task index.")

def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    else:
        print("Invalid task index.")

def save_tasks_to_file(filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(f"{task['title']},{task['description']}.{task['due_date']}\n")


if __name__ == "__main__":
    while True:
        print("\nCommand Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save Tasks to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task decription: ")
            due_date = input("Enter due date(YYYY-MM-DD): ")
            add_task(title,description,due_date)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            index = int(input("Enter task index to update: ")) - 1
            title = input("Enter new title (leave blank to keep unchanged): ")
            description = input("Enter task decription (leave blank to keep unchanged): ")
            due_date = input("Enter due date(YYYY-MM-DD) (leave blank to keep unchanged): ")
            update_task(index, title,description,due_date)
        elif choice == '4':
            index = int(input("Enter task index to delete: ")) - 1
            delete_task(index)
        elif choice == '5':
            filename = input("Enter filename to save tasks (e.g., tasks.txt): ")
            save_tasks_to_file(filename)
            print(f"Tasks saved to {filename}.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
