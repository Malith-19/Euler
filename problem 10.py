def prime_sum(end, start=2):
    tot = 0
    primes = []
    for i in range(start, end):
        print(i)
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
            tot += i
    return tot


print(prime_sum(2*10**6))
