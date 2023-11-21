#!/usr/bin/env python3

n = int(input())
final = ''
while n > 0:
    if n % 2 == 0:
        final += "9"
    else:
        final += "3"
    n = (n- 1) // 2
print(final)