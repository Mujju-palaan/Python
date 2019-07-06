#grades = [71, 81, 77, 84]
#for i in range(len(grades)):
#    grades[i] = grades[i] + 5
#print(grades)
#####same answer to diff type #######
grades = [71, 81, 77, 84]
print(grades)
grades = [grade + 5 for grade in grades]
print(grades)
#############
words = ['NOW','IS','THE','TIME']
print(words)
words = [word.lower() for word in words]
print(words)