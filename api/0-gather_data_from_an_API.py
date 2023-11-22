#!/usr/bin/python3
"""
place holder
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    user_id = argv[1]

    # Fetch all tasks for the user
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    )
    name_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={user_id}"
    )

    name_data = name_response.json()
    name = name_data[0]["name"] if name_data else None

    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]

    total_tasks = len(completed_tasks)

    todo_list = [f"\t{task['title']}" for task in completed_tasks]

    print(f"Employee {name} is done with tasks({total_tasks}/20):")

    for task in todo_list:
        print(task)
