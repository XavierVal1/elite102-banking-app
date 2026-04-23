import sqlite3
import tkinter as tk
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
idCounter = 1
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
conn.commit()

'''Defining functions'''

def makeAccount():
    '''Creating page for making account'''
    global action
    action = "make-type"
    button.grid_remove()
    button_1.grid_remove()
    button_2.grid_remove()
    button_3.grid_remove()
    button_4.grid_remove()
    query.grid_remove()
    greet.grid_remove()
    input_entry.grid()
    save_button.grid()
    act.grid()
    act_check.grid()
    global idCounter
    idCounter += 1
    type = input("Type of account: ")
    balance = int(input("Starting balance: "))
    act_hold = input("First and last name of account holder: ")
    cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?)", (idCounter, type, balance, act_hold))
    print("***Account added***")
    conn.commit()
def deposit():
    account = input("Please enter your first and last name: ")
    bal = cursor.execute("SELECT balance FROM accounts WHERE account_holder = ?", (account,))
    bal_1 = cursor.fetchall()
    add = int(input("Amount to deposit: "))
    cursor.execute("UPDATE accounts SET balance = ? WHERE account_holder = ?", (bal_1[0][0] + add, account))
    print("depositing money")
def withdraw():
    account = input("Please enter your first and last name: ")
    bal = cursor.execute("SELECT balance FROM accounts WHERE account_holder = ?", (account,))
    bal_1 = cursor.fetchall()
    withdraw = int(input("Amount to withdraw: "))
    cursor.execute("UPDATE accounts SET balance = ? WHERE account_holder = ?", (bal_1[0][0] - withdraw, account))
    print("Withdrawing money")
def display_accounts():
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    conn.commit
    print("All accounts:")
    for row in rows:
        print(f"  ID: {row[0]}, Type: {row[1]}, Balance: {row[2]}, account_holder: {row[3]}")
def singleAccount():
    account = input("First name and Last name: ")
    cursor.execute("SELECT * FROM accounts WHERE account_holder = ?", (account,))
    display = cursor.fetchall()[0]
    conn.commit
    print(f"{account}'s account: ")
    print(f"  ID: {display[0]}, Type: {display[1]}, Balance: {display[2]}, account_holder: {display[3]}")
def action_entry():
    if action == "make":
        type1 = input_entry.get()
        act.grid_remove()
        name.grid()
        global action
        action = "make-name"
    if action == "make-name":
        name1 = input_entry.get()
        name.grid_remove()
        balance.grid()




'''GUI Setup'''
window = tk.Tk()
window.title("Banking Interface")
greet = tk.Label(window, text = "Welcome to the Valverde Bank!", font=("Arial", 20, "bold"))
greet.grid(row = 0, column = 0, padx = 10, pady = 5)
query = tk.Label(window, text = "Please make a selection from the following:")
query.grid(row = 1, column = 0, padx = 10, pady = 50)
act_check = tk.Label(window, text = "Make an account", font=("Arial", 20, "bold"))
act_check.grid(row = 0, column = 5, padx = 10, pady = 5)
act_check.grid_remove()
button = tk.Button(window, text="Create New Account", command=makeAccount)
button_1 = tk.Button(window, text="Deposit Money", command=deposit)
button_2 = tk.Button(window, text="Withdraw Money", command=withdraw)
button_3 = tk.Button(window, text="Check account details", command=singleAccount)
button_4 = tk.Button(window, text="List existing accounts", command=display_accounts)

button.grid()
button_1.grid()
button_2.grid()
button_3.grid()
button_4.grid()
input_entry = tk.Entry(window, width = 15)
input_entry.grid(row = 5, column = 5, padx = 0, pady = 10)
act = tk.Label(window, text = "Savings or checking account:")
act.grid(row = 5, column = 4, padx = 0, pady = 10)
act.grid_remove()
name = tk.Label(window, text = "First and last name of account holder:")
name.grid(row = 5, column = 4, padx = 0, pady = 10)
name.grid_remove()
balance = tk.Label(window, text = "Initial deposit:")
balance.grid(row = 5, column = 4, padx = 0, pady = 10)
balance.grid_remove()
save_button = tk.Button(window, text="Save entry", command=action_entry)
save_button.grid(row = 5, column = 6, padx = 0, pady = 10)
input_entry.grid_remove()
save_button.grid_remove()
window.mainloop()


while True:
    select = input("Enter choice: ")
    if select == "1":
        makeAccount()
    if select == "2":
        deposit()
        display_accounts()
    if select == "3":
        withdraw()
        display_accounts()
    if select == "4":
        singleAccount()
    if select == "5":
        print("Listing existing accounts")
        display_accounts()
    if select == "6":
        print("Thanks for using this app!")
        conn.close()
        break