from task import Task
from storage import Storage

def main():
    store = Storage("tasks.txt")

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            task = Task(title)
            store.add_task(task)
            print("Task added.")

        elif choice == "2":
            tasks = store.get_tasks()
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t.title} - {'Done' if t.done else 'Pending'}")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
