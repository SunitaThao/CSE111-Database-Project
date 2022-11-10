import sqlite3
from sqlite3 import Error
from decimal import Decimal


def openConnection(_dbFile): #'C:\Users\sunit\OneDrive\Desktop\CSE 111\lab-1\tpch.sqlite'
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")
       
    print("success")
    print("++++++++++++++++++++++++++++++++++")
    

def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")
    file = open("output/1.out", "w")
    try:
        sql = "SELECT st_champ_name, max(st_banrate) FROM stats;"
        cursor = _conn.cursor()
        cursor.execute(sql)
        _conn.commit()

        rows = cursor.fetchall()
        for row in rows:
            l = '{:10} {:<20}\n'.format(row[0], row[1])
            print(l)
            file.write(l)
            _conn.commit()
        print("success")
        file.close()
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")
    file = open("output/2.out", "w")
    try:
        sql = (f"""SELECT sk_champ_name, sk_name
                    From skins;"""
        )
        cursor = _conn.cursor()
        cursor.execute(sql)
        _conn.commit()
       
        rows = cursor.fetchall()
        for row in rows:
            l = '{:20} {:<30}\n'.format(row[0], row[1])
            print(l)
            file.write(l)
            _conn.commit()
        print("success")
        file.close()
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")





def main():
    database = r"LOL.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        #dropTable(conn)
        #createTable(conn)
        #populateTable(conn)

        Q1(conn)
        Q2(conn)


    closeConnection(conn, database)


if __name__ == '__main__':
    main()
