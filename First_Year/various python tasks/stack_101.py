#!/usr/bin/env python3

class Stack():
    def __init__(self):
        self.s = []
    def push(self, object):
        self.s.append(object)
    def is_empty(self):
        if self.s:
            return False
        else:
            return True
    def top(self):
        return self.s[-1]
    def pop(self):
        return self.s.pop()
    def __len__(self):
        return len(self.s)

