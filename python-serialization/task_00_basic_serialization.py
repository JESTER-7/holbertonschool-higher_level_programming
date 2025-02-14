#!/usr/bin/env python3
"""serialize and deserialize"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serialize a python dictionary in a JSON file
    data: python dictionary with data
    filename: If the output file already exists it should be replaced
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    load a file and deserialize it
    filename: return a python dictionary with the deseialized JSON data
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
