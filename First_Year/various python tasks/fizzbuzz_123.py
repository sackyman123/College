#!/usr/bin/env python3

line = input()
line = line.strip().split()
num_1 = int(line[0])
num_2 = int(line[1])
limit = int(line[2])

for i in range(1,limit+1):
    if i % num_1 == 0 and i % num_2 == 0:
        print("fizzbuzz")
    elif i % num_1 == 0:
        print("fizz")
    elif i % num_2 == 0:
        print('buzz')
    else:
        print(i)