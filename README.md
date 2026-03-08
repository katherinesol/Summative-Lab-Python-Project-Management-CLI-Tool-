# Project Tracker CLI

A command-line project management tool for managing users, projects, and tasks.

## Description

This CLI application allows administrators to:
- Create and manage users
- Assign projects to users
- Add tasks to projects
- Track task status (pending → in-progress → complete)
- Persist data using JSON files

## Setup Instructions

### 1. Clone the repository
```bash
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the CLI
```bash
python3 main.py --help
```

## Usage

### Add a user
```bash
python3 main.py add-user --name "Katherine" --email "katherine@example.com"
```

### List users
```bash
python3 main.py list-users
```

### Add a project
```bash
python3 main.py add-project --user "Katherine" --title "My Project" --description "Project description" --due-date "2026-03-07"
```

### List projects
```bash
python3 main.py list-projects
```

### Add a task
```bash
python3 main.py add-task --project "My Project" --title "Task name" --assigned-to "Katherine"
```

### List tasks
```bash
python3 main.py list-tasks
```

### Update task status
```bash
python3 main.py update-task --title "Task name" --status "in-progress"
```

### Complete a task
```bash
python3 main.py complete-task --title "Task name"
```
