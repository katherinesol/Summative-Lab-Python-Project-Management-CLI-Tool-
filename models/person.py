# Person class - Parent class for User

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Email must be a valid email address")
        self._email = value
    
    def __repr__(self):
        return f"Person(name={self.name}, email={self.email})"