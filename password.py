import random
import string

def generate_password(minlength, numbers=True, specialChars=True):
    # Generate a password with the given length
    letters = string.ascii_letters
    nums = string.digits
    special = string.punctuation

    