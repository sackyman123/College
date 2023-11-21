#!/usr/bin/env python3

def minimum(L):
    if len(L) == 1:
        return L[0]
    if L[0] > L[-1]:
        return minimum(L[1:])
    else:
        return minimum(L[:-1])

def main():
    min = None
    print(minimum([6,5,1,3,4]))
    print(minimum([6,5,11,3,4]))
    print(minimum([6,15,11,13,14]))
    print(minimum([6,15,11,13,4]))

if __name__ == '__main__':
    main()