#Modify
import json
import os
#add a task to the todo list
def addTask():
    with open('tasks.json', 'r+') as file:
        data = json.load(file)
        taskName = input("What is your new task: ")
        taskDesc = input("Please describe the task: ")
        max_task_num = max(task['taskNum'] for task in data['tasks'])
        new_task = {
            "taskNum": max_task_num + 1,
            "name": taskName,
            "description": taskDesc
        }
        data["tasks"].append(new_task)
        file.seek(0)  # Move the file cursor to the beginning
        file.truncate()  # Clear the file content
        
        json.dump(data, file, indent=4)
        print(f"New task added: {new_task['name']} -> {new_task['description']}")


#get rid of a task that is not completed 
def removeTask(taskNum):
    with open('tasks.json', 'r+') as file:
        data = json.load(file)
        for task in data['tasks']:
            if task['taskNum'] == taskNum:
                print(f"{task['name']}  ->  {task['description']} - Completed")
                data['tasks'].remove(task)
                break
        sorted_tasks = sorted(data['tasks'], key=lambda task: task['taskNum'])
        for index, task in enumerate(sorted_tasks):
            task['taskNum'] = index + 1
        data['tasks'] = sorted_tasks
        
        file.seek(0)  # Move the file cursor to the beginning
        file.truncate()  # Clear the file content
        json.dump(data, file, indent=4)


#get the tasks from file
def loadTask(taskNum):
    with open('tasks.json') as file:
        data = json.load(file)
    for task in data['tasks']:
        if taskNum == task['taskNum']:
            print(f"\n\n{task['name']}  ->  {task['description']}")
    cont = input("\nPress any button to continue...")

#Show the name of the tasks
def displayTaskName():
    with open('tasks.json') as file:
        data = json.load(file)  
    for task in data['tasks']:
        print(f"{task['taskNum']}. {task['name']}")

#Edit the task 
def editTaskName(taskNum):
    with open('tasks.json', 'r+') as file:
        data = json.load(file)
        newName = input("New Name: ")
        for task in data['tasks']:
            if taskNum == task['taskNum']: 
                task['name'] = newName

        file.seek(0)  # Move the file cursor to the beginning
        file.truncate()  # Clear the file content
        json.dump(data, file, indent=4)

def editTaskDesc(taskNum):
    with open('tasks.json', 'r+') as file:
        data = json.load(file)
        newDesc = input("New Description: ")
        for task in data['tasks']:
            if taskNum == task['taskNum']: 
                task['name'] = newDesc

        file.seek(0)  # Move the file cursor to the beginning
        file.truncate()  # Clear the file content
        json.dump(data, file, indent=4)