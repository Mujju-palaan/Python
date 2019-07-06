numbers = (1,2,3,4,5)
sum = 0
for number in numbers:
    sum = sum + number
    print(number)
print("The sum is :" + '  '+ str(sum))
#Another program
words = ("now","is","the","time")
for word in words:
    print(word)
max = 0
for i in range(1,len(words)):
    if len(words[i]) > len(words[max]):
        max= i
print("the longest word is " + words[max])