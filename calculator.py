#A simple python calculator
2
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
print('------The results is as follows------')
print('Addition: ', a + b)
print('Difference: ', a - b)
print('Multiplication: ', a * b)
print('True Division: ', a / b) # Quotient of a and b
print('Modulus: ', a % b) #Integer remainder after  division of a by b
print('Floor Division: ', a // b) #Quotient of a and b removing fractional parts
print('Exponentiation: ', a ** b) # a raised to the power of b
print('Negation : ', -a) # the negative of a