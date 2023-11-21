#!/usr/bin/env python3

def power(N, M):
    if M == 0:
        return 1
    return N * power(N,M-1)