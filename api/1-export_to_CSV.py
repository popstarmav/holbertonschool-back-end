#!/usr/bin/python3
"""
place holder
"""

import requests
import csv
from sys import argv

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

    # Create CSV file
    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write tasks data
        for task in todos_data:
            csv_writer.writerow([user_id, user_name, str(task['completed']), task['title']])

    print(f"Data exported to {csv_file_name}")
