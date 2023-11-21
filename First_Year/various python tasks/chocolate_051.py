#!/usr/bin/env python3

import sys 

for lines in sys.stdin.readlines():
    lines = lines.strip().split()
    lines = int(lines[0])
    if lines / 400 % 1 == 0:
        print(lines // 400)
    else:
        print(lines // 400 + 1)
