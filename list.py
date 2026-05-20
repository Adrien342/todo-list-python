task=[]
def add_task():
    task_name=input("Enter the task name: ")
    task.append(task_name)
    print("Task added successfully.")
def view_tasks():
    if not task:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task_name in enumerate(task, start=1):
            print(f"{index}. {task_name}")
def delete_task():
    view_tasks()
    if not task:
        return
    try:
        task_index=int(input("Enter the task number to delete: "))
        if 1<=task_index<=len(task):
            deleted_task=task.pop(task_index-1)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        add_task()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        delete_task()
    elif choice=="4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
