import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('school.db')
cur = conn.cursor()

# Read the query from file
with open('queries.sql', 'r') as file:
    queries = file.read()

# Execute queries one by one
for query in queries.strip().split(';'):
    if query.strip():
        cur.execute(query.strip())
        results = cur.fetchall()
        print(f"Results for query: {query.strip()}")
        for row in results:
            print(row)
        print("\n")


conn.commit()

cur.close()
conn.close()
