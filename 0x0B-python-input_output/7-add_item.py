#!/usr/bin/python3
"""adds all arguments to a Python list and then save them
to a file
"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        file_items = load_from_json_file(filename)
    except FileNotFoundError:
        file_items = []

    file_items.extend(sys.argv[1:])
    file_items = save_to_json_file(file_items, filename)
