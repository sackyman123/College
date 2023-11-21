#!/usr/bin/env python3

class Customer():
    def __init__(self,name="",num=0,bal=0):
        self.name = name
        self.number = num
        self.balance = float(bal)

    def lodge(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if self.balance - amount > 0:
            self.balance -= amount
    
    def __str__(self):
        return f'Name: {self.name}\nNumber: {self.number}\nBalance: {self.balance:.2f}'

class Bank():
    def __init__(self):
        self.customers = {}
    
    def add(self,customer):
        self.customers[customer.number] = customer
    
    def lookup(self,number):
        if self.customers[number]:
            return self.customers[number]
        else:
            return None
    
    def remove(self,customer):
        self.customers[customer] = None