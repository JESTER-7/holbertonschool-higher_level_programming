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
    stateName = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=mysqlName, passwd=mysqlPassword, db=dbName, port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (stateName,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
