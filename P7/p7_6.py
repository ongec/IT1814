answerList = ['C', 'D', 'B', 'A', 'B', 'D', 'A', 'C', 'D', 'C']
highest = 0 # need a variable to remember current highest score
while True: # Allow mult attempts until user wants to stop
    studentAttempt = [] # stores student's answer

    correct = 0
    print('\nPlease enter your Review Exercise answer')
    for n in range(10):
        #store student's answer
        studentAttempt.append(input(f'MCQ #{n+1}: ').upper())
         #compares for correct answer
        if answerList[n] == studentAttempt[n]:
            correct += 1
    if correct > highest:
        highest = correct
    print(f'You have {correct} correct answer and {10-correct} wrong answer')
    tryAgain = input("Do you want to try again? (Y/N): ").lower()
    if tryAgain !='y': #just for lab practice, did not do full error check
        break
print(f'\nYour highest mark for Review Exercise is {highest}')
print('\nReview Exercise Answers: ')
print(answerList)

