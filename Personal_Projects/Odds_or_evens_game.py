import random
#takes player input with limitations
def take_an_input():
    #specifically 1 or 2 as input
    choice = None
    while choice != 1 and choice != 2:
        try:
            choice = int(input("\n"))
            assert choice == 2 or choice == 1
        except:
            print(f'error: please input a number\n')
            continue
        if choice > 2 or choice < 1:
            print(f'error: please input a valid number\n')
    return choice
#takes player input with limitations too, but for numbers between 0 and 10
def finger_choice():
    choice = None
    while True:
        try:
            choice = int(input())
        except:
            print(f'error: please input a number\n')
            continue
        if choice < 0 or choice >= 10:
            print(f'error please input a valid number')
        else:
            return choice

def odds_or_evens():
    print(f'Would you like to be odds or evens in this game?\n\n1) Odds\n\n2) Evens')
    choice = take_an_input()
    if choice == 1:
        choice = "odds"
    else:
        choice = "evens"
    print(f'well great you have chosen {choice}\nis this correct?\n\n1) YES\n\n2) NO')
    confirmation = take_an_input()
    if confirmation == 1:
        return choice
    else:
        odds_or_evens()

#allows the entire game to replay or prints an exit message
def repeat():
    print(f'would you like to play again?\n1) YES\n2) NO')
    choice = take_an_input()
    if choice == 1:
        run_game()
    else:
        print("\nThank you for playing")

#variables for the long term history of the game
global history_log
history_log = []
global game
game = 1

def run_game(score1=0,score2=0):
    player_1_history = []
    player_2_history = []
    rounds_won = 0
    bonus_points = 0
    if score1 == 0 and score2 == 0:
        choice = odds_or_evens()
    #set the game loop to run until one player reaches 6 points
    while score1 <= 6 and score2 <= 6:
        print(f'please select the amount of fingers you would like to hold up, between 1 and 10.')
        player_1_fingers = finger_choice()
        player_2_fingers = random.randint(1,10)
        print(f'the computer has held out {player_2_fingers} fingers')
        player_1_history.append(player_1_fingers)
        player_2_history.append(player_2_fingers)
        total = player_1_fingers + player_2_fingers
        print(f'\nThe final number is.....\n\n{total}')
        #finding out if the final number is odd or even and then assigning the point values
        if total % 2 == 0:
            print(f'The final number is even\n')
            if choice == "evens":
                score1 += 2
                rounds_won += 1
                print("2 points to the player\n")
            else:
                score2 += 2
                print("2 points to the computer\n")
        else:
            print(f'The final number is odd\n')
            if choice == "odds":
                score1 += 2
                rounds_won += 1
                print("2 points to the player\n")
            else:
                score2 += 2
                print("2 points to the computer\n")
        if  total - player_1_fingers < total - player_2_fingers:
            print(f'bonus point goes to the player')
            score1 += 1
            bonus_points += 1
        elif total - player_1_fingers == total - player_2_fingers:
            print(f'you are evenly matched, no bonus point this round')
        else:
            print(f'bonus point goes to the computer')
            score2 += 1
        print(f'player score is currently: {score1}\nthe computers score is currently: {score2}\n\n')
    if score1 > 6:
        print(f'the player has won, congratulations\n')
    else:
        print(f'the computer wins this round, bettter luck next time\n')

    take_game_history(rounds_won, bonus_points)
    print(f'Here are the amounts of fingers held up by each player in each round\n\nPlayer          Computer')
    for i in range(len(player_1_history)):
        print(f'{player_1_history[i]:<16}{player_2_history[i]}')
    repeat()

#create a string per game that records itself within a list
def take_game_history(rounds_won, bonus):
    global game
    history_log.append(str(f'game {game}\n\nplayer won {rounds_won} round(s)\nDuring this game they also earned {bonus} bonus points\n\n'))
    game += 1

#defining the main programme that will be run
run_game()
print(f"\n\n --Game History:^20--")
for elements in history_log:
    print(f'{elements:^20}')