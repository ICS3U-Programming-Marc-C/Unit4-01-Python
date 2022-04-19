#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# Sum of numbers program


def main():
    # Defining variables
    counter = 0
    loop_sum = 0
    user_input = input("Enter a positive number: ")
    try:
        user_num = int(user_input)
        if user_num < 0:
            exit()

        while counter < user_num:
            counter = counter + 1
            print("Tracking {} times through loop.".format(counter))
            loop_sum = loop_sum + counter
        print("The sum of the numbers from 0 to {} = {}".format(user_num, loop_sum))

    except:
        print("Invalid input.\nNot a proper number")


if __name__ == "__main__":
    main()
