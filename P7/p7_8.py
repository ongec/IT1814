"""
Using dictionary to store all the respective marks for a student in a list
"""
results = {
'Jane': [75, 80, 85], 
'John':[60, 68, 74], 
'Jerome':[81, 63, 77], 
'Jason':[55, 76, 67], 
'Jessica':[62, 45, 68], 
'Joanne':[52, 47, 51]}
name = input('Enter student name: ').capitalize()
studentResult = results.get(name, 'Student does not exist!')
if studentResult != "Student does not exist!":
    print("Results of", name)
    print("=================================")
    # english is stored at list position 0, 
    # Math at 1 and Science at 2
    print(f'English : { studentResult[0] } ') 
    print(f'Math : { studentResult[1] } ')
    print(f'Science: { studentResult[2] } ')
else:
    print(studentResult)

