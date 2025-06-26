answer = "bee hive"
guess = "--- ----"
print('Guess the phrase :', guess)
while True :
    if guess == answer :
        print('Yeah, you got it right!')
        break
    char = input('Give me a letter : ')
    char = char.lower()
    i = 0
    for curChar in answer :
        if char == curChar :
            guess = guess[:i] + char + guess[i+1:]
        i += 1
    print('Guess the phrase :', guess)



