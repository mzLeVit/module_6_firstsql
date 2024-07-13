import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

# Connect to SQLite database
conn = sqlite3.connect('school.db')
cur = conn.cursor()

fake = Faker()

# Insert teachers
teachers = []
for _ in range(5):
    name = fake.name()
    cur.execute("INSERT INTO teachers (name) VALUES (?)", (name,))
    teachers.append(cur.lastrowid)

# Insert groups
groups = []
for i in range(3):
    name = f"Group {i + 1}"
    cur.execute("INSERT INTO groups (name) VALUES (?)", (name,))
    groups.append(cur.lastrowid)

# Insert students
students = []
for _ in range(50):
    name = fake.name()
    group_id = random.choice(groups)
    cur.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
    students.append(cur.lastrowid)

# Insert subjects
subjects = []
for i in range(8):
    name = fake.word().capitalize()
    teacher_id = random.choice(teachers)
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (name, teacher_id))
    subjects.append(cur.lastrowid)

# Insert grades
for student in students:
    for subject in subjects:
        for _ in range(random.randint(1, 20)):
            grade = random.randint(0, 100)
            date = fake.date_time_between(start_date='-1y', end_date='now')
            cur.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                        (student, subject, grade, date))

# Commit the transaction and close the connection
conn.commit()
conn.close()
