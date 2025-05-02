price = float(input('Enter price of book $ '))
copy = int(input('Enter number of copy purchased: '))
subtotal = price * copy
gst = 0.07 * subtotal
total = subtotal + gst
print("Subtotal: $%.2f" % subtotal)
print("GST: $%.2f" % gst)
print("Total: $%.2f" %total)
