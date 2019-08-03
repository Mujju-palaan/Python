def factorial(number):
    product = 1
    for i in range (1,number+1):
        product *= i
    return product
print("Enter a number  :")
number = int(raw_input())
print(str(number) + "! equals to " + str(factorial(number)))

