# Task class - Belongs to a Project

class Task:
    all = []
    VALID_STATUSES = ["pending", "in-progress", "complete"]
    
    def __init__(self, title, project_title, assigned_to=None):
        self.title = title
        self.project_title = project_title
        self.assigned_to = assigned_to
        self._status = "pending"
        Task.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if value not in Task.VALID_STATUSES:
            raise ValueError(f"Status must be one of: {Task.VALID_STATUSES}")
        self._status = value
    
    def mark_in_progress(self):
        self.status = "in-progress"
        return self
    
    def mark_complete(self):
        self.status = "complete"
        return self
    
    def project(self):
        from models.project import Project
        return Project.find_by_title(self.project_title)
    
    def to_dict(self):
        return {
            "title": self.title,
            "project_title": self.project_title,
            "assigned_to": self.assigned_to,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["project_title"], data.get("assigned_to"))
        task.status = data.get("status", "pending")
        return task
    
    @classmethod
    def find_by_title(cls, title):
        for task in cls.all:
            if task.title.lower() == title.lower():
                return task
        return None
    
    def __repr__(self):
        return f"Task(title={self.title}, status={self.status})"