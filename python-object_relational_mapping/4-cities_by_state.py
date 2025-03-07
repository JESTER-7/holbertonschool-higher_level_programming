#!/usr/bin/python3
"""
database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysqlName = sys.argv[1]
    mysqlPassword = sys.argv[2]
    dbName = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=mysqlName, passwd=mysqlPassword, db=dbName, port=3306)
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
    """
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
