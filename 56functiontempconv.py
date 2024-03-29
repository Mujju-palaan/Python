def ftoc(temp):
    return (temp - 32.0) * (5.0 / 9.0)

def ctof(temp):
    return temp * (9.0 / 5.0) + 32.0

def convert(temp, toScale):
    if toScale == "c":
        return ftoc(temp)
    else:
        return ctof(temp)

print("Enter a temperatere :")
temp = int(raw_input())
print("Enter the scale to convert to :")
scale = raw_input()
convertedtemp = convert(temp, scale)
print(temp, convertedtemp, scale)