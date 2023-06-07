# Registration and Login System

This project implements a simple registration and login system using Python. It allows users to register with a valid email and password, and then login with their credentials. The user data is stored in a text file. Read the  [Project Task](https://github.com/priyankaChandramohan/Python-Login-System/blob/main/Project%20task.md) file to find the assignment question.

## Features

- User registration with email and password validation
- Secure login authentication
- Forgot password functionality
- Data storage using a text file

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the source code.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script by executing the command: `python registration_login.py`
4. Follow the instructions on the command line to register, login, or reset the password.

## File Structure

-  [`registration.py`](https://github.com/priyankaChandramohan/Python-Login-System/blob/main/registration.py): The main Python script that implements the registration and login system.
- [`users.txt`](https://github.com/priyankaChandramohan/Python-Login-System/blob/main/users.txt): The text file that stores the user data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Explanation to the project:

- The validate_email() function uses regular expressions to validate the email format based on the given pattern.
- The validate_password() function checks if the password meets the specified requirements using regular expressions.
- The register() function prompts the user to enter a username, email, and password. It validates the email and password formats and appends the user data to the "users.txt" file if they are valid.
- The login() function prompts the user to enter a username and password. It checks if the username and password match any user data stored in the "users.txt" file and provides appropriate login status messages.
- The forgot_password() function allows the user to reset their password by entering a new password. It updates the password


