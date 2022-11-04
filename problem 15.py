import math


def ncr(n,r):
    return int((math.factorial(n))/(math.factorial(r)*math.factorial(n-r)))

grid_size = 20

print(ncr(grid_size*2,grid_size))