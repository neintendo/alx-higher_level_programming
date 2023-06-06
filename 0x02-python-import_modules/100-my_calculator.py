#!/usr/bin/python3
import calculator_1 as calculator

if __name__ == "__main__":
    import sys

    operators = ["+", "-", "*", "/"]
    valid_OP = 0

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for a in range(len(operators)):
        if sys.argv[2] == operators[a]:
            valid_OP = 1
    if valid_OP == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        c = calculator.add(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, c))
    elif sys.argv[2] == "-":
        c = calculator.sub(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, c))
    elif sys.argv[2] == "/":
        c = calculator.div(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, c))
    elif sys.argv[2] == "*":
        c = calculator.mul(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, sys.argv[2], b, c))

