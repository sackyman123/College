#!/usr/bin/env python3

class Score():
    def __init__(self, goals = 0, points = 0):
        self.goals = goals
        self.points = points
    def __str__(self):
        return f'{self.goals} goal(s) and {self.points} point(s)'
    def Score(self, goals, points):
        self.goals += goals
        self.points += points
