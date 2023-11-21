#!/usr/bin/env python3

def count(S,L=0):
    if S:
        return count(S[:-1],L + 1)
    else:
        return L
    
def main():
    len = None
    print(count('cat'))
    print(count('catastrophe'))
    print(count(''))

if __name__ == '__main__':
    main()