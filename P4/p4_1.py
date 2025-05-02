# Solution A
grade = input("Enter grade: ")

if grade == "A" or grade == "a" : 
    print("GPA 4.0")
elif grade=="B" or grade == "b":
    print("GPA 3.0")
elif grade == "C" or grade == "c":
    print("GPA 2.0")
elif grade == "D" or grade == "d":
    print("GPA 1.0")
else: 
    print("Invalid grade")


# Solution B
grade = input("Enter grade: ")
grade = grade.lower()

if grade == "a" : 
    print("GPA 4.0")
elif grade == "b":
    print("GPA 3.0")
elif grade == "c":
    print("GPA 2.0")
elif grade == "d":
    print("GPA 1.0")
else: 
    print("Invalid grade")



