#magic 8 ball 
import random

n = input()
num = random.randint(1,8)

if num == 1:
    print(n, 
    ",this is very unlikely")
elif num == 2:
    print(n, 
    ",this is somewhat unlikely")
elif num == 3:
    print(n,
     ",this might happen, but probably not")
elif num == 4:
    print(n, "is 50/50")
elif num == 5:
    print(n, 
    ",this will probably happen")
elif num == 6:
    print(n, 
    ",this is somewhat likely")
elif num == 7:
    print(n, 
    ",this is very likely")
elif num == 8:
    print("inconclusive")