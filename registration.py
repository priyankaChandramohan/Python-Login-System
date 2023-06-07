import re

def validate_email(email):
    """Validate email format"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_password(password):
    """Validate password format"""
    if len(password) < 5 or len(password) > 16:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@#$%^&+=]', password):
        return False
    return True

def register():
    """Register a new user"""
    while True:
        email = input("Enter email/username: ")
        if validate_email(email):
            break
        print("Invalid email format. Please try again.")

    while True:
        password = input("Enter password: ")
        if validate_password(password):
            break
        print("Invalid password format. Please try again.")

    # Store user data in a file
    with open('user_data.txt', 'a') as file:
        file.write(f"{email},{password}\n")

    print("Registration successful!")

def login():
    """Login an existing user"""
    email = input("Enter email/username: ")
    password = input("Enter password: ")

    # Check if user credentials exist in the file
    with open('user_data.txt', 'r') as file:
        for line in file:
            stored_email, stored_password = line.strip().split(',')
            if email == stored_email and password == stored_password:
                print("Login successful!")
                return

    print("Invalid credentials. Please try again.")

def main():
    print("Welcome to the Registration and Login System")
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
