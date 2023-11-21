#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    employee_id = int(argv[1])

    # Fetch user data
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todo_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        # Count completed and total tasks
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        # Display information
        print(f"Employee {user_data['name']} is done with tasks("
              f"{completed_tasks}/{total_tasks}):")
        for task in todo_data:
            if task['completed']:
                print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
