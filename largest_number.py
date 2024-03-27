#Find the largest or smallest number among three numbers

a = float(input('Give me a number: '))
b = float(input('Give me another number: '))
c = float(input('Give me yet another number: '))

max_num = max(a,b,c)
min_num = min(a,b,c)

print('The largest number is ', max_num, 'and the smallest number is ', min_num)

