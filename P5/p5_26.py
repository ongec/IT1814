order = True
itemDesc=""
total = 0
while order:
    print('\nMenu')
    print('====')
    print('0) Buy Burger')
    print('1) Buy Drink')
    item = int(input('Please enter your order: '))
    # assign string for display purpose
    if(item == 0):
        itemDesc = "Burger"
    else:  #assume no error checking
        itemDesc = "Drink"
    qty = int(input('How many %s for this order : ' % itemDesc))
    for i in range(qty):
        price = float(input('Enter price for %s %i : ' % (itemDesc, i+1)))
        total += price
    print('Total price now is $%.2f.' % total)
    # ask user whether there is more orders
    moreOrders = input('Do you have more orders (Y/N)? : ')
    if(moreOrders == 'N' or moreOrders == 'n'): #assume no error input
        order = False  # this is stop the outer while loop and come out of it
print('\nThank You. Please pay $%.2f' % total)

