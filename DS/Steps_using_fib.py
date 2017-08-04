
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

def steps(n):
    
    if n==1:
        return 1
    first = 1
    second = 2
    for i in range(3,n+1):
        third = first+second
        first = second
        second = third
    
    return second

print(steps(2))

