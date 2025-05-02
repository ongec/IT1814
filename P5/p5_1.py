# Solution A
sum = 0
num = int(input("Enter number: "))
print('\nAdd odd number(s):')
for i in range(1, num+1):
    if( i % 2 == 1):  #odd number
        print(f'{i}')
        sum += i
print("Sum is", sum)

# Solution B
sum = 0
num = int(input("Enter number: "))
print('\nAdd odd number(s):')
for i in range(1, num+1, 2):
    print(f'    {i}')
    sum += i
print("Sum is", sum)

