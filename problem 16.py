def digit_sum(n):
    str_n = str(n)
    total = 0
    for digit in str_n:
        total += int(digit)
    return total


print(digit_sum(2 ** 1000))
