import random

player_1_name = ""
player_2_name = ""
P1S= 0
P2S= 0
def main():
    global P1S, P2S
    display_welcome()
    get_player_names()


    #P#S stands for Player # score

    next_turn = 1
    while P1S < 100 and P2S < 100:
        show_scoreboard()
        if next_turn == 1:
            P1S = P1S + player_turn()
            next_turn = 2
        else:
            P2S = P2S + player_turn()
            next_turn = 1

def display_welcome():

    print('''
      _____ _____ _____ 
     |  __ \_   _/ ____|
     | |__) || || |  __ 
     |  ___/ | || | |_ |
     | |    _| || |__| |
     |_|   |_____\_____|      
     
Welcome to Pig! You need 100 points to win.                                                           
    ''')

def roll_die():
    input("\nPress Enter to roll the dice...")

    die_roll = random.randrange(1, 7)

    print()
    print(" +---+ ")
    print(" |", die_roll, "| ")
    print(" +---+ ")
    print()

    return die_roll

def get_player_names():
    global player_1_name
    global player_2_name

    player_1_name = input("Enter the name of player 1: ")
    player_2_name = input("Enter the name of player 2: ")

def show_scoreboard():
    print("\nScoreboard")
    print('----------')
    print(player_1_name, ":", P1S)
    print(player_2_name, ":", P2S)

def player_turn():
    round_score = 0
    rolling = True

    while rolling :
        roll = roll_die()
        if roll == 1:
            rolling = False
            round_score = 0
        else:
            round_score = round_score + roll
            rolling = (input("press enter to continue or h to exit.") == "")



    return round_score



main()
