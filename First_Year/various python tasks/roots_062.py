#!/usr/bin/env python3

import math
import sys

def find_roots(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    d = (b**2) - (4*a*c)
    try:
        sol1 = (-b-math.sqrt(d))/(2*a)  
        sol2 = (-b+math.sqrt(d))/(2*a)
        return(sol1,sol2)
    except:
        return None

for lines in sys.stdin.readlines():
    lines = lines.strip().split()
    list = find_roots(lines[0],lines[1],lines[2])
    try:
        print(f'{list[0]}, {list[1]}')
    except TypeError:
        print(None)