#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(arguments))
        for a in range(len(sys.argv)):
            if a != 0:
                print("{:d}: {:s}".format(a, sys.argv[a]))
