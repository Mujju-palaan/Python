# def square(number):
#     return number * number
# print("Enter a number")
# number = int(input())
# numsquared = square(number)
# print(str(number) + " squared = " + str(numsquared))
################################################
def Vowels(word):
    word = word.lower()
    count = 0
    for i in range(len(word)):
        if word[i] == "a" or word[i] == "e" \
            or word[i] == "i" or word[i] == "o" \
                or word[i] == "u":
            count += 1  # count = count + 1
    return count
print("Enter a word :")
word = str(raw_input())
print("There are " + str(Vowels(word)) + '  ' + "vowles in the word")