import json

def add_new_task(task):
    with open('data/tasks.json', 'r') as f:
        tasks = json.load(f)

    task['id'] = len(tasks)  + 1
    tasks.append(task)

    with open('data/tasks.json', 'w') as file:
        json.dump(tasks, file)
