from itertools import groupby
import sqlite3
import arrow
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.exceptions import abort
from momentjs import momentjs

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_task_type(name):
    conn = get_db_connection()
    task_type = conn.execute('SELECT * FROM task_types WHERE name = ?', (name,)).fetchone()
    
    conn.close()
    
    if task_type is None:
        abort(404)
    return task_type

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Something Secret'
app.add_template_global(name='momentjs', f=momentjs)

@app.route("/")
def index():
    conn = get_db_connection()
    task_types = conn.execute('SELECT * FROM task_types').fetchall()
    tasks = conn.execute(
        'SELECT i.*, t.name FROM tasks i JOIN task_types t ON i.task_type_id = t.id ORDER BY t.name'
    ).fetchall()
    
    lists = {}
    for k, g in groupby(tasks, key=lambda t: t['name']):
        lists[k] = list(g)
     
    conn.close()
    return render_template('index.html', lists=lists, types=task_types)

@app.route("/todos-detail/<string:name>", methods=('GET', 'POST'))
def taskDetails(name):
    task_type = get_task_type(name)
    
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks WHERE task_type_id = ?', (task_type['id'],)).fetchall()
    
    return render_template('todo-detail.html', tasks=tasks)

@app.route("/create-task", methods=('POST',))
def createTask():
    if request.method == 'POST':
        task_type_id = request.form['task_type_id']
        title = request.form['title']
        content = request.form['content']
        priority = request.form['priority']
        
        if not task_type_id:
            flash('Task Type is required')
        elif not title:
            flash('Title is required')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO tasks (task_type_id, title, content, priority) VALUES(?, ?, ?, ?)', (task_type_id, title, content, priority))
            
            conn.commit()
            conn.close()
            
            return redirect(url_for('index'))
        
@app.route("/delete-task/<int:id>", methods=('POST',))
def deleteTask(id):
    task_type = request.form['grpName']
    
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    flash("Task Deleted Successfully")
    return redirect(url_for('taskDetails', name=task_type))

@app.route("/check-complete/<int:id>", methods=('POST',))      
def checkComplete(id):
    if request.method == 'POST':
        completed = 'check' in request.form
        if completed == True:
            checked = 1
        else:
            checked = 0
            
        conn = get_db_connection()
        conn.execute('UPDATE tasks SET completed = ?''WHERE id = ?', (checked, id))
        
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    

if __name__ == "__main__":
    app.run(debug=True)
