#!/usr/bin/env python3

import sys
line = sys.stdin.readline()
line = line.strip().split()
word1 = line[0]
word2 = line[1]
if len(word1) > len(word2):
    longest = word1
    check = word2
else:
    longest = word2
    check = word1
letters = []
for i in range(len(longest)):
    if longest[i] in check:
        letters.append(longest[i])
final_occurence = letters[-1]
i = -1
while True:
    if word1[i] == final_occurence:
        break
    i = i - 1
word1_count = len(word1) + i
i = -1
while True:
    if word2[i] == final_occurence:
        break
    i = i - 1
word2_count = len(word2) + i
for i in range(word1_count):
    print(f'{"." * (word2_count)}{word1[i]}{"." * (len(word2) - word2_count - 1)}')
print(word2)
for i in range(len(word1) - word1_count - 1):
    print(f'{"." * (word2_count)}{word1[i+word1_count+1]}{"." * (len(word2) - word2_count - 1)}')