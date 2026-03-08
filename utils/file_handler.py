# File handler - JSON read/write functions

import json
import os

DATA_DIR = "data"

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_json(filename):
    filepath = os.path.join(DATA_DIR, filename)
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Warning: {filename} contains invalid JSON. Starting fresh.")
        return []

def save_json(filename, data):
    ensure_data_dir()
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w") as file:
        json.dump(data, file, indent=2)

def load_all_data():
    from models.user import User
    from models.project import Project
    from models.task import Task
    
    User.all = []
    Project.all = []
    Task.all = []
    
    for user_dict in load_json("users.json"):
        User.from_dict(user_dict)
    
    for project_dict in load_json("projects.json"):
        Project.from_dict(project_dict)
    
    for task_dict in load_json("tasks.json"):
        Task.from_dict(task_dict)

def save_all_data():
    from models.user import User
    from models.project import Project
    from models.task import Task
    
    save_json("users.json", [user.to_dict() for user in User.all])
    save_json("projects.json", [project.to_dict() for project in Project.all])
    save_json("tasks.json", [task.to_dict() for task in Task.all])