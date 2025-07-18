# code the function getValidAge
def getValidAge():
    msg = "Invalid age! Valid age is 3 - 80."
    while(True):
        try:
            age1 = int(input("\nEnter Age: "))
            if( age1 < 3 or age1 > 80 ):
                print( msg )
            else:
                return(age1)
        except:
            print( msg )
# code the function getTicketPrice
def getTicketPrice(age):
    if age <= 20:
        return 10
    elif age <= 65:
        return 30
    else:
        return 15
# main program calling the functions    
userAge = getValidAge()
price = getTicketPrice( userAge )
print(f'Age = {userAge}, Please pay ${ price }')
