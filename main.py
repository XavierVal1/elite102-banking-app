import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE accounts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')
print("Welcome to the Valverde Bank! Please make a selection from the following... (1-5)\n1. Create new account\n2. Deposit money into an account\n3. Withdraw money\n4. Check account balance\n5. list existing accounts")
cursor.execute("INSERT INTO accounts VALUES (1, 'Maria Garcia', 'maria@school.edu')")
cursor.execute("INSERT INTO accounts VALUES (2, 'James Chen', 'james@school.edu')")
select = input("Enter choice: ")
if select == "1":
    print("creating account")
if select == "2":
    print("depositing money")
if select == "3":
    print("Withdrawing money")
if select == "4":
    print("Checking account balance")
    
conn.commit()

cursor.execute("SELECT * FROM accounts")
rows = cursor.fetchall()

def display_accounts():
    print("All accounts:")
    for row in rows:
        print(f"  ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

        conn.close()