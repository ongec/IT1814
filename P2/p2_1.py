totalHour = 10.50
rate = 12.35
pay = totalHour * rate
# Display the pay in 2 decimal places using the below 2 method
#    - use string modulo operator % 
#    - use  f-Strings
print( "Total Hour= %.2f , Hourly Rate= %.2f , Salary= $%.2f" % (totalHour,rate,pay))
print( f"Total Hour= {totalHour:.2f} , Hourly Rate= {rate:.2f} , Salary= ${pay:.2f}")
