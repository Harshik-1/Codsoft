import random
import string

def generate_password(length=12, uppercase=True, digits=True, special_chars=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input():
    length = int(input("Enter the length of the password: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    return length, uppercase, digits, special_chars

def main():
    print("Welcome to the Password Generator!")

    length, uppercase, digits, special_chars = get_user_input()

    password = generate_password(length, uppercase, digits, special_chars)

    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
