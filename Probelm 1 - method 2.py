import time
start_time = time.time()

total = 0
no_of_threes = 999//3
no_of_fives = 999//5
no_of_fifteens = 999//15

sum_of_threes = (no_of_threes/2)*(3+3*no_of_threes)
sum_of_fives = (no_of_fives/2)*(5+5*no_of_fives)
sum_of_fifteens = (no_of_fifteens/2)*(15+15*no_of_fifteens)

print(int(sum_of_threes+sum_of_fives-sum_of_fifteens))

end_time = time.time()
print("the execution time: "+str(end_time-start_time)+" seconds...")
