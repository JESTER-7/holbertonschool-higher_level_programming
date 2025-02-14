#!/usr/bin/env python3
"""serialize and deserialize to xml"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize the python dictionary into XML"""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file)
    return True


def deserialize_from_xml(filename):
    """deserialize XML data from a file into a python dictionary"""
    tree = ET.parse(filename)
    dict = {}
    root = tree.getroot()
    for element in root:
        dict[element.tag] = element.text
    return dict
