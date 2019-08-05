######## square root (wrong anser)##########33
import math
def squareroot(number):
    def square(num):
        return num * num
    return math.sqrt(square(number))

# print("Enter the number")
answer = int(raw_input("Enter the number"))
print(str(answer) + "square root is" + str(squareroot(answer)))
