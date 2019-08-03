import formula
print(formula.sqrt(9))
############################
def square(number):
    print("not from the formula module")
    return number*number
num = 12
print("square from forluma.py:")
print(formula.square(num))
print("Square from main program: ")
print(square(num))