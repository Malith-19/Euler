total = 0
num1 = 0
num2 = 1
while True:
    new = num1+num2
    if new >= 4e6 :
        break
    if new%2==0:
        total += new


    num1 = num2
    num2 = new
print(total)
