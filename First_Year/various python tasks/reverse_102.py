#!/usr/bin/env python3

def reverse(l):
    if l == []:
        return []
    else:
        return reverse(l[1:]) + [l[0]]
