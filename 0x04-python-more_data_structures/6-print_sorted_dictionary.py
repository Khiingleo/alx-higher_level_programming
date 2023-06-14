#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.keys())
    for i in sort:
        print("{}: {}".format(i, a_dictionary[i]))

# alternative
# for key, value in sorted(a_dictionary.items()):
#       print("{}: {}".format(key, value))
