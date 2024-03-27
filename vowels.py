#Counting vowels in a string

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count
        
string = input('Tell me a string, I will tell you the number of vowels in it? ')
print('The number of vowels is ', count_vowels(string))
