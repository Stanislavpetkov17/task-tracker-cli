import json

#open json
with open("tasks.json", "r") as file:
    tasks = json.load(file)

command = input("Add, Update, Delete or Clear: ")

#clear the whole thing
if command == "Clear" or command == "clear":
    tasks = []




#add new task
if command == "Add" or command == "add":
    task = {}
    description = input("Add task: ")  #add the
    task["description"] = description  #description
    tasks.append(task)                 #append new task to list
    id = task["id"] = len(tasks)       #add ID



#write to json
with open("tasks.json", "w") as file:
    json.dump(tasks, file)

print(tasks)


