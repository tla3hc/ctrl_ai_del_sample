# storage.py
import os
from task import Task

class Storage:
    def __init__(self, filepath):
        self.filepath = filepath

    def add_task(self, task):
        with open(self.filepath, "a") as f:
            f.write(task.to_string() + "\n")

    def get_tasks(self):
        tasks = []
        # 1. Ensure file exists—create it if not
        if not os.path.exists(self.filepath):
            open(self.filepath, "w").close()
        # 2. Read tasks with error handling
        try:
            with open(self.filepath, "r") as f:
                for line in f:
                    if line.strip():
                        tasks.append(Task.from_string(line))
        except (OSError, ValueError) as e:
            print(f"Error reading tasks: {e}")
        return tasks
    
    def remove_task(self, task_to_remove):
        tasks = self.get_tasks()
        tasks = [task for task in tasks if task != task_to_remove]
        with open(self.filepath, "w") as f:
            for task in tasks:
                f.write(task.to_string() + "\n")
