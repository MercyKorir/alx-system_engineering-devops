#!/usr/bin/python3
"""Returns info about to-do list progress for given employee ID"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)
    name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id)
    response = requests.get(todos_url)
    todos = json.loads(response.text)
    names = requests.get(name_url)
    name_data = json.loads(names.text)
    completed_tasks = 0
    for todo in todos:
        if todo.get("completed") is True:
            completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(
        name_data.get("name"), completed_tasks, len(todos)))
    for todo in todos:
        if todo.get("completed") is True:
            print('\t {}'.format(todo.get("title")))
