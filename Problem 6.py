upper_limit = 100

sum_of_square = 0
square_of_sum = 0
total = 0

for i in range(1,upper_limit+1):
    sum_of_square += i**2
    total += i

square_of_sum = total**2

print(square_of_sum - sum_of_square)
