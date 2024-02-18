import hashlib
import getpass

def hash_password(password):
    """Hash a password using SHA-256."""
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

def main():
    # Prompt the user for a password without echoing it back
    password = getpass.getpass('Please enter your password: ')
    
    # Hash the password
    hashed_password = hash_password(password)
    
    # Store the hashed password in a file
    with open('hashed_password.txt', 'w') as file:
        file.write(hashed_password)
    
    print("The hashed password has been stored in 'hashed_password.txt'.")

if __name__ == "__main__":
    main()
