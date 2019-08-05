# def square(number):
#     return number * number
# numbers = [1,2,3,4,5]
# print(numbers)
# numberssq = list(map(square , numbers))
# print(numberssq)

#########################
# def even(number):
#     if number % 2 == 0 :
#         return True
#     else:
#         return False
# numbers = list(range(1,11))
# print(numbers)
# evens = list(filter(even , numbers))
# print(evens)

##########import functools ##########
def sum(x,y):
    return x + y
import functools
numbers = list(range(1,11))
print(numbers)
sum = functools.reduce(sum , numbers)
print(sum)