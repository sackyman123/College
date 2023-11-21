#!/usr/bin/env python3

class BankAccount():
    def set_attributes(self, name, number, bal):
        self.name = name
        self.number = number
        self.balance = float(bal)
    def print_attributes(self):
        print(f'Name: {self.name}\nAccount number: {self.number}\nBalance: {self.balance:.2f}')
    def deposit(self, number):
        self.balance += float(number)
