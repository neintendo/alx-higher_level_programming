#!/usr/bin/python3
"""
This script adds all arguments to a Python list then saves them to a JSON file.
"""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

list = []

try:
    list = load_from_json_file("add_item.json")
except FileNotFoundError:
    with open('add_item.json', 'w', encoding='utf-8') as file:
        file.write("[]")
for a in range(len(sys.argv)):
    if a != 0:
        list.append(sys.argv[a])

save_to_json_file(list, "add_item.json")
