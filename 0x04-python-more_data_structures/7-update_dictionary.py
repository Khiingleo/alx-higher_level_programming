#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        if key in a_dictionary:
            a_dictionary[key] = value
            return a_dictionary
        elif isinstance(key, str) and len(key) != 0:
            new = {key: value}
            a_dictionary.update(new)
            return a_dictionary
    else:
        return None
