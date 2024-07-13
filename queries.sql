-- Query 1: Find 5 students with the highest average grade across all subjects.
SELECT s.name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 5;

-- Query 2: Find the student with the highest average grade in a specific subject.
-- Replace '1' with the actual subject_id for the specific subject.
SELECT s.name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 1
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;

-- Query 3: Find the average grade in groups for a specific subject.
-- Replace '1' with the actual subject_id for the specific subject.
SELECT g.name, AVG(gr.grade) AS avg_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gr ON s.id = gr.student_id
WHERE gr.subject_id = 1
GROUP BY g.id;

-- Query 4: Find the average grade across all subjects.
SELECT AVG(grade) AS avg_grade
FROM grades;

-- Query 5: Find the courses taught by a specific teacher.
-- Replace '1' with the actual teacher_id for the specific teacher.
SELECT name
FROM subjects
WHERE teacher_id = 1;

-- Query 6: Find the list of students in a specific group.
-- Replace '1' with the actual group_id for the specific group.
SELECT name
FROM students
WHERE group_id = 1;

-- Query 7: Find the grades of students in a specific group for a specific subject.
-- Replace '1' with the actual group_id and '1' with the actual subject_id.
SELECT s.name, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 1
AND g.subject_id = 1;

-- Query 8: Find the average grade given by a specific teacher in their subjects.
-- Replace '1' with the actual teacher_id for the specific teacher.
SELECT AVG(g.grade) AS avg_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
WHERE s.teacher_id = 1;

-- Query 9: Find the list of courses attended by a specific student.
-- Replace '1' with the actual student_id for the specific student.
SELECT DISTINCT sub.name
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
WHERE g.student_id = 1;

-- Query 10: Find the courses a specific student is taught by a specific teacher.
-- Replace '1' with the actual student_id and '1' with the actual teacher_id.
SELECT DISTINCT sub.name
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
WHERE g.student_id = 1
AND sub.teacher_id = 1;
