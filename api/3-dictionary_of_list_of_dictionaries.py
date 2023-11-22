#!/usr/bin/python3
import requests
import json

def get_all_employees_todo():
    # Define the API endpoint for fetching all users
    users_api_url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(users_api_url)

    if users_response.status_code == 200:
        users = users_response.json()

        # Dictionary to store tasks for all employees
        all_employees_tasks = {}

        # Iterate through each user to fetch tasks
        for user in users:
            employee_id = user['id']
            employee_name = user['username']

            # Define the API endpoint for fetching tasks for the current user
            todos_api_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
            todos_response = requests.get(todos_api_url)

            if todos_response.status_code == 200:
                todos = todos_response.json()

                # List to store tasks for the current employee
                employee_tasks = []

                for todo in todos:
                    task_info = {
                        "username": employee_name,
                        "task": todo['title'],
                        "completed": todo['completed']
                    }
                    employee_tasks.append(task_info)

                # Add tasks for the current employee to the dictionary
                all_employees_tasks[employee_id] = employee_tasks

            else:
                print(f"Error: Unable to fetch TODO list for employee {employee_id}")

        # Export data to JSON file
        export_to_json(all_employees_tasks)
    else:
        print("Error: Unable to fetch user data")

def export_to_json(data):
    # Define the JSON file name
    json_filename = "todo_all_employees.json"

    # Write data to JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    get_all_employees_todo()
