#5! = 5*4*3*2*1 = 120
#6 = 6 * 5!
print("Enter a number: ")
num = int(raw_input())
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(str(num) + "!= " + str(fact))