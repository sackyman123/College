import sys 
import random

intake = sys.stdin.readline()
intake = intake.strip().split()

def dice_roll(amount, number):
    total = 0
    for i in range(amount):
        roll = random.randint(1,number)
        print(roll)
        total += roll
    print(f'your total is {total}')

dice_roll(int(intake[0]),int(intake[1]))
