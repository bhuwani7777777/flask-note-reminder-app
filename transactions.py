import csv
import os

DATA_FILE = 'data/transactions.csv'

def ensure_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Description', 'Amount'])

def get_all_transactions():
    ensure_file()
    with open(DATA_FILE, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

def add_transaction(date, description, amount):
    ensure_file()
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, description, amount])
