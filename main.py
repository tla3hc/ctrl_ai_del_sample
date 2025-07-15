from task import Task
from storage import Storage

number_of_tasks = 0
number_of_completed_tasks = 0

def main():
    store = Storage("tasks.txt")

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Complete Percentage\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            task = Task(title)
            store.add_task(task)
            print("Task added.")
            number_of_tasks += 1

        elif choice == "2":
            tasks = store.get_tasks()
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t.title} - {'Done' if t.done else 'Pending'}")
        
        elif choice == "3":
            tasks = store.get_tasks()
            if not tasks:
                print("No tasks available.")
                continue
            
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t.title} - {'Done' if t.done else 'Pending'}")
            
            task_num = int(input("Enter task number to complete: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num].done = True
                number_of_completed_tasks += 1
                print(f"Task '{tasks[task_num].title}' marked as done.")
            else:
                print("Invalid task number.")
        
        elif choice == "4":
            if number_of_tasks == 0:
                number_of_tasks = 1  # Avoid division by zero
            completion_percentage = (number_of_completed_tasks / number_of_tasks) * 100
            print(f"Completion Percentage: {completion_percentage:.2f}%")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
