import json

#open json
with open("tasks.json", "r") as file:
    tasks = json.load(file)

#add new task
task = {}
description = input("Add task: ")
task["description"] = description
tasks.append(task)

#write to json
with open("tasks.json", "w") as file:
    json.dump(tasks, file)

print(tasks)


