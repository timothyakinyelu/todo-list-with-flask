from itertools import groupby
import sqlite3
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    conn = get_db_connection()
    tasks = conn.execute(
        'SELECT i.*, t.name FROM tasks i JOIN task_types t ON i.task_type_id = t.id ORDER BY t.name'
    ).fetchall()
    
    lists = {}
    for k, g in groupby(tasks, key=lambda t: t['name']):
        lists[k] = list(g)  
     
    conn.close()
    return render_template('index.html', lists=lists)

@app.route("/todo-detail")
def detail():
    return render_template('todo-detail.html')

if __name__ == "__main__":
    app.run(debug=True)
