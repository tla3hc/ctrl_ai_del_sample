from task import Task

class Storage:
    def __init__(self, filepath):
        self.filepath = filepath

    def add_task(self, task):
        with open(self.filepath, "a") as f:
            f.write(task.to_string() + "\n")

    def get_tasks(self):
        tasks = []
        with open(self.filepath, "r") as f:
            for line in f:
                tasks.append(Task.from_string(line))
        return tasks
