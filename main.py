import json

#open json
with open("tasks.json", "r") as file:
    tasks = json.load(file)
while True:
    command = input("\n1:Add\n2:Update\n3:Delete\n4:Clear\n5:List\n6:Exit\nChoose an action: ")

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
        task["status"] = "To-Do"       #add status
        tasks.append(task)             #append new task to list

    #update task
    if command == "2":
        id_to_update = input("Enter task ID: ")
        id_to_update = int(id_to_update) 
        #find task with inputted id
        for task_to_update in tasks:
            if task_to_update["id"] == id_to_update:
                #update status
                new_status = input("1:To-Do\n2:In-Progress\n3:Completed\nChoose new status: ")
                if new_status == "1":
                    task_to_update["status"] = "To-Do"
                if new_status == "2":
                    task_to_update["status"] = "In-Progress"
                if new_status == "3":
                    task_to_update["status"] = "Completed"

    if command == "4": #clear
        tasks = []

    if command == "5": #list
        print()
        print(tasks)
    if command == "6": #exit
        break

    #save to json
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
