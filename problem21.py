# function to get the sum divisors of a number
def sumOfDivisors(n):
    tot = 0
    for i in range(1,n//2+1):
        if(n%i==0):
            tot+= i
            # print(i)
    return tot

# function to check if a number is amicable
def isAmicable(n):
    divSum = sumOfDivisors(n)
    if n == sumOfDivisors(divSum) and n != divSum:
        return True
    else:
        return False
    
# driver code
def main():
    amicableSum = 0
    for i in range(1,10000):
        if isAmicable(i):
            amicableSum += i
    print(amicableSum)

main()