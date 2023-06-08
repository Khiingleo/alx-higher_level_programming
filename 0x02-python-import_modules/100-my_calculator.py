#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    from sys import argv

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    op = argv[2]
    lists = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in list(lists.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, op, b, lists[op](a, b)))
