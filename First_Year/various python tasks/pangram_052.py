#!/usr/bin/env python3
import sys
for lines in sys.stdin.readlines():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    missing = ""
    lines = lines.strip().lower()
    for i in range(26):
        if alphabet[i] in lines:
            None
        else:
            missing += alphabet[i]
    if len(missing) == 0:
        print("pangram")
    else:
        print(f'missing {missing}')