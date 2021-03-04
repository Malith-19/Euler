import math

number = 600851475143

def maxPrime(n):
    upper_limit_factor = math.ceil(n**0.5)
    for i in range(2, upper_limit_factor):
        if n%i ==0:
            upper_limit_prime = math.ceil(i**0.5)
            for j in range(2,upper_limit_prime):
                if i%j ==0:
                    break
            else:
                max_prime = i
    return max_prime

print(maxPrime(number))
