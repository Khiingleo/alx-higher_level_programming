#!/usr/bin/python3
for i in range(97, 123):
    i = chr(i)
    if i == "q" or i == "e":
        continue
    print(f"{i}", end="")
