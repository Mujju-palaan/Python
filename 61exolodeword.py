#####explode('hello') = 'h e l l o'##########
# def explode(word):
#     if len(word) <= 1 :
#         return word
#     else:
#         return word[0] + ' ' + explode(word[1:])

# print("Enter a word")
# word = raw_input()
# print(str(word) + " == " + str(explode(word)))

##################removeDublicates#############
def removeDups(word) :
    if len(word) <= 1 :
        return word
    elif word[0] == word[1] :
        return removeDups(word[1:])
    # elif word[0] == word[1] :
        # return removeDups(word(1:))
    else:
        return word[0] + removeDups(word[1:])

print("Enter double word")
word = raw_input()
print(removeDups(word))