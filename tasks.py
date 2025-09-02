import csv
import os

CSV_FILE = "tasks.csv"

def load_tasks():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            return [row[0] for row in reader]
    return []

def save_tasks(task_list):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])

