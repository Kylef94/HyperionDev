class Task:
    #constructor for task class
    def __init__(self, assignee, title, desc, assigned_date, due_date, complete=False):
        self.assignee = assignee
        self.title = title
        self.desc = desc
        self.assigned_date = assigned_date
        self.due_date = due_date
        #logic to impute boolean value from string
        if complete == 'Yes':
            self.complete = True
        else:
            self.complete = False

    def mark_complete(self):
        """marks task as complete"""
        self.complete = True

    def update_user(self, user):
        "updates username to which task is assigned"
        self.assignee = user

    def update_date(self, due_date):
        """updates task due date"""
        self.due_date = due_date


    def __str__(self):
        """sets string representation for printouts"""
        return (f"Task: {self.title}\n"
                      f"Assigned to: {self.assignee}\n"
                      f"Date assigned: {self.assigned_date}\n"
                      f"Due date: {self.due_date}\n"
                      f"Task Complete?: {self.complete}\n"
                      f"Task Description:\n {self.desc}\n")

    def to_file(self):
        """creates string for storing to file"""
        completed = "Yes" if self.complete else "No"
        return f"{self.assignee}, {self.title}, {self.desc}, {self.due_date}, {self.assigned_date}, {completed} \n"