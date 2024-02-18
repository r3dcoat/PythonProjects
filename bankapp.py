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

# This function will create the account of the user and then log the user in after account creation
def create_account():
    print("Thank you for chosing to create an account with us. First we need to ask a few questions.")
    account_email = input("Please enter an email address: ") # User selects their username which is an email
    account_password = input("Please choose a password: ") # Users enter their password
    password_verify = input("Please enter the password again: ") # Users are asked to enter their password again. 
    if account_password == password_verify: # This will verify that they have entered their password correctly. 
        # New accounts do not have any money in them. 
        user_accounts.append([account_email, account_password, 0])
    print(user_accounts)
    #this should be a loop. I will add after acount creation. 
        #this should be a loop. I will add after acount creation. 
# This funciton will log a user into their account
def user_login():
    account_email = input("Please enter your email: ")
    account_password = input("Please enter your password: ")
    for account in user_accounts: 
        if account_email == account[0] and account_password == account[1]:
            print("Welcome back")
            logged_in = True
            logged_in_account = account[0]
            return account
        else:
            print("Invalid credentials.")

while app_running == True:
    print("Welcome to Bank of Money")
    print("For us to help you today please login or if you are new, create an account. Enter 1 for login or enter 2 for account creation")
    user_choice = input()
    if user_choice == str(1):
        user_login()
    elif user_choice == str(2):
        create_account()
    elif user_choice.lower() == "exit" or user_choice.lower() == "quit":
        app_running = False
    else:
        print("Please select option 1 or 2.")
    while logged_in == True:
        print("Hello " + logged_in_account)

    