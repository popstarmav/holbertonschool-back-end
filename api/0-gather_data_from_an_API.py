#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

def get_user_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    return response.json() if response.ok else None

def get_todo_data(employee_id):
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todo_url)
    return response.json() if response.ok else None

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit()

    employee_id = int(argv[1])

    user_data = get_user_data(employee_id)
    todo_data = get_todo_data(employee_id)

    if not user_data or not todo_data:
        print("Error: Unable to fetch data.")
        exit()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    print(f"Employee {user_data['name']} is done with tasks({completed_tasks}/{total_tasks}):")

    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")
