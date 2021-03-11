
num = 2
while True:
    for i in range(2,num):
        if num%i ==0 :
            break
    else:
        prime_count+=1
        if prime_count == wanted_prime_count:
            print(num)
            break
    num += 1
