#!/usr/bin/python3
''' Uses REST API, and for an employee ID, gives its information. '''


if __name__ == '__main__':
    import json
    import sys
    import requests

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    url_user = base_url + 'users/{}'.format(employee_id)
    url_todo = base_url + 'todos'
    info_user = requests.get(url_user).json()
    all_todo = requests.get(url_todo).json()

    username = info_user.get('username')
    employee_json = {}

    with open('{}.json'.format(employee_id), 'w+') as file:
        tasks = []
        for todo in all_todo:
            if todo.get('userId') == int(employee_id):
                task = {}
                task['task'] = todo.get('title')
                task['completed'] = todo.get('completed')
                task['username'] = username
                tasks.append(task)
        employee_json[employee_id] = tasks
        file.write(json.dumps(employee_json))
