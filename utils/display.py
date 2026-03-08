# Display utilities - Rich formatting

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def display_users(users):
    if not users:
        console.print("[yellow]No users found.[/yellow]")
        return
    
    table = Table(title="Users", show_header=True, header_style="bold cyan")
    table.add_column("Name", style="green")
    table.add_column("Email", style="blue")
    table.add_column("Projects", justify="center")
    
    for user in users:
        table.add_row(user.name, user.email, str(len(user.projects())))
    
    console.print(table)

def display_projects(projects):
    if not projects:
        console.print("[yellow]No projects found.[/yellow]")
        return
    
    table = Table(title="Projects", show_header=True, header_style="bold cyan")
    table.add_column("Title", style="green")
    table.add_column("Description", style="white")
    table.add_column("Due Date", style="yellow")
    table.add_column("Owner", style="blue")
    table.add_column("Tasks", justify="center")
    
    for project in projects:
        table.add_row(project.title, project.description, project.due_date, project.user_name, str(len(project.tasks())))
    
    console.print(table)

def display_tasks(tasks):
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return
    
    table = Table(title="Tasks", show_header=True, header_style="bold cyan")
    table.add_column("Title", style="green")
    table.add_column("Project", style="blue")
    table.add_column("Assigned To", style="white")
    table.add_column("Status", justify="center")
    
    for task in tasks:
        if task.status == "complete":
            status = "[green]complete[/green]"
        elif task.status == "in-progress":
            status = "[yellow]in-progress[/yellow]"
        else:
            status = "[red]pending[/red]"
        table.add_row(task.title, task.project_title, task.assigned_to or "Unassigned", status)
    
    console.print(table)

def display_success(message):
    console.print(f"[green]✓ {message}[/green]")

def display_error(message):
    console.print(f"[red]✗ {message}[/red]")

def display_welcome():
    console.print(Panel.fit(
        "[bold cyan]Project Tracker CLI[/bold cyan]\n[white]Manage users, projects, and tasks[/white]",
        border_style="cyan"
    ))