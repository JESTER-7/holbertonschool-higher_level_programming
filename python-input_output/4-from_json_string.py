#!/usr/bin/python3
"""file"""


import json


def from_json_string(my_str):
    """return an object representated by a json str"""

    return json.loads(my_str)
