#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1
    result = 0
    for i in range(count):
        result += int(argv[i + 1])
    print(f"{result}")
