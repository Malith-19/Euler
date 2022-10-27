# now we are using sieve method to find the primes in the given range

def sieve(n):
    prime = [True for i in range(n + 1)]

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # getting the sum of prime numbers
    total = 0
    for i in range(2, n):
        if prime[i]:
            total += i
    return total


print(sieve(2 * 10 ** 6))
