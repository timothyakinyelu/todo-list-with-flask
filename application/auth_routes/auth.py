from flask import render_template, Blueprint, redirect, url_for, request, flash
from flask_login import login_required, logout_user
from werkzeug.exceptions import abort
from application.models import *
from application.db import session

auth = Blueprint('auth', __name__)
TaskType = task_types.TaskType
Task = tasks.Task

def get_task_type(name):
    task_type = TaskType.query.filter_by(name=name).first()
    return task_type

def get_task_types():
    task_types = TaskType.query.all()
    return task_types


@auth.route('/')
@login_required
def index():
    taskTypes = get_task_types()

    tasks = session.query(TaskType).join(Task, Task.task_type_id == Task.id).all()

    return render_template('index.html', types=tasks)

    
@auth.route('/todos-detail/<name>', methods=['GET', 'POST'])
@login_required
def taskDetails(name):
    taskType = get_task_type(name)
    
    tasks = Task.query.filter_by(task_type_id = taskType.id).all()
    
    return render_template('todo-detail.html', tasks=tasks)


@auth.route('/create-type', methods=['POST',])
@login_required
def createType():
    if request.method == 'POST':
        name = request.form['name']
        
        existing_type = TaskType.query.filter_by(name=name).first()
        
        
        if existing_type:
            flash('Group already exists!')
            return redirect(url_for('auth.index'))

        new_type = TaskType(
            name = name
        )
        session.add(new_type)
        session.commit()
        
        return redirect(url_for('auth.index'))
    

@auth.route('/create-task', methods=['POST',])
@login_required
def createTask():
    if request.method == 'POST':
        taskTypeId = request.form['taskTypeId']
        title = request.form['title']
        content = request.form['content']
        priority = request.form['priority']
        
        if not taskTypeId:
            flash('Please select a task type')
        elif not title:
            flash('Please input a title for the task')
        else:
            task = Task(
                task_type_id = taskTypeId,
                title = title,
                content = content,
                priority = priority
            )
            
            session.add(task)
            session.commit()
            
            return redirect(url_for('auth.index'))

    
@auth.route('/check-complete/<int:id>', methods=['POST',])
@login_required
def checkComplete(id):
    if request.method == 'POST':
        completed = 'check' in request.form

        if completed == True:
            checked = 1
        else:
            checked = 0
        
        session.query(Task).filter(Task.id == id).update({Task.completed: checked}, synchronize_session = False)
        session.commit()
        
        return redirect(url_for('auth.index'))
    

@auth.route('/delete-task/<int:id>', methods=['POST',])
@login_required
def deleteTask(id):
    taskType = request.form['grpName']
    
    Task.query.filter_by(id=id).delete()
    flash('Task Deleted Sucessfully')
    
    return redirect(url_for('taskDetails', name=taskType))
   
 
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('nonAuth.login'))