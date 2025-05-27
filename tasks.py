import csv
import os

DATA_FILE = os.path.join('data', 'tasks.csv')
FIELDNAMES = ['id', 'title', 'date', 'category', 'completed']

def read_tasks():
    tasks = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                tasks.append(row)
    return tasks

def write_tasks(tasks):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(tasks)

def add_task(title, date, category):
    tasks = read_tasks()
    task_id = str(len(tasks) + 1)
    tasks.append({'id': task_id, 'title': title, 'date': date, 'category': category, 'completed': 'False'})
    write_tasks(tasks)

def delete_task(task_id):
    tasks = [t for t in read_tasks() if t['id'] != task_id]
    write_tasks(tasks)

def update_task(task_id, title, date, category, completed):
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = title
            task['date'] = date
            task['category'] = category
            task['completed'] = completed
    write_tasks(tasks)
