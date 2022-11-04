cache = {}  # cache collector which optimizes the program when repeating the same number.


def collatz(n):
    terms = 1
    while n != 1:
        if n in cache:
            terms += cache[n] - 1
            n = 1
        elif n % 2 == 0:
            n = n // 2
            terms += 1

        else:
            n = 3 * n + 1
            terms += 1

    return terms


max_terms = 0
max_number = 0
for i in range(1, 10 ** 6):
    terms = collatz(i)
    cache[i] = terms
    if terms > max_terms:
        max_number = i
        max_terms = terms

print(max_number)
