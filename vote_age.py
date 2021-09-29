#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user input their age to see if they are able to vote


def main():
    # this tells the user if they can vote

    # input
    age_check = input("Please enter your age: ")

    # process & output
    try:
        integer_as_number = int(age_check)

        if integer_as_number >= 18:
            print("You are old enough to vote!")

        else:
            print("You are too young to vote!")

    except Exception:
        print("This is not a number!")

    finally:
        print("Thank you for checking your age to vote!")
        print("\nDone.")


if __name__ == "__main__":
    main()
