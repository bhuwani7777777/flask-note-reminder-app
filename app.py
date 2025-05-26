from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

TASKS_CSV = 'data/tasks.csv'
TRANSACTIONS_CSV = 'data/transactions.csv'

# Ensure data directory and CSV files exist
os.makedirs('data', exist_ok=True)
for file, headers in [(TASKS_CSV, ['Date', 'Task']), (TRANSACTIONS_CSV, ['Date', 'Description', 'Amount'])]:
    if not os.path.exists(file):
        with open(file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

def read_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_task(date, task):
    with open(TASKS_CSV, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, task])

def write_transaction(date, description, amount):
    with open(TRANSACTIONS_CSV, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, description, amount])

@app.route('/')
def index():
    tasks = read_csv(TASKS_CSV)
    transactions = read_csv(TRANSACTIONS_CSV)
    return render_template('index.html', tasks=tasks, transactions=transactions)

@app.route('/daily_tasks')
def daily_tasks_view():
    tasks = read_csv(TASKS_CSV)
    return render_template('daily_tasks.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    date = request.form['date']
    task = request.form['task']
    write_task(date, task)
    return redirect(url_for('daily_tasks_view'))

@app.route('/transactions')
def transactions_view():
    transactions = read_csv(TRANSACTIONS_CSV)
    return render_template('transactions.html', transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']
    write_transaction(date, description, amount)
    return redirect(url_for('transactions_view'))

if __name__ == '__main__':
    app.run(debug=True)
