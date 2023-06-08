#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    command = len(argv) - 1
    if command == 0:
        print("0 arguments.")
    elif command == 1:
        print("1 argument:")
    else:
        print(f"{command} arguments:")
    for num in range(command):
        print(f"{num + 1}: {argv[num + 1]}")
