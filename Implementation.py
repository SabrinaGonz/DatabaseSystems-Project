import sqlite3
from sqlite3 import Error
import random

def openConnection(dbfile):

    conn = None
    try:
        conn = sqlite3.connect(dbfile)
    except Error as e:
        print(e)

    return conn 

def closeConnection(conn, dbfile):

    try:
        conn.close()
    except Error as e:
        print(e)




def dropTables(conn):

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

        sql = """drop view if exists movies"""
        conn.execute(sql)

        sql = """drop view if exists shows"""
        conn.execute(sql)

        conn.commit()
    except Error as e:
        print(e)




def createTables(conn):

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
                f_sid            varchar(10) not null,
                f_title          char(117))"""
        conn.execute(sql)

        conn.commit()
    except Error as e:
        conn.rollback()
        print(e)




def populateTables(conn):

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
    except Error as e:
        print(e)




def choices(conn):
    print("Enter the number of the option that you wish to use: ")
    print("     0. Exit the program.")
    print("     1. Search for a specific title.")
    print("     2. View Favorites list.")
    print("     3. Filter through our titles to be given a show recommendation.")
    print("     4. Receive a random title recommendation.")
    selection = int(input())
    return selection

def favorites(conn):
    print("\nHere is your current Favorite list")

    sql = "select * from Favorite"
    cur = conn.cursor()
    cur.execute(sql)
    l = '{:>10} {:>10}'.format("Show ID", "Title")
    print(l + "\n")

    rows = cur.fetchall()
    for row in rows:
        l = '{:>10} {:>10}'.format(row[0], row[1])
        print(l)
    print("\n")

def addfavorites(conn):
    s = input("Please enter the Show ID of the title you wish to add to your Favorites list: ")
    try:
        sql = """insert into Favorite(f_sid, f_title)
                select t_sid, t_title
                from Titles 
                where t_sid = ?"""
        conn.execute(sql, (s,))
        conn.commit()
        favorites(conn)
    except Error as e:
        print("Sorry, we were not able to add that show into your Favorites list.\nPlease double check that you also included 's' into the Show ID.\n")
        addfavorites(conn)

def search(conn):
    cur = conn.cursor()
    s = '%'
    s += input("Please enter what title you are searching for: ")
    s += '%'
    with conn:
        sql = """select t_sid, t_title
                from Titles
                where t_title like ?"""
        cur.execute(sql, (s,))

        l = '{:>10} {:>10}'.format("Show ID", "Title")
        print(l + "\n")

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>10}'.format(row[0], row[1])
            print(l)
    print("If the title you are looking for does not appear, it is not available on Netflix.\n")

    fav = input("If you would like to add a title to your favorites, please enter 1 or 0 if not: ")
    if fav == "1":
        addfavorites(conn)
    
    print("Okay, returning you to the main menu.\n\n")
    

def randomshow(conn):
    print("Here is a random show in Netflix: \n")
    r = "s"
    r += str(random.randint(1, 8807))
    cur = conn.cursor()
    sql = """select t_sid, t_title, t_type
            from Titles
            where ? = t_sid"""
    cur.execute(sql, (r,))

    l = '{:>10} {:>10} {:>10}'.format("Show ID", "Title", "Show Type")
    print(l + "\n")

    rows = cur.fetchall()
    for row in rows:
        l = '{:>10} {:>10} {:>10}'.format(row[0], row[1], row [2])
        print(l + "\n")
    

def typefilter(conn):
    print("Would you like: ")
    print("     1. Movies")
    print("     2. TV Shows")
    i = int(input())
    return i

def morefilter(conn):
    m = int(input("If you would like to filter more, please enter 1 or 0 if not: "))
    return m
    
def genrefilter(conn):
    print("Would you like: ")
    print("     1. Action & Adventure")
    print("     2. Anime")
    print("     3. Children & Family")
    print("     4. Comedies")
    print("     5. Horror")
    print("     6. Romantic")
    print("     7. Thrillers")
    g = int(input())
    return g

def filter(conn):
    sql = """drop view if exists movies"""
    conn.execute(sql)
    sql = """drop view if exists shows"""
    conn.execute(sql)
    sql = """drop view if exists actionadventuremovies"""
    conn.execute(sql)
    sql = """drop view if exists actionadventureshows"""
    conn.execute(sql)
    conn.commit()

    cur = conn.cursor()
    t = typefilter(conn)
    if t == 1:
        sql = """create view movies(sid, title, genre, release, rating) as 
                select n_sid, n_title, n_listed, n_release, n_rating
                from Netflix
                where n_type = 'Movie'"""
        cur.execute(sql)
        conn.commit()
        sql = "select * from movies"
        cur.execute(sql)

        l = '{:>10} {:>20} {:>30} {:>20} {:>20}'.format("Show ID", "Title", "Genre", "Release Date", "Rating")
        print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>20} {:>30} {:>20} {:>20}'.format(row[0], row[1], row[2], row[3], row[4])
            print(l)
    else:
        sql = """create view shows(sid, title, genre, release, rating) as 
                select n_sid, n_title, n_listed, n_release, n_rating
                from Netflix
                where n_type = 'TV Show'"""
        cur.execute(sql)
        conn.commit()
        sql = "select * from shows"
        cur.execute(sql)
        l = '{:>10} {:>20} {:>30} {:>20} {:>20}'.format("Show ID", "Title", "Genre", "Release Date", "Rating")
        print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:>20} {:>30} {:>20} {:>20}'.format(row[0], row[1], row[2], row[3], row[4])
            print(l)

    # print()
    # g = genrefilter(conn)
    # if g == 1 & t == 1:             
    #     sql = """create view actionadventuremovies(sid, title, genre, release, rating) as 
    #             select n_sid, n_title, n_listed, n_release, n_rating
    #             from Netflix
    #             where n_listed = 'Action & Adventure'
    #             and n_type = 'Movie'"""
    #     cur.execute(sql)
    #     conn.commit()
    #     sql = "select * from actionadventuremovies"
    #     cur.execute(sql)
        
    #     l = '{:>10} {:>20} {:>30} {:>20} {:>20}'.format("Show ID", "Title", "Genre", "Release Date", "Rating")
    #     print(l)

    #     rows = cur.fetchall()
    #     for row in rows:
    #         l = '{:>10} {:>20} {:>30} {:>20} {:>20}'.format(row[0], row[1], row[2], row[3], row[4])
    #         print(l)
            
    # elif g == 1 & t == 2:
    #     sql = """create view actionadventureshows(sid, title, genre, release, rating) as 
    #             select n_sid, n_title, n_listed, n_release, n_rating
    #             from Netflix
    #             where n_listed like '%Action%'
    #             and n_type = 'TV Show'"""
    #     cur.execute(sql)
    #     conn.commit()
    #     sql = "select * from actionadventureshows"
    #     cur.execute(sql)
        
    #     l = '{:>10} {:>20} {:>30} {:>20} {:>20}'.format("Show ID", "Title", "Genre", "Release Date", "Rating")
    #     print(l)

    #     rows = cur.fetchall()
    #     for row in rows:
    #         l = '{:>10} {:>20} {:>30} {:>20} {:>20}'.format(row[0], row[1], row[2], row[3], row[4])
    #         print(l)

    
        
            





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
                randomshow(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()

