import random
import string

def generate_password(minlength, numbers=True, specialChars=True):
    # Generate a password with the given length
    letters = string.ascii_letters
    nums = string.digits
    special = string.punctuation

minInput = int(input("Enter the minimum length of the password: "))
hasNumber = input("Do you want numbers in your password? (y/n): ").lower() == "y"
hasSpecial = input("Do you want special characters in your password? (y/n): ").lower() == "y"

pwd = generate_password(minInput, hasNumber, hasSpecial)
print(pwd)