#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv

    if len(argv) != 4:
        print("Usage {} <a> <operator> <b>")
        exit(1)


    operator = argv[2]
    lists = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in lists:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, operator, b, lists[operator](a, b)))
