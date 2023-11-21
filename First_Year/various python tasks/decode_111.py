#!/usr/bin/env python3

import sys 

vowels = ['a','e','i','o','u']

for lines in sys.stdin.readlines():
    lines = lines.strip().split()
    decoded = []
    for elements in lines:
        temp_string = ''
        characters = 0
        while characters < len(elements):
            temp_string += elements[characters]
            if elements[characters] in vowels:
                characters += 2
            characters += 1
        decoded.append(temp_string)
    print(" ".join(decoded))