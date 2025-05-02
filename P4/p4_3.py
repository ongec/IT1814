try:
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in m: "))
except ValueError:
    print('Invalid input detected. Exiting program.')
else:
    min = 18.5 * ( height ** 2 )
    max = 22.9 * ( height ** 2 )
    print(f"Your ideal weight is {min:.2f} kg to {max:.2f} kg")
     
    if( weight >= min and weight <= max):
        print('Good Job! Your weight is ideal')
    else:
        print("Work harder to maintain an ideal weight")

