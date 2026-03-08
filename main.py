#!/usr/bin/env python3
# Project Tracker CLI - Main entry point

import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_handler import load_all_data, save_all_data
from utils.display import display_users, display_projects, display_tasks, display_success, display_error, display_welcome

def add_user(args):
    if User.find_by_name(args.name):
        display_error(f"User '{args.name}' already exists.")
        return
    User(args.name, args.email)
    save_all_data()
    display_success(f"User '{args.name}' created successfully!")

def list_users(args):
    display_users(User.all)

def add_project(args):
    user = User.find_by_name(args.user)
    if not user:
        display_error(f"User '{args.user}' not found.")
        return
    if Project.find_by_title(args.title):
        display_error(f"Project '{args.title}' already exists.")
        return
    user.add_project(args.title, args.description, args.due_date)
    save_all_data()
    display_success(f"Project '{args.title}' created for user '{args.user}'!")

def list_projects(args):
    if args.user:
        user = User.find_by_name(args.user)
        if not user:
            display_error(f"User '{args.user}' not found.")
            return
        display_projects(user.projects())
    else:
        display_projects(Project.all)

def add_task(args):
    project = Project.find_by_title(args.project)
    if not project:
        display_error(f"Project '{args.project}' not found.")
        return
    project.add_task(args.title, args.assigned_to)
    save_all_data()
    display_success(f"Task '{args.title}' added to project '{args.project}'!")

def list_tasks(args):
    if args.project:
        project = Project.find_by_title(args.project)
        if not project:
            display_error(f"Project '{args.project}' not found.")
            return
        display_tasks(project.tasks())
    else:
        display_tasks(Task.all)

def update_task(args):
    task = Task.find_by_title(args.title)
    if not task:
        display_error(f"Task '{args.title}' not found.")
        return
    task.status = args.status
    save_all_data()
    display_success(f"Task '{args.title}' updated to '{args.status}'!")

def complete_task(args):
    task = Task.find_by_title(args.title)
    if not task:
        display_error(f"Task '{args.title}' not found.")
        return
    task.mark_complete()
    save_all_data()
    display_success(f"Task '{args.title}' marked as complete!")

def main():
    load_all_data()
    
    parser = argparse.ArgumentParser(description="Project Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # add-user
    p = subparsers.add_parser("add-user", help="Add a new user")
    p.add_argument("--name", required=True)
    p.add_argument("--email", required=True)
    p.set_defaults(func=add_user)
    
    # list-users
    p = subparsers.add_parser("list-users", help="List all users")
    p.set_defaults(func=list_users)
    
    # add-project
    p = subparsers.add_parser("add-project", help="Add a new project")
    p.add_argument("--user", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--description", default="")
    p.add_argument("--due-date", dest="due_date", default="TBD")
    p.set_defaults(func=add_project)
    
    # list-projects
    p = subparsers.add_parser("list-projects", help="List projects")
    p.add_argument("--user")
    p.set_defaults(func=list_projects)
    
    # add-task
    p = subparsers.add_parser("add-task", help="Add a new task")
    p.add_argument("--project", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--assigned-to", dest="assigned_to")
    p.set_defaults(func=add_task)
    
    # list-tasks
    p = subparsers.add_parser("list-tasks", help="List tasks")
    p.add_argument("--project")
    p.set_defaults(func=list_tasks)
    
    # update-task
    p = subparsers.add_parser("update-task", help="Update task status")
    p.add_argument("--title", required=True)
    p.add_argument("--status", required=True, choices=["pending", "in-progress", "complete"])
    p.set_defaults(func=update_task)
    
    # complete-task
    p = subparsers.add_parser("complete-task", help="Mark task complete")
    p.add_argument("--title", required=True)
    p.set_defaults(func=complete_task)
    
    args = parser.parse_args()
    
    if not args.command:
        display_welcome()
        parser.print_help()
        return
    
    args.func(args)

if __name__ == "__main__":
    main()