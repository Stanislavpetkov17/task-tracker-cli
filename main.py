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

    #new id algo
    highest_id = 0
    for existing_task in tasks:
        if existing_task["id"] > highest_id:
            highest_id = existing_task["id"]
    new_id = highest_id + 1

    task["id"] = new_id            #add ID
    tasks.append(task)             #append new task to list

#write to json
with open("tasks.json", "w") as file:
    json.dump(tasks, file)

print(tasks)


