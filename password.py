import random
import string

def generate_password(minlength, numbers=True, specialChars=True):
    # Generate a password with the given length
    letters = string.ascii_letters
    nums = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += nums
    if specialChars:
        characters += special

    password = ""
    checker = False
    hasNumber = False
    hasSpecial = False

    while not checker or len(password) < minlength:
        
        pwd = random.choice(characters)
        password += pwd

        if pwd in nums:
            hasNumber = True
        elif pwd in special:
            hasSpecial = True

        checker = True

        if numbers:
            checker = hasNumber
        if specialChars:
            checker = checker and hasSpecial

    return password

minInput = int(input("Enter the minimum length of the password: "))
hasNumber = input("Do you want numbers in your password? (y/n): ").lower() == "y"
hasSpecial = input("Do you want special characters in your password? (y/n): ").lower() == "y"

pwd = generate_password(minInput, hasNumber, hasSpecial)
print(pwd)