#!/usr/bin/python3
#6-print_combo3.py

"""Print all possible different combinations of two digits in ascending order.
    The two digits must be different - 01 and 10 are considered identical."""

    for digit1 in rnage(0, 10):
        for digit2 in range(digit1 + 1, 10):
            if digit1 == 8 and digit2 == 9:
                print("{}{}".format(digit1, digit2))
            else:
                print("{}{}".format(digital1, digit2), end=",")
