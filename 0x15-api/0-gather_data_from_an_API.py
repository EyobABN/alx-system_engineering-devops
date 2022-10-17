#!/usr/bin/python3
'''Gathers data from a given API
'''
import json
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'
"""The API's URL"""


if __name__ == "__main__":
    """
        Execute if not imported as a module
    """
    if (len(sys.argv) > 1):
        ID = sys.argv[1]
        x = requests.get(
                API_URL + '/users/' + ID + '/todos'
        )
        todos = json.loads(x.text)
        done = []
        numberOfTasks = 0
        numberOfDone = 0
        employee = json.loads(
                requests.get(
                    API_URL + '/users/' + ID
                ).text
        )
        nameOfEmployee = employee.get('name')
        for todo in todos:
            numberOfTasks += 1
            if todo.get('completed') is True:
                numberOfDone += 1
                done.append('\t ' + todo.get('title'))
        print(f'Employee {nameOfEmployee} is done with tasks\
({numberOfDone}/{numberOfTasks}):')
        [print(i) for i in done]
