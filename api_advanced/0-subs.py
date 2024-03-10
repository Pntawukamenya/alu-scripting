#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
 returns the number of subscribers for a given subreddit.
"""
import requests

def get_emp_todo(emp_id):
    TODO_URL = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    USER_URL = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    
    # Get the JSON of TODOS - DONE
    # Get TOTAL NUMBER of todos - DONE
    # Get COMPLETED NUMBER of todos - DONE
    # Get THE NAME of the employee - DONE 

    # GET THE TITLES OF THE COMPLETED TASKS
    # AND PRINT THEM ALL OUT ON STDOUT
    # EACH TASKS SHOULD BE PRINTED ON A NEW LINE


    emp_todos = requests.get(TODO_URL).json()
    emp_name = requests.get(USER_URL).json()["name"]
    emp_total_todos = len(emp_todos)
    emp_completed_todos = 0
    todo_titles = []

    for todo in emp_todos:
        if todo["completed"] is True:
            todo_titles.append(todo["title"])
            emp_completed_todos += 1
    print(f"Employee {emp_name} From total todos of {emp_total_todos}, {emp_completed_todos} tasks have been done")

    for todo_title in todo_titles:
        print(todo_title)

get_emp_todo(1)
