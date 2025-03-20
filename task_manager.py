# 📌 Simple Task Manager

tasks = []  # List to store tasks

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"✅ Task Added: {task}")

def view_tasks():
    if not tasks:
        print("📌 No tasks available.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['task']} - {status}")

def mark_complete(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"🎉 Task {task_number} marked as completed!")
    else:
        print("❌ Invalid task number!")

# 🔹 Main Menu
while True:
    print("\n📌 Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_number = int(input("Enter task number: "))
        mark_complete(task_number)
    elif choice == "4":
        print("🚀 Exiting Task Manager. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
