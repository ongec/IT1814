"""
The solution below read in input from user
The celsius is based on the input entered by the user
"""
celsius = float(input('Enter celsius: '))
fahrenheit = 9/5 *celsius + 32
print("The temperature in Fahrenheit is",fahrenheit)

# improvements
try:
    celsius = float(input('Enter celsius: '))
except:
    print("Invalid input. No conversion done ")
else:
    fahrenheit = 9/5 *celsius + 32
    print("The temperature in Fahrenheit is",fahrenheit)
