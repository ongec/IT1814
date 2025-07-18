import random
# Generates a number between 1 - 100 (inclusive)
def generate_number():
    return random.randint(1,100)
# generate a hint based on the guess
def compare(guess, answer):
    if guess > answer:
        result = 'Too high'
    elif guess < answer:
        result = 'Too low'
    else:
        result = 'Correct Answer'
    return result
# main program
answer = generate_number()  #generate random hidden number
print(answer)
tries = 3 
while tries > 0: 
    guess = int(input('Enter a number between 1 to 100: ')) 
    tries -= 1 
    # call function to generate hint
    result = compare(guess, answer)
    print(f" {result} \n")
    if result == 'Correct Answer': 
        break
else:
    print(f"Game over. The number is {answer}")


