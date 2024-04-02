import random
import string

def generate_password(length, include_digits = True, include_special_chars = True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ' '.join(random.choice(characters) for _ in range(length))
    return password

password_length = 12
print('Generated Password:', generate_password(password_length))