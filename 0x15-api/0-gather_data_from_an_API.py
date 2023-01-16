#!/usr/bin/python3
"""This script uses REST API for given employee ID
and returns info on todolist progress"""
import json
import sys
import urllib.request


def get_todo_list(employee_id):
    # Makes a GET request to API and retrieves employee info
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    # Get the employee's name
    name_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    name_response = urllib.request.urlopen(name_url)
    name_data = json.loads(name_response.read())
    employee_name = name_data["name"]

    # Count the number of completed tasks
    completed_tasks = 0
    total_tasks = len(data)
    completed_task_title = []
    for task in data:
        if task["completed"] is True:
            completed_tasks += 1
            completed_task_title.append(task["title"])

    # Print the results
    print("Employee " + employee_name + " is done with " +
          "tasks(" + str(completed_tasks) + "/" + str(total_tasks) + "):")
    for task in completed_task_title:
        print("\t" + task)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_todo_list(employee_id)
