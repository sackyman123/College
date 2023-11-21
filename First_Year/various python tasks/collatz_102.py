#!/usr/bin/env python3

def collatz(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 1:
        return collatz(n * 3 + 1)
    else: 
        return collatz(n = n // 2)