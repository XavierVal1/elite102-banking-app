import sqlite3
import unittest
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

'''initialising values & greeting'''
selection = [1, 2, 3, 4, 5, 6]
accounts = ["Xavier Valverde"]
print("Welcome to the Valverde Bank! Please make a selection from the following... (1-6)\n1. Create new account\n2. Deposit money into an account\n3. Withdraw money\n4. Check account details\n5. list existing accounts\n6. Exit")
cursor.execute("INSERT INTO accounts VALUES (1, 'checking', 1000, 'Xavier Valverde')")
idCounter = 1
loop = 1
conn.commit()

'''Defining functions'''
def display_accounts():
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    conn.commit
    print("All accounts:")
    for row in rows:
        print(f"  ID: {row[0]}, Type: {row[1]}, Balance: {row[2]}, account_holder: {row[3]}")
def make_account(type, balance, act_hold):
    global idCounter
    idCounter += 1
    if type == 0:
        while True:
            type = str.lower(input("Checking or savings account: "))
            if type != "savings" and type != "checking":
                print("choose a savings or checking account.")
            if type == "savings" or type == "checking":
                break

    if balance == 0:
        while True:
            try:
                balance = float(input("Starting balance: "))
            except ValueError:
                balance = -1
            if balance < 0:
                print("Enter a positive number")
            if balance > 0:
                break
    if act_hold == 0:
        act_hold = input("First and last name of account holder: ")
    accounts.append(act_hold)
    cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?)", (idCounter, type, balance, act_hold))
    if act_hold != 0:
        print("Account made.")
    conn.commit()
def deposit_account(account, add):
    while True:
        account = input("Please enter your first and last name: ")
        if account not in accounts:
            print("Account not found, try again.")
        if account in accounts:
            break
    bal = cursor.execute("SELECT balance FROM accounts WHERE account_holder = ?", (account,))
    bal_1 = cursor.fetchall()
    while True:
        try:
            add = float(input("Amount to deposit: "))
        except ValueError:
            add = -1
        if add < 0:
            print("Enter a positive number")
        if add > 0:
            break
    cursor.execute("UPDATE accounts SET balance = ? WHERE account_holder = ?", (bal_1[0][0] + add, account))
    print(f"New balance: {bal_1[0][0] + add}")
def withdraw_account(account, withdraw):
    if account == 0:
        while True:
            account = input("Please enter your first and last name: ")
            if account not in accounts:
                print("Account not found, try again.")
            if account in accounts:
                break
    bal = cursor.execute("SELECT balance FROM accounts WHERE account_holder = ?", (account,))
    bal_1 = cursor.fetchall()
    if withdraw == 0:
        while True:
            try:
                withdraw = float(input("Amount to withdraw: "))
            except ValueError:
                print("Enter a positive number")
                withdraw = -1.12
            if withdraw != -1.12 and bal_1[0][0] - withdraw < 0:
                print("Not enough in account")
            if withdraw != -1.12 and bal_1[0][0] - withdraw > 0:
                break
    cursor.execute("UPDATE accounts SET balance = ? WHERE account_holder = ?", (bal_1[0][0] - withdraw, account))
    print(f"New balance: {bal_1[0][0] - withdraw}")
    if account == "Xotchitl Valverde":
        global new_balance
        new_balance = bal_1[0][0] - withdraw
def display_single(account):
    while True:
            account = input("Please enter your first and last name: ")
            if account not in accounts:
                print("Account not found, try again.")
            if account in accounts:
                break
    cursor.execute("SELECT * FROM accounts WHERE account_holder = ?", (account,))
    display = cursor.fetchall()[0]
    conn.commit
    print(f"{account}'s account: ")
    print(f"  ID: {display[0]}, Type: {display[1]}, Balance: {display[2]}, account_holder: {display[3]}")


'''Main CLI app'''
while True:
    if loop != 1:
        print("1. Create new account\n2. Deposit money into an account\n3. Withdraw money\n4. Check account details\n5. list existing accounts\n6. Exit")
    loop += 1
    try:
        select = int(input("Enter choice: "))
    except ValueError:
        select = 7
    if select not in selection:
        print("enter an integer between 1 and 6.")
    if select == 1:
        make_account(0, 0, 0)
    if select == 2:
        deposit_account(0, 0)
    if select == 3:
        withdraw_account(0, 0)
    if select == 4:
        display_single(0)
    if select == 5:
        print("Listing existing accounts")
        display_accounts()
    if select == 6:
        print("Thanks for using this app!")
        break

'''Unit Testing'''
def does_exist(e):
    '''returns true if account does exist, false otherwise'''
    return e in accounts

class TestMyFunctions(unittest.TestCase):
    def test_account_exists(self):
        #checks that account exists / make account function works
        make_account("checking", 340, "Xotchitl Valverde")
        self.assertTrue(does_exist("Xotchitl Valverde"))
    def test_withdraw(self):
        #checks withdraw function
        withdraw_account("Xotchitl Valverde", 40)
        self.assertEqual(new_balance, 300)
'''Running The Tests'''
import sys
loader = unittest.TestLoader()
suite = loader.loadTestsFromTestCase(TestMyFunctions)
runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
runner.run(suite)
conn.close()