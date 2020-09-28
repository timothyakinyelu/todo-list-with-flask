import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())
    
cur = connection.cursor()

cur.execute('INSERT INTO tasks (title, content) VALUES(?, ?)', ('Write Todo App', 'Write a todo app with python and flask'))
cur.execute('INSERT INTO tasks (title, content) VALUES(?, ?)', ('Start Week 3', 'Start week 3 of automation course on coursera'))
cur.execute('INSERT INTO tasks (title, content, urgency) VALUES(?, ?, ?)', ('Find food', 'Make garri to drink before groundnut spoils', 'HIGH'))

connection.commit()
connection.close()