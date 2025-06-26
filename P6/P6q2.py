text = input('Enter a string: ')
print(f"\nLength : {len(text)} ")
if(text[-1] == '.'):
    print("It ends with full stop!\n")
else:
    print("It does not end with full stop!\n")
index = 0
for char in text:
    print('position', index ,':',char )
    index +=1

