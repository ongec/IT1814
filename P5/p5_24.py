student = int(input("Enter number of students: "))
test = int(input("Enter number of tests: "))
for num in range(1, student + 1 ):
    total = 0.0
    print(f'\n******* Student #{num} *******')
    for count in range ( 1 , test + 1):
        score = float(input(f'Test {count} score: '))
        total += score
    avg = total / test
    print(f'The average for student #{num} is: {avg}')
    print()

