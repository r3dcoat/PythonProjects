''' This is an example banking application. It will have users login or create an account. Users will then be able to withdraw, deposit, and transfer money between account 
    Users will first be welcomed to the bank, then asked to login or create an account. 
    Creating an account will have the users enter an email and a password. 
    After the creation of the account the user is asked to deposit money.
    The user can then also withdraw money from their accounts.
    Users can transfer money to other user accounts.

    List of user accounts: email password balance
    Use a function to create the account when users create their account or login
'''
import getpass
import hashlib

app_running = True
logged_in = False
user_accounts = []
logged_in_account = ""



def hash_password(password):
    """Hash a password for storing"""
    return hashlib.sha256(password.encode()).hexdigest() # Once I learn a bit more about hashing I should be salting these.

# This function will create the account of the user and then log the user in after account creation
def create_account():
    global hash_password
    print("Thank you for chosing to create an account with us. First we need to ask a few questions.")
    account_email = input("Please enter an email address: ") # User selects their username which is an email
    if any(account[0] == account_email for account in user_accounts):
        print("An account with this email already exists.")
        return
    account_password = getpass.getpass("Please choose a password: ") # Users enter their password ||| After testing the working application I will work on implementing security into the password section. This is work in progress and mainly to just learn Python. 
    password_verify = getpass.getpass("Please enter the password again: ") # Users are asked to enter their password again. 
    if account_password == password_verify: # This will verify that they have entered their password correctly. 
        # New accounts do not have any money in them.
        hashed_password = hash_password(account_password) 
        user_accounts.append([account_email, hashed_password, 0])
        print("Account created successfully.")
    else:
        print("Passwords do not match.")
    print(user_accounts)


# This funciton will log a user into their account
def user_login():
    global logged_in, logged_in_account, hash_password
    account_email = input("Please enter your email: ")
    account_password = getpass.getpass("Please enter your password: ")
    hashed_password = hash_password(account_password)
    for account in user_accounts: 
        if account_email == account[0] and hashed_password == account[1]:
            logged_in = True
            logged_in_account = account[0]
            print("Welcome back " + logged_in_account)
            return account
        else:
            print("Invalid credentials.")

# This function will deposit money into the accounts of users. 
def deposit_money():
    global user_accounts
    deposit_amount = int(input("Enter amount to deposit: "))

    for account in user_accounts:
        if account[0] == logged_in_account:
            account[2] += deposit_amount
            print(f"Your current balance is now  ${account[2]}")
            return
    print("Account not found.")

# Function to withdraw money from a users account. This also prevents users from overdrafting there accounts. You need money to bank with the Bank of Money
def withdraw_money():
    global user_accounts
    withdraw_ammount = int(input("Enter amount to withdraw: "))

    for account in user_accounts:
        if account[0] == logged_in_account:
            account[2] -= withdraw_ammount
            if account[2] >= 0:
                print(f"Your current balance is now ${account[2]}")
                return
            elif account[2] < 0:
                print("You do not have the necessary funds for that transaction.")
                account[2] += withdraw_ammount
                return
    print("Account not found.")

# Simple function to display the current account balance. 
def display_balance():
    global user_accounts
    for account in user_accounts:
        if account[0] == logged_in_account:
            print(f"Your current balance is ${account[2]}")
            return

# Function to transfer money from one account to another. 
def transfer_money():
    global user_accounts, logged_in_account
    target_user = input("What user account to transfer funds to. Enter their email address: ")
    transfer_amount = float(input("Enter the dollar amount you wish to transfer: "))

    # Users are not to transfer money to themselves. 
    if target_user == logged_in_account:
        print("You cannot transfer money to your own account.")
        return

    target_account_found = False
    for account in user_accounts:
        if account[0] == target_user:
            target_account_found = True
            break
    
    if not target_account_found:
        print("An account with that email address has not been found. Please try again later.")
        return

    for account in user_accounts:
         if account[0] == logged_in_account:
            if account[2] >= transfer_amount:
                account[2] -= transfer_amount
                for target_account in user_accounts:
                    if target_account[0] == target_user:
                        target_account[2] += transfer_amount
                        print(f"Transfer of ${transfer_amount} has been sent. Your current balance is ${account[2]}")
                        return
            else:
                print("Insufficient funds for this transfer.")
                return                    

#Functions to save accounts to a file and to load the accounts when the application is opened
def save_accounts_to_file():
    with open('user_accounts.txt', 'w') as file:
        for account in user_accounts:
            account_data = [account[0], account[1], str(account[2])]
            file.write(','.join(account_data) + '\n')

def load_accounts_from_file():
    global user_accounts
    try:
        with open('user_accounts.txt', 'r') as file:
            for line in file:
                email, hashed_password, balance_str = line.strip().split(',')
                balance = float(balance_str)
                user_accounts.append([email, hashed_password, balance ])
    except FileNotFoundError:
        user_awccounts = []

### Application Running Section ###
while app_running == True:
    load_accounts_from_file()
    print(r"""
__________                __             _____     _____                              
\______   \_____    ____ |  | __   _____/ ____\   /     \   ____   ____   ____ ___.__.
 |    |  _/\__  \  /    \|  |/ /  /  _ \   __\   /  \ /  \ /  _ \ /    \_/ __ <   |  |
 |    |   \ / __ \|   |  \    <  (  <_> )  |    /    Y    (  <_> )   |  \  ___/\___  |
 |______  /(____  /___|  /__|_ \  \____/|__|    \____|__  /\____/|___|  /\___  > ____|
        \/      \/     \/     \/                        \/            \/     \/\/     
    """)
    print("For us to help you today please login or if you are new, create an account. Enter 1 for login or enter 2 for account creation.")
    print("1) Login") 
    print("2) Create an account")
    user_choice = input()
    if user_choice == str(1):
        user_login()
    elif user_choice == str(2):
        create_account()
    elif user_choice.lower() == "exit" or user_choice.lower() == "quit":
        save_accounts_to_file()
        app_running = False
    else:
        print("Please select option 1 or 2.")
    while logged_in == True: # After the user has logged in they will be presented with this.
        print("How can we help you today?")
        print("1) Deposit money")
        print("2) Withdraw money")
        print("3) Display Balance")
        print("4) Transfer money")
        print("5) Log out")
        user_choice = input()
        if user_choice == "1":
            deposit_money()
        elif user_choice == "2":
            withdraw_money()
        elif user_choice == "3":
            display_balance()
        elif user_choice == "4":
            transfer_money()
        elif user_choice == "5":
            print("You are now logged out")
            logged_in = False
        else:
            print("Invalid option")
    