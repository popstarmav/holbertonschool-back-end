#!/usr/bin/python3
import requests
import csv
import sys

def get_employee_todo_progress(employee_id):
    api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(api_url)

    if response.status_code == 200:
        todos = response.json()
        employee_name = todos[0]['username']
        completed_tasks = sum(1 for todo in todos if todo['completed'])
        total_tasks = len(todos)

        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")

        export_to_csv(employee_id, employee_name, todos)
    else:
        print(f"Error: Unable to fetch TODO list for employee {employee_id}")

def export_to_csv(employee_id, employee_name, todos):
    csv_filename = f"{employee_id}.csv"
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)

        for todo in todos:
            csv_writer.writerow([employee_id, employee_name, str(todo['completed']), todo['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
