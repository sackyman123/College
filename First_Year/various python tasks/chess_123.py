#!/usr/bin/env python3

import sys

base = [2,2,4,4,4,16]

for lines in sys.stdin.readlines():
    lines = lines.strip().split()
    print(f'{base[0]-int(lines[0])} {base[1]-int(lines[1])} {base[2]-int(lines[2])} {base[3]-int(lines[3])} {base[4]-int(lines[4])} {base[5]-int(lines[5])}')