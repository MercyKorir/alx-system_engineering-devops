#!/usr/bin/python3
"""Returns info about to-do list progress for given employee ID"""
import json
import requests

if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId="
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url)
    users_data = json.loads(users.text)

    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as jsonfile:
        json.dump({user.get("id"): [{
            "username": user.get("username"),
            "task": item.get("title"),
            "completed": item.get("completed")
            } for item in json.loads(requests.get(
                todos_url + "{}".format(user.get("id"))).text)]
            for user in users_data}, jsonfile)
