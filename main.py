import json
task = {}
description = input("Add task: ")
task["description"] = description
tasks = json.dumps(task)
print(tasks)


