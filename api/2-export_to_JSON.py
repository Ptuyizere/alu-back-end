#!/usr/bin/python3
"""
0-gather_data_from_an_API.py module

This module interacts with the JSONPlaceholder API to retrieve and display
TODO list progress for a given employee ID and exports to a JSON file.

Features:
- Connects to the JSONPlaceholder API (https://jsonplaceholder.typicode.com)
- Retrieves the employee's name and their TODO tasks
- Calculates the number of completed tasks
- Displays the progress and titles of completed tasks
- Exports all tasks (completed and not) to a JSON file

Usage:
    Run this module from the command line with an integer employee ID:

        $ python3 0-gather_data_from_an_API.py <employee_id>

Example:
    $ python3 0-gather_data_from_an_API.py 2
    Employee Ervin Howell is done with tasks(8/20):
         distinctio vitae autem nihil ut molestias quo
         adipisci atque cum quia aspernatur totam laudantium et
         ...

Note:
- This script must not be executed on import.
- All dictionary access uses `.get()` to avoid exceptions.
- Follows PEP 8 coding standards.
"""


import json
import requests
import sys


def get_employee_todo_progress(emp_id):
    """
    Fetch and display the TODO list progress and export to JSON.

    Args:
        emp_id (int): ID of the employee
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{emp_id}'
    todos_url = f'{base_url}/todos?userId={emp_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    emp_name = user_data.get('name')
    username = user_data.get('username')
    if not emp_name:
        return

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed') is True]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {emp_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Export to JSON
    json_data = {
            str(emp_id): [
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                }
                for task in todos_data
            ]
    }

    filename = f"{emp_id}.json"
    with open(filename, mode='w', encoding='utf-8') as jsonFile:
        json.dump(json_data, jsonFile)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        emp_id = int(sys.argv[1])
        get_employee_todo_progress(emp_id)
