#!/usr/bin/python3
"""
Export to CSV
"""

import csv
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
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={user_id}"
    )

    user_data = user_response.json()
    user_name = user_data[0]["username"] if user_data else None

    todos_data = todos_response.json()

    # Create CSV file
    file_name = f"{user_id}.csv"
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)

        # Write header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write tasks data
        for todo in todos_data:
            csv_writer.writerow([user_id, user_name, str(todo['completed']), todo['title']])

    print(f"Data exported to {file_name}")
