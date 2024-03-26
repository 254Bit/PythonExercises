# Check if a year is a leap year or not using FUNCTIONS
def is_it_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input('Enter a Year: '))
if is_it_leap_year(year):
    print('Yes', year,'is a Leap Year')
else:
    print('No', year, 'is not a Leap Year')
