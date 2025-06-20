#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def usage_exit():
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)


def unknown_operator_exit():
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage_exit()

    a_str, operator, b_str = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        usage_exit()

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        unknown_operator_exit()

    print(f"{a} {operator} {b} = {result}")
