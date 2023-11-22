#!/usr/bin/python3
"""
Export to JSON
"""

import requests
from sys import argv
import json

if __name__ == "__main__":
    if len(argv) < 2:
        exit()

    user_id = argv[1]

    # Fetch all tasks for the user
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    )
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={user_id}"
    )

    user_data = user_response.json()
    user_name = user_data[0]["username"] if user_data else None

    todos_data = todos_response.json()

    # Create JSON file
    result = {}
    result[user_id] = []

    for todo in todos_data:
        result[user_id].append(
            {"task": todo["title"], "completed": todo["completed"],
             "username": user_name}
        )

    file_name = f"{user_id}.json"
    with open(file_name, 'w') as result_file:
        json.dump(result, result_file)

    print(f"Data exported to {file_name}")
