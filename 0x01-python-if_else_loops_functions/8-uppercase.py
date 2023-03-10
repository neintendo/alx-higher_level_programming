#!/usr/bin/python3
def uppercase(str):
    output = ""
    for i in range(len(str)):
        char = ord(str[i])

        if char > 96 and char < 123:
            char = char - 32
            char = chr(char)
            output += char

        else:
            char = chr(char)
            output += char

    print("{:s}".format(output))
