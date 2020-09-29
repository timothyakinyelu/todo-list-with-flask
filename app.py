from itertools import groupby
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.static_folder = 'static'

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

@app.route("/todo-detail")
def detail():
    return render_template('todo-detail.html')

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
    # return render_template('create.html', types=task_types)
        

if __name__ == "__main__":
    app.run(debug=True)
