from random import randint
import time
print("Welcome to my Game, there are 4 statistics, Strength, Dexterity, Inteliigence and Vitality\n\n")
print("Strength will determine your base amount of damage\n")
print("Dexterity will determine your dodge chance\n")
print("Intelligence will determine your critical strike chance\n")
print("Vitality will determine your health\n\n")


def take_scores_1():
    print(f'Player 1 : you have a total of 20 points to allocate, please type them line by line')
    print("strength score: ")
    global str1
    try:
        global str1
        str1 = int(input())
    except ValueError:
        print(f'Use numbers u cunt')
        return
    print("dexterity score: ")
    global dex1
    try:
        global dex1
        dex1 = int(input())
    except ValueError:
        print(f'Use numbers u cunt')
        return
    print("intelligence score: ")
    global int1
    try:
        global int1
        int1 = int(input())
    except ValueError:
        print(f'Use numbers u cunt')
        return
    print("vitality score: ")
    global vit1
    try:
         global vit1
         vit1 = int(input())
    except ValueError:
        print(f'Use numbers u cunt')
        return

def take_scores_2():
    print(f'Player 2 : you have a total of 20 points to allocate, please type them line by line')
    print("strength score: ")
    global str2
    try:
        global str2
        str2 = int(input())
    except ValueError:
        print(f'Use numbers u cunt')
        return
    print("dexterity score: ")
    global dex2
    try:
        global dex2
        dex2 = int(input())
    except ValueError:
        print(f'Use numbers u cunt')
        return
    print("intelligence score: ")
    global int2
    try:
        global int2
        int2 = int(input())
    except ValueError:
        print(f'Use numbers u cunt')
        return
    print("vitality score: ")
    global vit2
    try:
         global vit2
         vit2 = int(input())
    except ValueError:
        print(f'Use numbers u cunt')
        return

def basic_attack(DMG, OPP_DODGE, CRIT):
    chance = randint(1,100)
    if OPP_DODGE > chance:
        print(f'Oh no! Your attack missed')
        DMG = 0
    elif CRIT > chance:
        print(f'Lucky! You hit a critical attack')
        DMG = DMG * 2
    else:
        print(f'Your attack has hit, well done')
    return(DMG)

player_1_stats = True
str1 = None
dex1 = None
int1 = None
vit1 = None
take_scores_1()

while player_1_stats:
    print(f'Player 1 these are your scores, is this correct?')
    print(f'\nStrength {str1}\nDexterity {dex1}\nIntelligence {int1}\nVitality {vit1}\n')
    print(f'Yes or No')
    response = input()
    if response == 'no' or response =="No":
        str1 = None
        dex1 = None
        int1 = None
        vit1 = None
        take_scores_1()
    try:
        if str1 + dex1 + int1 + vit1 != 20:
            print(f'\nThe sum of your scores was incorrect please try again')
            take_scores_1()
    except TypeError:
        print(f'Error please try again')
        take_scores_1()
    else:
        print(f'\nThank you')
        player_1_stats = False

str2 = None
dex2 = None
int2 = None
vit2 = None
take_scores_2()

player_2_stats = True
while player_2_stats:
    print(f'Player 2 these are your scores, is this correct?')
    print(f'\nStrength {str2}\nDexterity {dex2}\nIntelligence {int2}\nVitality {vit2}\n')
    print(f'Yes or No')
    response = input()
    if response == 'no' or response =="No":
        str1 = None
        dex1 = None
        int1 = None
        vit1 = None
        take_scores_2()
    try:
        if str2 + dex2 + int2 + vit2 != 20:
            print(f'\nThe sum of your scores was incorrect please try again')
            take_scores_2()
    except TypeError:
        print(f'Error please try again')
        take_scores_2()
    else:
        print(f'\nThank you')
        player_2_stats = False


print(f'player 1 it is now time to select your class\nYou have 3 options\n\n1) Tank\n2) Fighter\n3) Assasin.')
class_select = input()
while True:
    try:
        int(class_select)
        break
    except:
        print("please input a number")
        class_select = input()

if class_select == "1":
    vit1 += 6
    if dex1 > 3:
        dex1 -= 3
elif class_select == "2":
    str1 += 3
    dex1 += 2
    int1 += 2
else:
    str1 += 6
    if vit1 > 3:
        vit1 -= 3
    int1 += 4

print(f'player 2 it is now time to select your class\nYou have 3 options\n\n1) Tank\n2) Fighter\n3) Assasin.')
class_select = input()
while True:
    try:
        int(class_select)
        break
    except:
        print("please input a number")
        class_select = input()
    
if class_select == "1":
    vit2 += 6
    if dex2 > 3:
        dex2 -= 3
elif class_select == "2":
    str2 += 3
    dex2 += 2
    int2 += 2
else:
    str2 += 6
    if vit2 > 3:
        vit2 -= 3
    int2 += 4

score1 = 0
score2 = 0
while score1 < 3 and score2 < 3:
    hp1 = vit1 * 20
    dmg1 = str1 * 2
    dodge1 = dex1 * 4
    crit1 = int1 * 4
    hp2 = vit2 * 20
    dmg2 = str2 * 2
    dodge2 = dex2 * 4
    crit2 = int2 * 4
    print(f'Player 1 Health\n{hp1}\n\nPlayer 2 health\n{hp2}')
    i = 1
    while hp1 > 0 and hp2 > 0:
        print(f'Round {i}, hit enter to begin.\n')
        input()
        print(f'Player 1 strikes first\n')
        time.sleep(1)
        player_1_attack = basic_attack(dmg1, dodge2, crit1)
        print(f'Player 1 deals {player_1_attack} damage\n')
        hp2 = hp2 - player_1_attack
        time.sleep(1)
        print(f'Player 2 hp is now {hp2}\n')
        time.sleep(2)
        print(f'Player 2 strikes\n')
        time.sleep(1)
        player_2_attack = basic_attack(dmg2, dodge1, crit2)
        print(f'Player 2 deals {player_2_attack} damage\n')
        hp1 = hp1 - player_2_attack
        time.sleep(1)
        print(f'Player 1 hp is now {hp1}\n')
        time.sleep(1)
        i += 1
    if hp1 <= 0:
        print(f'Player two has won this round the current score is\n player one: {score1} vs player two: {score2}')
    elif hp2 <= 0:
        print(f'Player one has won this round the current score is\n player one: {score1} vs player two: {score2}')