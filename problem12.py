def get_divisors(number):
    if number == 1:
        return 1
    count = 0
    for i in range(1, int(number // 2)):
        if number % i == 0:
            count += 1
    return count + 1


no_of_divisors = 0
number = 1
triangular_number = 0

while no_of_divisors < 500:
    print(number)
    triangular_number += number
    no_of_divisors = get_divisors(triangular_number)
    number += 1

print(triangular_number)
