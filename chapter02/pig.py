import random

WIN = 100

player_1_name = ""
player_2_name = ""
player_1_score= 0
player_2_score= 0


def main():
    global player_1_score, player_2_score, player_1_name, player_2_name, WIN
    display_welcome()
    get_player_names()

    next_turn = 1
    while player_1_score < WIN and player_2_score < WIN:
        show_scoreboard()
        if next_turn == 1:
            print("\nIt's ", player_1_name,"'s turn", sep="")
            player_1_score = player_1_score + player_turn()
            next_turn = 2
        else:
            print("\nIt's ", player_2_name,"'s turn", sep="")
            player_2_score = player_2_score + player_turn()
            next_turn = 1

    winner()


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
    print(player_1_name, ":", player_1_score)
    print(player_2_name, ":", player_2_score)


def player_turn():
    round_score = 0
    rolling = True

    while rolling :
        roll = roll_die()
        if roll == 1:
            rolling = False
            round_score = 0
            print("Oh no! You busted!")
        else:
            round_score = round_score + roll
            rolling = (input("Press enter to continue or h to hold.") == "")

    return round_score


def winner():
    global player_1_score, player_2_score, player_1_name, player_2_name, WIN
    if player_1_score >= WIN:
        print("\nCongrats", player_1_name, "you win!")
    else:
        print("\nCongrats", player_2_name, "you win!")


main()
