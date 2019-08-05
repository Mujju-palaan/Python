# def first(word):
#     return word[0]

# words = ['in','my','humble','opinion']
# print(words)
# acro = list(map(first ,words))
# print(acro)

####################
def first(word):
    return word[0]
words = ['in','my','humble','opinion']
acro = ''
acro = acro.join(list(map(first, words))).upper()
print(acro)