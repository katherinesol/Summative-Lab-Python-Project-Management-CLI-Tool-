# Project class - Belongs to a User, has many Tasks

class Project:
    all = []
    
    def __init__(self, title, description, due_date, user_name):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_name = user_name
        Project.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value
    
    def tasks(self):
        from models.task import Task
        return [t for t in Task.all if t.project_title == self.title]
    
    def add_task(self, title, assigned_to=None):
        from models.task import Task
        return Task(title, self.title, assigned_to)
    
    def user(self):
        from models.user import User
        return User.find_by_name(self.user_name)
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_name": self.user_name
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["description"], data["due_date"], data["user_name"])
    
    @classmethod
    def find_by_title(cls, title):
        for project in cls.all:
            if project.title.lower() == title.lower():
                return project
        return None
    
    def __repr__(self):
        return f"Project(title={self.title}, user={self.user_name})"