#!/usr/bin/python3
"""
Dictionary of list of dictionaries
"""

import requests
import json

if __name__ == "__main__":
    # Fetch all users
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = users_response.json()

    result = {}

    for user in users_data:
        # Fetch tasks for each user
        todos_response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={user['id']}"
        )
        todos_data = todos_response.json()

        result[user["id"]] = []
        
        for todo in todos_data:
            result[user["id"]].append(
                {"username": user["username"],
                 "task": todo["title"], "completed": todo["completed"]}
            )

    # Create JSON file
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as result_file:
        json.dump(result, result_file)

    print(f"Data exported to {file_name}")
