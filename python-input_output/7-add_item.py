#!/usr/bin/python3
"""file"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = []
for i in sys.argv:
    args.append(i)
args.pop(0)
file = 'add_item.json'
try:
    list = load_from_json_file(file)
except FileNotFoundError:
    list = []
list.extend(args)
save_to_json_file(list, file)
