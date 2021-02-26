import time
fib_dictionary = dict()

def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    if n in fib_dictionary:
        return fib_dictionary[n]
    return fib(n-1) + fib(n-2)

starting_time = time.time()

n=1
total = 0
while True:
    number = fib(n)
    if n not in fib_dictionary:
        fib_dictionary[n] = number
    if number >= 4e6:
        break
    if number%2 ==0:
        total+=number
    n+=1

print(total)

end_time = time.time()
print("execution time is :"+str(end_time-starting_time)+"seconds")
