#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub
    from sys import argv

    if len(argv) != 4:
        print(f"usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    ops = {"+": add, "-": sub, "/": div, "*": mul}
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    print(f"{a} {operator} {b} = {ops[operator](a, b)}")
