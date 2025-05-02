no = int(input('Enter number : '))
print(f'\nPrime nos before {no} :')
for testNo in range(2,no): 
    #run through all numbers before this num
    for curDivisor in range(2, testNo):
        if testNo % curDivisor == 0: #divisible
            break 
    else:
        print(f" {testNo}") 

