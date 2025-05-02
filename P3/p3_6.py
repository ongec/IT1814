''' Convert seconds to hours, minutes and seconds
    3600 sec in 1 hour
'''
totalSec = int(input("enter seconds: "))
hr = totalSec//3600
min = ( totalSec // 60 ) % 60 #or minute = (totalSec - (hr * 3600)) // 60
sec = totalSec % 60
print(f"{totalSec} seconds is {hr} hours, {min} minutes and {sec} seconds" )
