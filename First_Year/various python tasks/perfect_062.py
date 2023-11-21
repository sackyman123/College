#!/usr/bin/env python3
def get_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    return sorted(divisors)

def get_proper_divisors(n):
    return get_divisors(n)[:-1]

def is_perfect(n):
    if sum(get_proper_divisors(n)) == n:
        return True
    else:
        return False