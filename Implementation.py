import sqlite3
from sqlite3 import Error

def openConnection(dbfile):
    print("Opening Database: ", dbfile)

    conn = None
    try:
        conn = sqlite3.connect(dbfile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
    return conn 

def closeConnection(conn, dbfile):
    print("++++++++++++++++++++++++++++++++++")
    print("Closing Database: ", dbfile)

    try:
        conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")



def dropTables(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Dropping Tables")

    try:
        sql = """drop table if exists Titles"""
        conn.execute(sql)

        sql = """drop table if exists Favorite"""
        conn.execute(sql)

        sql = """drop table if exists Genre"""
        conn.execute(sql)

        sql = """drop table if exists Rating"""
        conn.execute(sql)

        sql = """drop table if exists ReleaseDate"""
        conn.execute(sql)

        conn.commit()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")



def createTables(conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating Tables")

    try:
        sql = """create table Titles (
                t_sid           decimal(15,0) primary key,
                t_title         char(50) not null,
                t_type          varchar(10) not null,
                t_cast          char(152) not null,
                t_description   char(152) not null)"""
        conn.execute(sql)

        sql = """create table Genre (
                g_sid decimal(20,0) primary key,
                g_genre char(50) not null)"""
        conn.execute(sql)

        sql = """CREATE TABLE ReleaseDate (
                re_sid          decimal(20,0) primary key,
                re_release      decimal(20,0) not null,
                re_added        decimal(20,0) not null)"""
        conn.execute(sql)

        sql = """create table Rating (
                ra_sid          decimal(10,0) not null,
                ra_rating       varchar(10) not null)"""
        conn.execute(sql)

        sql = """create table Favorite (
                f_sid           decimal(9,0) not null,
                f_like          char(117) not null)"""

        conn.commit()
        print("success")
    except Error as e:
        conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")



def populateTables(conn):
    print("++++++++++++++++++++++++++++++++++")
    print ("Populating Tables")

    try:
        sql = """insert into Titles (t_sid, t_title, t_type, t_cast, t_description)
                select n_sid, n_title, n_type, n_cast, n_description
                from Netflix"""
        conn.execute(sql)

        sql = """insert into ReleaseDate (re_sid, re_release, re_added)
                select n_sid, n_release, n_added
                from Netflix"""
        conn. execute(sql)

        sql = """insert into Genre (g_sid, g_genre)
                select n_sid, n_listed
                from Netflix"""
        conn.execute(sql)

        sql = """insert into Rating (ra_sid, ra_rating)
                select n_sid, n_rating
                from Netflix"""
        conn.execute(sql)
    
        conn.commit()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")



def choices(conn):
    print("Enter the number of the option that you wish to use: ")
    print("     0. Exit the program.")
    print("     1. Search for a specific title.")
    print("     2. View Favorites list.")
    print("     3. Filter through our titles to be given a show recommendation.")
    print("     4. Receive a random title recommendation.")
    selection = int(input())
    return selection

def search(conn):
    print("you have selected option 1")

def favorites(conn):
    print("you have selected option 2")

def filter(conn):
    print("you have selected option 3")

def random(conn):
    print("you have selected option 4")


def main():
    database = "Project.db"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)
        populateTables(conn)

        print("Hello! Welcome to FlixFinder, a movie and show search application based off of Netflix.")

        while True:
            i = choices(conn)
            if i == 0:
                print("Goodbye! I hope you enjoyed our services!")
                break
            elif i >= 5:
                print("Oops, it looks like that number does not correspond to a function above. Please try again.")
                print("++++++++++++++++++++++++++++++++++")         
            elif i == 1:
                search(conn)
            elif i == 2:
                favorites(conn)
            elif i == 3:
                filter(conn)
            elif i == 4:
                random(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()

