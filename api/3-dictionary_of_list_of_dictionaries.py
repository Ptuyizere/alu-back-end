#!/usr/bin/python3
"""
0-gather_data_from_an_API.py module

This module fetches TODO tasks for all employees from the API 
and exports to JSON formatt file.

Features:
- Connects to the JSONPlaceholder API (https://jsonplaceholder.typicode.com)
- Retrieves all users ID with tasks, usernames, and status
- Outputs to 'todo_all_employees.json' in the required structure

Usage:
    $ python3 3-dictionary_of_list_of_dictionaries.py

Output:
    todo_all_employees.json

Note:
- This script must not be executed on import.
- All dictionary access uses `.get()` to avoid exceptions.
- Follows PEP 8 coding standards.
"""


import json
import requests


def export_all_employees_todos():
    """
    Fetch all users and their TODO tasks, then export to a JSON file.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    user_dict = {user.get('id'): user.get('username') for user in users}

    all_todos = {}
    for todo in todos:
        user_id = todo.get("userId")
        username = user_dict.get(user_id)
        task_entry = {
            "username": username,
            "task": todo.get("title"),
            "completed": todo.get("completed")
        }

        if str(user_id) not in all_todos:
            all_todos[str(user_id)] = []
        all_todos[str(user_id)].append(task_entry)

    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="utf-8") as jsonFile:
        json.dump(all_todos, jsonFile)


if __name__ == "__main__":
    export_all_employees_todos()
