#!/usr/bin/env python3

class Element():
    def set_attributes(self, number, name, symbol, boiling_point):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.bp = boiling_point
    def print_attributes(self):
        print(f'Number: {self.number}\nName: {self.name}\nSymbol: {self.symbol}\nBoiling point: {self.bp} K')
