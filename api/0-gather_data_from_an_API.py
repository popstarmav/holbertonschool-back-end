#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and 
exports the data in CSV format.
"""

import requests
import csv
from sys import argv


def get_user_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    return requests.get(user_url).json() if requests.get(user_url).ok else None


def get_todo_data(employee_id):
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    return requests.get(todo_url).json() if requests.get(todo_url).ok else None


def export_to_csv(user_data, todo_data):
    if not user_data or not todo_data:
        print("Error: Unable to fetch data.")
        return

    user_id, username = user_data['id'], user_data['username']
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({'USER_ID': user_id, 'USERNAME': username,
                             'TASK_COMPLETED_STATUS': str(task['completed']),
                             'TASK_TITLE': task['title']})

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print(f"Usage: {argv[0]} employee_id")
        exit()

    employee_id = int(argv[1])

    user_data = get_user_data(employee_id)
    todo_data = get_todo_data(employee_id)

    if not user_data or not todo_data:
        print("Error: Unable to fetch data.")
        exit()

    total_tasks, completed_tasks = len(todo_data), sum(1 for task in todo_data if task['completed'])

    print(f"Employee {user_data['name']} is done with tasks("
          f"{completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")

    export_to_csv(user_data, todo_data)

