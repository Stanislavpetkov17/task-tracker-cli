import json

#open json
with open("tasks.json", "r") as file:
    tasks = json.load(file)
while True:
    command = input("\n1:Add\n2:Update\n3:Delete\n4:Clear\n5:List\n6:Exit\nChoose an action: ")

    #clear the whole thing
    if command == "4":
        tasks = []

    #add new task
    if command == "1":
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

    if command == "5":
        print()
        print(tasks)
    if command == "6":
        break


