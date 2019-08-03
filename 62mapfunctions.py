# def square(number):
#     return number * number
# print("Enter a number")
# number = int(raw_input())
# print(str(number) + " Square is " + str(square(number)))

############### MAP high-order FUNCTION  ############
def square(number):
    return number * number
numbers = [1,2,3,4]
square = list(map(square, numbers))
print(square)

