#!/usr/bin/env python3

import sys
import string

intake = sys.stdin.readlines()
no_dupes = []

for lines in intake:
    lines = lines.strip().split()
    print_list = []
    for elements in lines:
        var = elements
        if var[-1] in string.punctuation:
            var = var[:-1]
        if var.lower() not in no_dupes:
            print_list.append(elements)
            no_dupes.append(var.lower())
        else:
            print_list.append(".")
    print(" ".join(print_list))