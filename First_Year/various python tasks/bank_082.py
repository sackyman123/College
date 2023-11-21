#!/usr/bin/env python3

class BankAccount():
    def __init__(self, optional = 0):
        self.balance = optional
    def deposit(self, balance):
        self.balance += balance
    def withdraw(self, amount):
        self.balance -= amount
    def __str__(self):
        print(f'Your current balance is: {self.balance}')

