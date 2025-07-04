englishMark= {'Jane': 75, 'John': 60, 'Jerome': 81}
for key, value in englishMark.items() :
    print(f' {key} : {value}')
print('======================')
name = input('Enter student name: ')
name = name.capitalize() # make 1st letter capitalise
# method 1, use in to check
if name in englishMark:
    print(f'\nResult for English: {englishMark[name]}')
else:
    print(f'\nThere is no result for {name}')
# method 2, use .get( key, default value), 
# return default value -1 when key not found
if (englishMark.get(name, -1) != -1 ):
    print(f'\nResult for English: {englishMark[name]}')
else:
    print(f'\nThere is no result for {name}')

