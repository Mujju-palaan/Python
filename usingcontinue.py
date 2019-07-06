number = 0
denom = 0
while denom != -1:
    print("enter  numberator: ")
    numer = float(raw_input())
    print("enter a denominator: ")
    denom = float(raw_input())
    if denom == 0:
        continue
    print(numer / denom)