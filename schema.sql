DROP TABLE IF EXISTS task_types;
DROP TABLE IF EXISTS tasks;

CREATE TABLE task_types(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL

);

CREATE TABLE tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_type_id INTEGER NOT NULL,
    title VARCHAR NOT NULL,
    content TEXT NOT NULL,
    priority VARCHAR NOT NULL DEFAULT LOW,
    completed INTEGER NOT NULL DEFAULT 0,
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_type_id) REFERENCES task_types (id)
);