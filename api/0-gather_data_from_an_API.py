#!/usr/bin/python3
"""
place holder
"""

if __name__ == "__main__":

    import requests
    from sys import argv
    if len(argv) < 2:
        exit()

    user_id = argv[1]

    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?"
        f"userId={user_id}&completed=true"
    )
    name_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users?id={user_id}"
    )
    todos_data = todos_response.json()
    name_data = name_response.json()

    name = name_data[0]["name"] if name_data else None
    total_tasks = len(todos_data)

    todo_list = []

    for task in todos_data:
        todo_list.append(f"\t{task['title']}")

    print(f"Employee {name} is done with tasks({total_tasks}/{total_tasks}):")

    for task in todo_list:
        print(task)
