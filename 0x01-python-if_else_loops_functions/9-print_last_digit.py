#!/usr/bin/python3
def print_last_digit(number):

    if number > 0:
        number = number % 10
        print("{:d}".format(number), end='')
        return (number)

    elif number < 0:
        number = (number * -1) % 10
        print("{:d}".format(number), end='')
        return (number)

    else:
        print("{:d}".format(number), end='')
        return (number)
