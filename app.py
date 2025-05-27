from flask import Flask, render_template, request, redirect, send_file
import tasks
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    all_tasks = tasks.read_tasks()
    return render_template('index.html', tasks=all_tasks)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    date = request.form['date']
    category = request.form['category']
    tasks.add_task(title, date, category)
    return redirect('/')

@app.route('/delete/<task_id>')
def delete(task_id):
    tasks.delete_task(task_id)
    return redirect('/')

@app.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        category = request.form['category']
        completed = 'completed' in request.form
        tasks.update_task(task_id, title, date, category, str(completed))
        return redirect('/')
    else:
        all_tasks = tasks.read_tasks()
        task = next((t for t in all_tasks if t['id'] == task_id), None)
        return render_template('edit_task.html', task=task)

@app.route('/export')
def export():
    file_path = os.path.join('data', 'tasks.csv')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
