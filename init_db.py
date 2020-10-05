# import sqlite3
import hashlib
from werkzeug.security import generate_password_hash
from application.models.users import User
from application.models.task_types import TaskType
from application.models.tasks import Task

# connection = sqlite3.connect()
    
password1 = hashlib.sha256('password'.encode()).hexdigest()
# cur = connection.cursor()

# cur.execute('INSERT INTO task_types (name) VALUES(?)', ('Personal',))
# cur.execute('INSERT INTO task_types (name) VALUES(?)', ('Work',))
# cur.execute('INSERT INTO task_types (name) VALUES(?)', ('Study',))

# cur.execute('INSERT INTO users (email, first_name, last_name, password) VALUES(?, ?, ?, ?)', ('lee.juniper@xo.com', 'Juniper', 'Lee', "password1"))
# # cur.execute('INSERT INTO users (email, first_name, last_name, password) VALUES(?, ?, ?, ?)', ('hills.lauretta@xo.com', 'Lauretta', 'Hills', sha256('secret'))

# cur.execute('INSERT INTO tasks (user_id, task_type_id, title, content) VALUES(?, ?, ?, ?)', (1, 2, 'Write Todo App', 'Write a todo app with python and flask'))
# cur.execute('INSERT INTO tasks (user_id, task_type_id, title, content) VALUES(?, ?, ?, ?)', (1, 2, 'Write GraphQL Pagination', 'Write a data table code with windowed pagination with ApolloClient'))
# cur.execute('INSERT INTO tasks (user_id, task_type_id, title, content) VALUES(?, ?, ?, ?)', (1, 3, 'Start Week 3', 'Start week 3 of automation course on coursera'))
# cur.execute('INSERT INTO tasks (user_id, task_type_id, title, content) VALUES(?, ?, ?, ?)', (1, 3, 'Start Week 3', 'Start week 3 of automation course on coursera'))
# cur.execute('INSERT INTO tasks (user_id, task_type_id, title, content) VALUES(?, ?, ?, ?)', (1, 3, 'HackerRank Tests', 'Take tests to move up a level'))
# cur.execute('INSERT INTO tasks (user_id, task_type_id, title, content, priority) VALUES(?, ?, ?, ?)', (1, 1, 'Find food', 'Make garri to drink before groundnut spoils', 'HIGH'))

# connection.commit()
# connection.close()

User(
    email = 'lee.juniper@xo.com',
    first_name = 'Juniper',
    last_name = 'Lee',
    password = generate_password_hash('password', method='sha256')
)
User(
    email = 'hills.lauretta@xo.com',
    first_name = 'Lauretta',
    last_name = 'Hills',
    password = generate_password_hash('secret', method='sha256')
)

TaskType(
    name = 'Personal'
)
TaskType(
    name = 'Work'
)
TaskType(
    name = 'Study'
)

Task(
    user_id = 1,
    task_type_id = 2,
    title = 'Write Todo App',
    content = 'Write a todo app with python and flask'
)
Task(
    user_id = 1,
    task_type_id = 2,
    title = 'Write GrapQL Pagination',
    content = 'Write a data table code with windowed pagination with ApolloClient'
)
Task(
    user_id = 1,
    task_type_id = 3,
    title = 'Start week 4',
    content = 'Start week 4 of automation course on coursera'
)
Task(
    user_id = 2,
    task_type_id = 3,
    title = 'Study Regex',
    content = 'Read up some more about regex'
)
Task(
    user_id = 2,
    task_type_id = 1,
    title = 'Find Food',
    content = 'Look for something to eat'
)
Task(
    user_id = 1,
    task_type_id = 1,
    title = 'Cook Rice',
    content = 'Make jollof rice'
)
Task(
    user_id = 2,
    task_type_id = 2,
    title = 'Add Authentication to app',
    content = 'Add authentication to todo app'
)