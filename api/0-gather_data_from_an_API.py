#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    user_id = argv[1]

    # Fetch completed tasks
    completed_todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}&completed=true"
    )
    completed_todos_data = completed_todos_response.json()

    # Fetch user data
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={user_id}"
    )
    user_data = user_response.json()
    user_name = user_data[0]["name"] if user_data else None

    # Fetch all tasks
    all_todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    )
    all_todos_data = all_todos_response.json()
    total_tasks = len(all_todos_data)

    todo_list = []

    for task in completed_todos_data:
        todo_list.append(f"\t {task['title']}")

    print(f"Employee {user_name} is done with tasks({len(completed_todos_data)}/{total_tasks}):")
    
    for task in todo_list:
        print(task)
