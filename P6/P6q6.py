txt = input('Enter text: ')
print('\nLength =',len(txt))
try:
    val=int(txt)
    print(f'Integer added 10 = { val + 10 }')
except:
    try:
        val=float(txt)
        print(f'float added 10 = { val + 10 }')
    except:
        print("Invalid float or int.")


