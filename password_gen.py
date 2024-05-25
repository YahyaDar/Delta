import random
import string


# Function to get a valid integer input within a specified range
def get_valid_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid integer")


# Function to get a valid 'y' or 'n' input
def get_valid_yn(prompt):
    while True:
        value = input(prompt).lower()
        if value in ['y', 'n']:
            return value
        else:
            print("Invalid option! Please enter 'y' or 'n'")


# Collect user inputs
password_length = get_valid_int("Enter the length of the password: ", 1, 256)
print_iterations = get_valid_int("Enter the number of passwords to generate: ", 1, 100)

bool_special = get_valid_yn("Include special characters? (y/n): ").lower()
bool_digit = get_valid_yn("Include numbers (0-9)? (y/n): ").lower()
bool_uppercase = get_valid_yn("Include uppercase letters (A-Z)? (y/n): ").lower()
bool_lowercase = get_valid_yn("Include lowercase letters (a-z)? (y/n): ").lower()


# Get the character set based on user inputs
def get_characters():
    characters = ""
    if bool_lowercase == 'y':
        characters += string.ascii_lowercase
    if bool_uppercase == 'y':
        characters += string.ascii_uppercase
    if bool_digit == 'y':
        characters += string.digits
    if bool_special == 'y':
        characters += string.punctuation

    if characters == "":
        return "No character set selected!"

    return characters


# Function to generate a single password
def password_gen():

    characters = get_characters()

    password = []

    # Ensure at least one character of each selected type
    if bool_lowercase == 'y':
        password.append(random.choice(string.ascii_lowercase))
    if bool_uppercase == 'y':
        password.append(random.choice(string.ascii_uppercase))
    if bool_digit == 'y':
        password.append(random.choice(string.digits))
    if bool_special == 'y':
        password.append(random.choice(string.punctuation))

    # Fill remaining length of the password if necessary
    while len(password) < password_length:
        char = random.choice(characters)
        if not password or char != password[-1]:
            password.append(char)

    # Ensure no two consecutive characters are the same
    for x in range(1, password_length):
        while password[x] == password[i - 1]:
            password[x] = random.choice(characters)

    # Shuffle the password list to mix the mandatory characters
    random.shuffle(password)

    # Replace number or special character at beginning or end with letters
    if password[0] in string.digits + string.punctuation:
        password[0] = random.choice(string.ascii_letters)
    if password[-1] in string.digits + string.punctuation:
        password[-1] = random.choice(string.ascii_letters)

    return ''.join(password)


# Generate and print the requested number of passwords
for i in range(print_iterations):
    print(password_gen())
