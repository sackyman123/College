#!/usr/bin/env python3

def maximum(L):
    if len(L) == 1:
        return L[0]
    if L[0] < L[-1]:
        return maximum(L[1:])
    else:
        return maximum(L[:-1])
    
def main():
    max = None
    print(maximum([6,5,1,3,4]))
    print(maximum([6,5,11,3,4]))
    print(maximum([6,15,11,13,14]))
    print(maximum([6,15,11,13,4]))

if __name__ == '__main__':
    main()