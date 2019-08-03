#########TAX##########
# 0-240  0%
# 241-480  15%
# 481-  28%
def TAX(amount):
    if amount <= 240:
        return 0
    elif amount >240 and amount<480 :
        return amount * .15
    else:
        return amount * .28
print("Enter amount  :")
amount = int(raw_input())
print("The tax is " + str(TAX(amount)))