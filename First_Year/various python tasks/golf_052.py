#!/usr/bin/env python3

import sys
scoreboard_dictionary = {}
disqualified = []

for lines in sys.stdin.readlines():
    lines = lines.strip().split()
    name = " ".join(lines[:-3])
    try:
        score = int(lines[-1]) + int(lines[-2]) + int(lines[-3])
        scoreboard_dictionary[score] = name
    except:
        disqualified.append(name)

ordered_scores = sorted(list(scoreboard_dictionary.keys()))

for i in range(len(ordered_scores)):
    try:
        print(f'{scoreboard_dictionary[ordered_scores[i]]}: {ordered_scores[i]}')
    except KeyError:
        continue
if disqualified:
    print(f'Disqualified: {", ".join(disqualified)}')