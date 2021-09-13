#!/usr/bin/python3
''' Uses REST API, and for an employee ID, gives its information. '''


if __name__ == '__main__':
    import json
    import requests

    base_url = 'https://jsonplaceholder.typicode.com/'
    url_user = base_url + 'users'
    url_todo = base_url + 'todos'
    all_user = requests.get(url_user).json()
    all_todo = requests.get(url_todo).json()

    with open('todo_all_employees.json', 'w+') as file:
        employee_json = {}
        for user in all_user:
            username = user.get('username')

            tasks = []
            for todo in all_todo:
                if todo.get('userId') == user.get('id'):
                    task = {}
                    task['username'] = username
                    task['task'] = todo.get('title')
                    task['completed'] = todo.get('completed')
                    tasks.append(task)
                employee_json[str(user.get('id'))] = tasks
        file.write(json.dumps(employee_json))
