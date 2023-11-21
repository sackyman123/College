#!/usr/bin/env python3

class Lamp():
    def __init__(self, optional = False):
        self.on = optional
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
    def toggle(self):
        if self.on:
            self.on = False
        else:
            self.on = True