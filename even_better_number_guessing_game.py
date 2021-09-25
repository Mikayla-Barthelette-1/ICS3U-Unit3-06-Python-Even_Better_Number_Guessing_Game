#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program creates an even better number guessing game

import random


def main():
    # this function creates the game

    # input
    user_input = input("Enter the number between 0 - 9: ")

    # process
    random_number = random.randint(0, 9)  # a number between 0 and 9
    try:
        number_guessed = int(user_input)
        not_integer = "false"
    except Exception:
        not_integer = "true"
    finally:
        if not_integer == "true":
            print("{0} is not an integer.".format(user_input))
        elif number_guessed not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Incorrect, the number was {0}.".format(random_number))
        elif number_guessed == random_number:
            print("You guessed the number!")
        else:
            print("Incorrect, the number was {0}.".format(random_number))

    # output
    print("Thanks for playing.")
    print("\nDone.")


if __name__ == "__main__":
    main()
