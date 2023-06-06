#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for a in range(len(sys.argv)):
        if a != 0:
            sum = sum + int(sys.argv[a])
    print("{:d}".format(sum))
