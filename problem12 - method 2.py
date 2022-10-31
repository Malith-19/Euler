def get_divisors(number):
    count = 0
    for i in range(1, int(number ** 0.5)):
        if number % i == 0:
            count += 1
            if not number // i == i:
                count += 1
    return count


no_of_divisors = 0
number = 1
triangular_number = 0

while no_of_divisors < 500:
    triangular_number += number
    no_of_divisors = get_divisors(triangular_number)
    number += 1

print(triangular_number)

