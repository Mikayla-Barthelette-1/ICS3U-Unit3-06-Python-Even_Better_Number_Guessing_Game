#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program creates an even better number guessing game

import random


def main():
    # this function creates the game

    # input
    number_guessed = input("Enter the number between 0 - 9: ")

    # process
    random_number = random.randint(0, 9)  # a number between 0 and 9
    try:
        number_guessed = int(number_guessed)
    except Exception:
        print("{0} is not an integer.".format(number_guessed))

    if number_guessed == random_number:
        print("You guessed the number!")
    else:
        print("Incorrect, the number was {0}.".format(random_number))

    # output
    print("Thanks for playing.")

    print("\nDone.")


if __name__ == "__main__":
    main()
