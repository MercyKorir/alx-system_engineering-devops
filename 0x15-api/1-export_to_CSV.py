#!/usr/bin/python3
"""Returns info about to-do list progress for given employee ID"""
import csv
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
    csv_data = [[]]
    for item in todos:
        csv_data.append(
                [item.get("userId"), name_data.get("username"),
                    item.get("completed"), item.get("title")])
    file_name = "{}.csv".format(str(sys.argv[1]))
    with open(file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(csv_data)
