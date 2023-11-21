#!/usr/bin/env python3

import sys

vowels = ['aa','ee','ii','oo','uu']

has_double = []
count_list = []
for lines in sys.stdin.readlines():
    lines = lines.strip().lower()
    count = 0
    for i in range(1,len(lines)):
        if lines[i] + lines[i-1] in vowels:
            i += 2
            count += 1
    if count >= 2:
        has_double.append(lines)
        count_list.append(count)

print(has_double[count_list.index(max(count_list))])