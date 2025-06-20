#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        # If a or b can't be converted to int, the problem doesn't specify error handling,
        # but since it says "you can assume", we can skip handling here.
        pass

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))

