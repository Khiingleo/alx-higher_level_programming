#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = {}
    for key, value in a_dictionary.items():
        mul = {key: value * 2}
        dic.update(mul)
    return dic
