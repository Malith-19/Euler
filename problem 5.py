
import time
start_time = time.time()


n = 0
while True:
    n += 20
    checkables = [20,19,18,17,16,14,13,11]
    for i in checkables:
        if n%i:
            break
    else:
        print(n)
        break

end_time = time.time()
print("execution time: ",str(end_time-start_time),"seconds...")
