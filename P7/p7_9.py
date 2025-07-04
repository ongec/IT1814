results = { 
'Jane': [75, 80, 85], 
'John':[60, 68, 74], 
'Jerome':[81, 63, 77], 
'Jason':[55, 76, 67], 
'Jessica':[62, 45, 68], 
'Joanne':[52, 47, 51]}
englishMark = 0
mathMark = 0
scienceMark = 0
print('== Average of Student marks ==')
for key in results:
    average = sum(results[key]) / len(results[key])
    print(f'Average marks of {key} = {average:.1f} ')
    englishMark +=results[key][0]
    mathMark += results[key][1]
    scienceMark += results[key][2]
englishMark = englishMark/len(results)
mathMark = mathMark/len(results)
scienceMark = scienceMark/len(results)
print('\n== Average of Subject marks ==')
print(f'Average results for English = {englishMark:.1f} ')
print(f'Average results for Math = {mathMark:.1f} ')
print(f'Average results for Science = {scienceMark:.1f} ')

