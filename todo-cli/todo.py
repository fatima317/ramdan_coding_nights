import click
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task"""
    tasks = load_tasks()
    tasks.append({"task":task, "completed":False})
    save_tasks(tasks)
    click.echo(f"Task '{task}' added successfully.")


@click.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo("Invalid task number. Please try again.")

@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        delete_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task '{delete_task['task']}' deleted successfully.")
    else:
        click.echo("Invalid task number. Please try again.")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
