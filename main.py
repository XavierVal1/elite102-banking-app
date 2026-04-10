import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

cursor.execute("INSERT INTO contacts VALUES (1, 'Maria Garcia', 'maria@school.edu')")
cursor.execute("INSERT INTO contacts VALUES (2, 'James Chen', 'james@school.edu')")

conn.commit()

cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()

print("All contacts:")
for row in rows:
    print(f"  ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    conn.close()