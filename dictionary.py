# Sort through a List of Dictionaries by using a specific key

list_of_dicts = [{'Name': 'Olivia', 'Profession': 'Data Analyst', 'Age': 37}, 
                 {'Name': 'Terry', 'Profession': 'Nurse', 'Age': 40}, 
                 {'Name': 'Dora', 'Profession': 'Vetinary', 'Age': 34},
                 {'Name': 'Alicia', 'Profession': 'Software Developer', 'Age': 29}]
sorted_list = sorted(list_of_dicts, key = lambda x:x['Age'])
print('Sorted List of Dictionaries:',sorted_list)