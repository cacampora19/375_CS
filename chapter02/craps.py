# craps.py
#
# This program simulates the dice game craps. The user starts with $100 and is allowed to bet on the roll of two
# six-sided dice:
#
#  - A roll of 7 or 11 on the opening throw results in a win
#  - A roll of 2, 3, or 12 on the opening throw results in a loss
#  - A roll of anything else means the user has to re-roll the dice until that same number is rolled (a win) or a 7 is
#    rolled (a loss)
#
# A win pays whatever amount was bet. A loss takes the amount bet. The user can continue to play until he/she is out of
# money.
#
# by Mr. Ciccolo

import random

cash = 0
bet = 0

def main():
    global cash

    cash = 100


    display_welcome()


    play_again = True # Boolean- Something that is either true and false
    while play_again:
        place_bet()
        total = roll_dice()
        if total == 7 or total == 11:
            print("You win!")
            print("You have $", cash, sep="")
        elif total == 2 or total == 3 or total == 12:
            print("You lose!")
            cash = bet - cash
            print("You have $", cash, sep="")
        else:
            re_roll(total)

        print() # Blank line for spacing

        if cash <= 5:
            play_again = False
            print("You lost! You have no money left! Feel free to vist www.gamblersanonymous.org")
        else:
            play_again = (input("Enter 'N' to quit! ") == '')
            clear_screen()

def clear_screen():
    for i in range(20):
        print()


def display_welcome():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                              $")
    print("$ Welcome to the Computer Science Craps Table! $")
    print("$                                              $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    #how to play?

def roll_dice():
    input("\nPress Enter to roll the dice...") # We don't do anything with the input, we're just using it to pause the game

    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    total = die1 + die2

    print()
    print(" +---+   +---+")
    print(" |", die1, "| + |", die2, "| =", total)
    print(" +---+   +---+")
    print()

    return total


def re_roll(point):
    global cash
    global bet
    print("You have to keep rolling until you get another", point)
    print() # Blank line for spacing

    total = roll_dice()
    while total != point and total != 7:
        total = roll_dice()

    if total == point:
        print("You win!")
        cash = cash + bet

    else:
        print("You lose!")
        cash = cash - bet

    print("You have $", cash, sep="")

def place_bet():
    global cash, bet
    raw_bet = input("You can bet $5-$" + str(cash) + ". How much do you want to bet?: ")
    while raw_bet == "":
        raw_bet = input("You can bet $5-$" + str(cash) + ". How much do you want to bet?: ")

    bet= eval(raw_bet)

    if bet < 5:
        print("\nHey, the minimum bet is $5. I'll let you off with warning and make it $5 this game")
        bet = 5

    elif bet > cash:
        print("\nHey, you only have ", cash,", you can't bet ", bet,"!\nDon't play tricks on me! \nI see you feel lucky today, so I'll put down all you have", sep="")
        bet = cash


main()
