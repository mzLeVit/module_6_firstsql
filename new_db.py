import sqlite3
import os

# Specify the directory where the database should be created - can be relevant, I chose it to be exact as my
# parent folder is full of files. Easier to find the file I need :)
db_directory = 'E:\SQLfiles'
os.makedirs(db_directory, exist_ok=True)
db_path = os.path.join(db_directory, 'school.db')

# Connect to SQLite database at the specified path
conn = sqlite3.connect(db_path)

# Create a cursor object
cur = conn.cursor()

# Create tables
cur.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    CHECK (grade >= 0 AND grade <= 100)
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
