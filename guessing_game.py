#File: guessing_game.py
import random
def main():

    magic_number = random.randrange(0,102);
    attempts = 1
    guess = eval(input("I have picked a number, try to guess it and I will tell you if it is too low or too high. Enter your guess here: "))

    while guess!= magic_number:
        if guess >= magic_number:
            guess = eval(input("You guessed too high! Try again: "))


        elif guess <= magic_number:
            guess = eval(input("You guessed too low! Try again: "))
        attempts = attempts + 1

    if guess == magic_number:
            if attempts == 1:
                print("\nYay! You guessed the magic number of", magic_number, "in 1 guess!")
            if attempts != 1:
                print("\nYay! You guessed the magic number of", magic_number, "in", attempts, "guesses!")
main()
