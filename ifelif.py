print("enter a numeric grade:")
grade = int(raw_input())
if grade >= 90:lettergrade = "A"
elif grade >= 80:lettergrade = "B"
elif grade >= 70:lettergrade = "C"
elif grade >= 60:lettergrade = "D"
elif grade <= 59:lettergrade = "F"
else:print("Did not recognize input")
print("Your letter grade is: " + lettergrade )