# User class - Inherits from Person

from models.person import Person

class User(Person):
    all = []
    
    def __init__(self, name, email):
        super().__init__(name, email)
        User.all.append(self)
    
    def projects(self):
        from models.project import Project
        return [p for p in Project.all if p.user_name == self.name]
    
    def add_project(self, title, description, due_date):
        from models.project import Project
        return Project(title, description, due_date, self.name)
    
    def to_dict(self):
        return {"name": self.name, "email": self.email}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["email"])
    
    @classmethod
    def find_by_name(cls, name):
        for user in cls.all:
            if user.name.lower() == name.lower():
                return user
        return None
    
    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"