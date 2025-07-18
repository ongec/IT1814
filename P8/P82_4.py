# code the function addStduent
def addStduent(name, dict):
    dict[name] = {}
    a1 = float(input(f'Enter attempt1 for {name}: '))
    dict[name]['attempt1'] = a1
    a2 = float(input(f'Enter attempt2 for {name}: '))
    dict[name]['attempt2'] = a2
# code the function getGrade
# it returns the final grade
def getGrade(score):
    if score >= 80: return 'A'
    elif score >= 70: return 'B'
    elif score >= 60: return 'C'
    elif score >= 50: return 'D'
    else: return 'F'
# code the function getFinalscore
# it returns the final score
def getFinalscore(name, dict):
    if dict[name]['attempt1'] > dict[name]['attempt2']:
        return dict[name]['attempt1']
    else:
        return dict[name]['attempt2']
# 2 attempts are stored in dictionary
# highest attempt will be the finalScore   
results = {
'jane': {'attempt1':75.5, 'attempt2':80.5}, 
'john': {'attempt1':68.5, 'attempt2':60.5}
}
# calls to add in 2 attempts for jimmy
addStduent('jimmy',results)
print()
# calls getFinalscore to get final score
# calls disdplayFinalGrade to display grade
for stud in results:
    finalScore = getFinalscore( stud, results )
    grade = getGrade( finalScore )
    print(f"{stud}: final score = {finalScore}, grade = {grade}")

