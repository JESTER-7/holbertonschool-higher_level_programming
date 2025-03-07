#!/usr/bin/python3
"""
satabase
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
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cursor.execute(query, (stateName,))

    cities = cursor.fetchall()
    print(", ".join(name for (name, ) in cities))

    cursor.close()
    db.close()
