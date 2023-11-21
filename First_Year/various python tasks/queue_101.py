#!/usr/bin/env python3

class Queue():
    def __init__(self):
        self.q = []
    def enqueue(self,object):
        self.q.append(object)
    def dequeue(self,object=None):
        if object != None:
            return self.q.pop(self.q.index(object))
        else:
            return self.q.pop(0)
    def is_empty(self):
        if self.q:
            return False
        else:
            return True
    def first(self):
        return self.q[0]
    def __len__(self):
        return len(self.q)
