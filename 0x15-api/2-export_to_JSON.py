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

    file_name = "{}.json".format(employee_id)
    with open(file_name, 'w') as jsonfile:
        json.dump({employee_id: [{
            "task": item.get("title"),
            "completed": item.get("completed"),
            "username": name_data.get("username")
            } for item in todos]}, jsonfile)
