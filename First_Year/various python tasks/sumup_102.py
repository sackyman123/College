#!/usr/bin/env python3

def sumup(N):
    if N == 0:
        return 0
    return N + sumup(N-1)
