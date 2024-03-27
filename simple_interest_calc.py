#A simple interest calculator
p = float(input('What is the Principal Amount: '))
r = float(input('What is the rate of interest: '))
t = float(input('What is the time period? - '))

interest = (p*r*t) / 100

print('The Simple Interest is: ', interest)