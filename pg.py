import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Prompt the user for password length
try:
    password_length = int(input("Enter the desired password length: "))
    if password_length <= 0:
        raise ValueError("Password length must be a positive integer.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Generate and display the password
password = generate_password(password_length)
print(f"Generated Password: {password}")

