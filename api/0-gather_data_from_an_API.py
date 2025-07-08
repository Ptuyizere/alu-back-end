#!/usr/bin/python3
"""
This module fetches and displays the TODO list progress of a given employee from a placeholder API.
"""

import requests
import sys

def get_emp_todo_progress(emp_id):
    """
    Fetch and display the TODO list progress for the given employee ID.
    Args:
        emp_id (int): ID of the employee
    """
    
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{emp_id}"
    todos_url = f"{base_url}/todos?userId={emp_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_name = user_data.get("name")
    if not employee_name:
        return

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")



if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        emp_id = int(sys.argv[1])
        get_emp_todo_progress(emp_id)
