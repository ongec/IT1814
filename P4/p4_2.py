weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
bmi = weight / (height * height)
if bmi <18.5:
    desc="You are underweight!"
elif bmi <23:
    desc="You are in normalweight!"
elif bmi <27.5:
    desc="You are overweight!"
else:
    desc="You are obese!"
print(f'\nYour BMI is {bmi:.2f}\n{desc}')

