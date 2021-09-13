#!/usr/bin/python3
''' Uses REST API, and for an employee ID, gives its information. '''


if __name__ == '__main__':
    import sys
    import requests

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    url_user = base_url + 'users/{}'.format(employee_id)
    url_todo = base_url + 'todos'
    info_user = requests.get(url_user).json()
    all_todo = requests.get(url_todo).json()

    name = info_user.get('name')
    total_todo = 0
    done_todo = 0
    tasks_done = []

    for todo in all_todo:
        if todo.get('userId') == int(employee_id):
            total_todo += 1
            if todo.get('completed') is True:
                done_todo += 1
                tasks_done.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name,
        done_todo,
        total_todo))
    for task in tasks_done:
        print('\t', task)
