"""
This part of the solution show the fixed book price and fixed number of copy
It does not get input from user
This solution also does not display the subtotal, GST and Total price in 2 decimal point format
"""
price = 3.75
copy = 3
subtotal = price * copy
gst = 0.07 * subtotal
total = subtotal + gst

print("Subtotal: $", subtotal)
print("GST: $", gst)
print("Total: $", total)


"""
This part of solution show the book price and number of copy are input from user
The subtotal, GST and Total price also display in 2 decimal point format
"""
price = float(input('Enter the book price $'))
copy = int(input('Enter number of copy purchased:'))
subtotal = price * copy
gst = 0.07 * subtotal
total = subtotal + gst

print("Subtotal: $%.2f" %subtotal)
print("GST: $%.2f" %gst)
print("Total: $%.2f" %total)

