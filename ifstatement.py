print("Enter hours worked:")
hoursworked = int(raw_input())
rate = 25.00
if hoursworked > 40: grosspay = (40*rate)+((hoursworked-40)*(rate*1.5))
else:grosspay = hoursworked * rate
# print(str(grosspay))
print("gross pay: " + str(grosspay))