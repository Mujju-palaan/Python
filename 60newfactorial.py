# Easy factorial method
def factorial(number):
    if number <= 1 :
        return 1
    else:
        return number * factorial(number - 1)

# print(factorial(5))

print("Enter a number")
number = int(raw_input())
print(str(number) + "! anwer is " + str(factorial(number)))
# print(number + "! anwer is " + str(factorial(number)))