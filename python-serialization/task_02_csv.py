#!/usr/bin/env python3
"""convert csv data to json"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """filename of csv"""

    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csvFile:
            readCSV = csv.DictReader(csvFile)
            dataCSV = []
            for rows in readCSV:
                dataCSV.append(rows)
        with open('data.json', mode='w', encoding='utf-8') as jsonFile:
            jsonFile.write(json.dumps(dataCSV))
        return True
    except FileNotFoundError:
        print("error: file not found")
        return False
