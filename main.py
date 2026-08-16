import json
import datetime

#open json
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []
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
        task["createdAt"] = datetime.datetime.now().strftime("%x-%H:%M") 
        tasks.append(task)             #append new task to list

    #update task
    elif command == "2":
        id_to_update = input("Enter task ID: ")
        try:
            id_to_update = int(id_to_update)
        except ValueError:
            print("\nPlease enter a valid ID")
        else:
            #find task with inputted id
            found_task = False
            for task_to_update in tasks:
                if task_to_update["id"] == id_to_update:
                    found_task = True
                    while True:
                        update_choice = input("Description:1\nStatus:2\nGo Back:3\nChoose attribute to update: ")
                        #update description
                        if update_choice == "1":
                            new_description = input("Enter new description: ")
                            task_to_update["description"] = new_description
                            task_to_update["updatedAt"] = datetime.datetime.now().strftime("%x-%H:%M")
                        #update status
                        elif update_choice == "2":
                            new_status = input("1:To-Do\n2:In-Progress\n3:Completed\nChoose new status: ")
                            if new_status == "1":
                                task_to_update["status"] = "To-Do"
                                task_to_update["updatedAt"] = datetime.datetime.now().strftime("%x-%H:%M")
                            elif new_status == "2":
                                task_to_update["status"] = "In-Progress"
                                task_to_update["updatedAt"] = datetime.datetime.now().strftime("%x-%H:%M")
                            elif new_status == "3":
                                task_to_update["status"] = "Completed"
                                task_to_update["updatedAt"] = datetime.datetime.now().strftime("%x-%H:%M")                
                            else:
                                print("Please enter a valid status")
                        elif update_choice == "3":
                            break
                        else:
                            print("\nPlease enter a valid attribute")
            if found_task == False:
                print("\nPlease enter a valid ID")

    #delete task
    elif command == "3":
        try:
            id_to_delete = int(input("Enter task ID: "))
        except ValueError:
                    print("\nPlease enter a valid ID")
        else:
            found_value_del = False
            #find task with inputted id
            for task_to_delete in tasks:
                if task_to_delete["id"] == id_to_delete:
                    if input("Are you sure? y/n\n") == "y":
                        found_value_del = True
                        tasks.remove(task_to_delete)
                        break
                    else:
                        found_value_del = True
                        break
            if found_value_del == False:
                print("\nPlease enter a valid ID")

    elif command == "4": #clear
        if input("Are you sure? y/n\n") == "y":
            tasks = []

    elif command == "5": #list
        while True:
            status_to_list = input("\nList all:1\nList To-Do:2\nList In-Progress:3\nList Completed:4\nGo Back:5\nChoose an action: ")
            found_task_ls = False
            if status_to_list in ["1", "2", "3", "4", "5"]:
                for task_to_list in tasks:
                    if status_to_list == "1":
                        print(task_to_list)
                        found_task_ls = True
                    elif status_to_list == "2":
                        if task_to_list["status"] == "To-Do":
                            print(task_to_list)
                            found_task_ls = True
                    elif status_to_list == "3":
                        if task_to_list["status"] == "In-Progress":
                            print(task_to_list)
                            found_task_ls = True
                    elif status_to_list == "4":
                        if task_to_list["status"] == "Completed":
                            print(task_to_list)
                            found_task_ls = True
                if status_to_list == "5":
                    break
                if found_task_ls == False:
                    print("\nNo tasks found")
            else:
                print("\nPlease enter a valid option")

    elif command == "6": #exit
        break

    else:
        print("\nPlease enter a valid option")
    #save to json
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)