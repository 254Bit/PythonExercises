# Check if a string is a valid email address
import re

def is_valid_email(email):
    return bool(re.match(r'[^@]+@[^@]+\.[^@]+',email))

input_email = input('Enter an Email Address:')
if is_valid_email(input_email):
    print('That is a valid email address')
else:
    print('Ooops! Invalid email address')