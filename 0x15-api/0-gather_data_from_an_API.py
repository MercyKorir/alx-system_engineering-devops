#!/usr/bin/python3
"""Returns information about todo list progress for given employee ID."""
import json
import sys
import urllib.request


def get_todo_list(employee_id):
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    name_url = "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id)
    name_response = urllib.request.urlopen(name_url)
    name_data = json.loads(name_response.read())
    employee_name = name_data["name"]
    completed_tasks = 0
    total_tasks = len(data)
    completed_task_title = []
    for task in data:
        if task["completed"] is True:
            completed_tasks += 1
            completed_task_title.append(task["title"])
    print("Employee " + employee_name + " is done with " +
          "tasks(" + str(completed_tasks) + "/" + str(total_tasks) + "):")
    for task in completed_task_title:
        print("\t" + task)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_todo_list(employee_id)
