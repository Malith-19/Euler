number = 600851475143

def maxPrime(n):
    for i in range(2,n):
        if n%i ==0:
            for j in range(2,i):
                if i%j ==0:
                    break
            else:
               max_prime = i
    return max_prime
  
  print(maxPrime(number))
