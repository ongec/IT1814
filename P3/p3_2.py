ip = input('Enter a number: ')
try:
    ipf=float(ip)   #Any exception inside try can be handled   

except ValueError:
    print("%s is not a valid number" % (ip))
else:
    print("%s is a valid number" % (ip))
    print("Program exit with no exception raised")
