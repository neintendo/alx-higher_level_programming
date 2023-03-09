#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# dgt: the last digit.
if number > 0:
    dgt = number % 10
    if dgt > 5:
        print(f"Last digit of {number} is {dgt} and is greater than 5")
    elif dgt == 0:
        print(f"Last digit of {number} is {dgt} and is 0")
    elif dgt < 6:
        print(f"Last digit of {number} is {dgt} and is less than 6 and not 0")

elif number < 0:
    dgt = (number * -1) % 10
    if dgt == 0:
        print(f"Last digit of {number} is {dgt} and is 0")
    else:
        print(f"Last digit of {number} is -{dgt} and is less than 6 and not 0")

else:
    print(f"Last digit of {number} is 0 and is 0")
