#1a
v1 , v2 = '3', 5
v1 = '3'
v2 = 5
# v3= v1+ v2
v3 = int( v1 ) + v2
print(f"{v1} + {v2} = {v3}")

#1b
v4 , v5 = 5.1 , '3.5'
v6 = v4 + float(v5)
print(f"{v4} + {v5} = {v6}")

#1c
no = float( input("Enter a number : "))
no1 = int(no) #cast to int, discard decimal
print(f"Your number is between {no1} and {no1+1}")
print(f"It is nearer to {no:.0f} with 2 dec pt:{no:.2f}")
