# Write a program to check if the given number is a palindrome number
# A palindrome number is a number that is the same after reverse.
# For example 747, is a palindrome number. end - den

# def is_palindrome(s):
#     return s == s[::-1]
# string = input('Give me a string:')
# if is_palindrome(string):
#     print('That is a palindrome')
# else:
#     print('This is not a palindrome')

num = input('Give me a number: ')
rev_num = num[::-1]
print(rev_num)

if num == rev_num:
    print('This is a palindrome number')
else:
    print('This is not a palindrome number')