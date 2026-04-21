import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE accounts (
        id INTEGER PRIMARY KEY,
        type TEXT,
        balance INTEGER,
        account_holder TEXT
    )
''')
print("Welcome to the Valverde Bank! Please make a selection from the following... (1-5)\n1. Create new account\n2. Deposit money into an account\n3. Withdraw money\n4. Check account details\n5. list existing accounts\n6. Exit")
cursor.execute("INSERT INTO accounts VALUES (1, 'checking', 500, 'Xavier Valverde')")
idCounter = 1
conn.commit()


def display_accounts():
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    conn.commit
    print("All accounts:")
    for row in rows:
        print(f"  ID: {row[0]}, Type: {row[1]}, Balance: {row[2]}, account_holder: {row[3]}")
while True:
    select = input("Enter choice: ")
    if select == "1":
        idCounter += 1
        type = input("Type of account: ")
        balance = int(input("Starting balance: "))
        act_hold = input("First and last name of account holder: ")
        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?)", (idCounter, type, balance, act_hold))
        conn.commit()
    if select == "2":
        account = input("Please enter your first and last name: ")
        bal = cursor.execute("SELECT balance FROM accounts WHERE account_holder = ?", (account,))
        bal_1 = cursor.fetchall()
        add = int(input("Amount to deposit: "))
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_holder = ?", (bal_1[0][0] + add, account))
        print("depositing money")
        display_accounts()
    if select == "3":
        account = input("Please enter your first and last name: ")
        bal = cursor.execute("SELECT balance FROM accounts WHERE account_holder = ?", (account,))
        bal_1 = cursor.fetchall()
        withdraw = int(input("Amount to withdraw: "))
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_holder = ?", (bal_1[0][0] - withdraw, account))
        print("Withdrawing money")
        display_accounts()
    if select == "4":
        account = input("First name and Last name: ")
        cursor.execute("SELECT * FROM accounts WHERE account_holder = ?", (account,))
        display = cursor.fetchall()[0]
        conn.commit
        print(f"{account}'s account: ")
        print(f"  ID: {display[0]}, Type: {display[1]}, Balance: {display[2]}, account_holder: {display[3]}")

    if select == "5":
        print("Listing existing accounts")
        display_accounts()
    if select == "6":
        print("Thanks for using this app!")
        conn.close()
        break