sellPrice = 0
while True:
    try:
        cost = float(input("\nEnter the cost of item ($): "))
        if cost == 0:
            break
        if( cost <0 ) :
            print('Cost must be positive. Please re-enter')
            continue
        sellPrice = cost * 1.25
        print("The selling price is $%.2f" % (sellPrice))
    except:
        print('Only numerical value. Please re-enter')
print('Program End')

