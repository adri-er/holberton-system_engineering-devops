#!/usr/bin/python3
''' Uses REST API, and for an employee ID, gives its information. '''


if __name__ == '__main__':
    import requests
    import sys

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'
    url_user = base_url + 'users/{}'.format(employee_id)
    url_todo = base_url + 'todos'
    info_user = requests.get(url_user).json()
    all_todo = requests.get(url_todo).json()

    username = info_user.get('username')

    with open('{}.csv'.format(employee_id), 'w+') as file:
        for todo in all_todo:
            if todo.get('userId') == int(employee_id):
                line = ""
                line += '\"{}\"'.format(employee_id) + ","
                line += '\"{}\"'.format(username) + ","
                line += '\"{}\"'.format(todo.get('completed')) + ","
                line += '\"{}\"\n'.format(todo.get('title'))
                file.write(line)
