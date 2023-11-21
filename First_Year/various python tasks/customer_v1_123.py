#!/usr/bin/env python3

class Customer():
    def __init__(self,name="",num=0,bal=0):
        self.name = name
        self.number = num
        self.balance = float(bal)
    
    def __str__(self):
        return f'Name: {self.name}\nNumber: {self.number}\nBalance: {self.balance:.2f}'
