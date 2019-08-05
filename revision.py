# num = 0
# while num<=10 :
#     print(num)
#     num = (num + 1)
###############################
# average = 0.0
# total = 0
# count = 0
# print("Enterr a grade (-1 to quit): ")
# grade = int(raw_input())
# print(grade)
# while grade != -1:
#     total = total + grade
#     count = count + 1
#     print("Enter a grade (-1 to quit): ")
#     grade = int(raw_input())
# average = total /count
# print("Average grade:" + str(average))
###################################
# sum = 0
# number = 1
# while number <= 10 :
#     sum = sum + number
#     number = number + 1
# print("The total is :" + str(sum))
######################################3
# balance = 5000
# rate = 1.2
# year = 1
# total = 0
# while year <= 10 :
#     total = balance + rate
#     year = year + 1
# print("Year :" + str(year) + ":"  + str(total) )
################################################
# numerator = 0
# denomerator = 0
# while denomerator != -1 :
#     print("Enter numerator ")
#     numerator = float(raw_input())
#     print("Enter denominator")
#     denomerator = float(raw_input())
#     print(numerator/denomerator)
##########################################
# message = "The recommended activity is :"
# print("Enter the temperature")
# temp = int(raw_input())
# if temp >80:
#     message = message + "swimming."
# elif temp >60:
#     message = message + "tripling"
# elif temp  >30:
#     message = message + "golf"
# elif temp >0 :
#     message = message + "dancing"
# else:
#     message = message + "Sitting near bornfire"
#     print(message)
###################################
# print("Enter a number")
# number1 = int(raw_input())
# print("Enter the second number")
# number2 = (raw_input())
# print("The sum is : " + str(number1+number2))
# print("The substraction is  :" + str(number1-number2))
# print("The multiplication is  :" + str(number1*number2))
# print("The division is  : " + str(number1/number2))
#########################################
# outFile = open('gradess.txt','w')
# grade = 0
# while (grade != "q") :
#     print("Enter a grade (-q to quit) ")
#     grade = raw_input()
#     outFile.write(grade + '\n')
# outFile.close()
######################################
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(numbers),2):
#     print([i])
#######################################
# numbers = [1,2,3,4,5]
# numbers = [number + 5 for number in numbers]
# print(numbers)
# for i in range(len(numbers)):
#     numbers [i] = numbers [i] + 5
##############################################
# words = ("THIS","IS","THE","PUPPY","SONG")
# print(words)
# words = [word.lower() for word in words]
# print(words)
#######################################