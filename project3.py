###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
print("The computer will think of 3 digit number that has no repeating digits")
print("You will then guess a 3 digit number")
print("The computer will then give back clues, the possible clues are:")
num = 1,2,3,4,5,6,7,8,9,0
import random
n = random.randint(1,10)
print([:3])
# guess = input("What is your guess? ")
# def guessed(num):
#     def Match(digits):
#         if guess == digits[:3] :
#             print(Match)
#     def Close(digits):
#         if guess  == (guess -1) or (guess +1) :
#             print(Close)
#     def Wrong(digits):
#         if guess != digits[:3]  :
#             print(Wrong)
#     return(guessed)
# print(guessed)

# import random
# n = random.randint(1, 99)
# guess = int(raw_input("Enter an integer from 1 to 99: "))
# while n != "guess":
#     print
#     if guess < n:
#         print('guess is low')
#         guess = int(raw_input("Enter an integer from 1 to 99: "))
#     elif guess > n:
#         print('guess is high')
#         guess = int(raw_input("Enter an integer from 1 to 99: "))
#     else:
#         print ('you guessed it!')
#         break
#     print




# Another hint:



# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
