age = int(input("Enter age: "))
if age>=4 and age <=130:
    day = int(input("Enter day of week (1-7): "))
    if day == 6 or day == 7:
        price = 9
    else:
        if (age < 16) :
            price = 7.5
        elif (age <= 65):
            price = 10
        else:
            price = 5.5
    print(f"Ticket Price: ${price:.2f} " )
else:
    print("Invalid age. Must be between 4 and 130.")

