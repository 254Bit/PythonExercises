#Get the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input('Give me a number: '))
print('Factorial: ', factorial(num))