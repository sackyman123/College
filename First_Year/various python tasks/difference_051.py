#!/usr/bin/env python3

import sys

line_1 = sys.stdin.readline()
line_2 = sys.stdin.readline()
output = ""
i = 0
for elements in line_1:
    if line_1[i] == line_2[i]:
        output += "-"
    else:
        output += "*"
    i += 1

print(line_1.strip())
print(line_2.strip())
print(output[:-1])