import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    
cur = connection.cursor()

cur.execute('INSERT INTO task_types (name) VALUES(?)', ('Personal',))
cur.execute('INSERT INTO task_types (name) VALUES(?)', ('Work',))
cur.execute('INSERT INTO task_types (name) VALUES(?)', ('Study',))

cur.execute('INSERT INTO tasks (task_type_id, title, content) VALUES(?, ?, ?)', (2, 'Write Todo App', 'Write a todo app with python and flask'))
cur.execute('INSERT INTO tasks (task_type_id, title, content) VALUES(?, ?, ?)', (2, 'Write GraphQL Pagination', 'Write a data table code with windowed pagination with ApolloClient'))
cur.execute('INSERT INTO tasks (task_type_id, title, content) VALUES(?, ?, ?)', (3, 'Start Week 3', 'Start week 3 of automation course on coursera'))
cur.execute('INSERT INTO tasks (task_type_id, title, content) VALUES(?, ?, ?)', (3, 'HackerRank Tests', 'Take tests to move up a level'))
cur.execute('INSERT INTO tasks (task_type_id, title, content, priority) VALUES(?, ?, ?, ?)', (1, 'Find food', 'Make garri to drink before groundnut spoils', 'HIGH'))

connection.commit()
connection.close()