#!/usr/bin/env python3

def a_switch(position):
    if position == 1:
        position = 2
    elif position == 2:
        position = 1
    return position

def b_switch(position):
    if position == 2:
        position = 3
    elif position == 3:
        position = 2
    return position

def c_switch(position):
    if position == 1:
        position = 3
    elif position == 3:
        position = 1
    return position

position = int(input())
movements = input()
for i in range(len(movements)):
    if movements[i] == "A":
        position = a_switch(position)
    elif movements[i] == "B":
        position = b_switch(position)
    else:
        position = c_switch(position)

print(position)