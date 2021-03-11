from math import log,ceil
wanted_prime_count = 10001
prime_count = 0

def find_upper_bound(n):
    return ceil(n*(log(n)+log(log(n))))

upper_bound = find_upper_bound(wanted_prime_count)
nums = [True]*(upper_bound+1)
nums[0] = False
nums[1] = False


for i in range(2,ceil(upper_bound**0.5)):
    for j in range(2,upper_bound//i):
        multi = i*j
        if nums[multi]:
            nums[multi] = False

for (index,is_prime) in enumerate(nums):
    if is_prime:
        prime_count+=1
        if prime_count == wanted_prime_count:
            print(index)
            break
