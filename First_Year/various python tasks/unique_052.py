#!/usr/bin/env python3

import sys
for lines in sys.stdin.readlines():
    seen_once_list = []
    duplicate_list = []
    final_list = []
    lines = lines.strip().split()
    for i in range(len(lines)):
        if lines[i] not in seen_once_list:
            seen_once_list.append(lines[i])
        else:
            duplicate_list.append(lines[i])

    for i in range(len(seen_once_list)):
        if seen_once_list[i] not in duplicate_list:
            final_list.append(seen_once_list[i])

    if final_list:
        print(max(final_list))
    else:
        print("none")