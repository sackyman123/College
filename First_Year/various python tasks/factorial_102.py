#!/usr/bin/env python3

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)