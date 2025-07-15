class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def to_string(self):
        return f"{self.title}|{self.done}"

    @staticmethod
    def from_string(s):
        title, done = s.strip().split("|")
        task = Task(title)
        task.done = done == "True"
        return task
