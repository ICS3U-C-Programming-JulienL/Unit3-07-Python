#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 30, 2023
# This is a dating program for someone's grandchild

def main():
    # get the user's age
    print(
        "In this game, I will see if you are old enough to date my grandchild."
    )
    user_age_string = input("What is your age: ")

    try:
        # convert user guess to an integer
        user_age_int = int(user_age_string)

        # if the user is less than 0 or greater than 120, they are not a valid age
        if user_age_int < 0 or user_age_int > 120:
            print("{} is not a valid age".format(user_age_string))
        elif user_age_int > 25 and user_age_int < 40 :
            # otherwise if the user is greater than 35 or less than 40, then they can date the grandchild
            print("You can date my grandchild")
        elif user_age_int < 25:
            # otherwise if the user is less than 25, they are too young
            print("You are too young to date my grandchild.")
        elif user_age_int > 40:
            # otherwise if the user is less than 25, they are too old
            print("You are too old to date my grandchild.")
        
    except:
        # if user age cannot become an integer, then tell the user to enter an integer.
        print("{} is not a valid age. Enter an integer between 0 and 120.".format(user_age_string))


if __name__ == "__main__":
    main()
