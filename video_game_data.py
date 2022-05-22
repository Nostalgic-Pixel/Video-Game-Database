##################################################################################
# PROGRAM: Video Games Database (sqlite3)
#
# AUTHOR: Joseph Wilson
#
# PURPOSE: The purpose of this software is to insert, keep track, remove, and/or
# display to the user the video games that have been played, completed, and ranked
# from all of the people that have entered into the database.
##################################################################################

import sqlite3


# Connect to the database 
connection = sqlite3.connect('VideoGames.db')
cursor = connection.cursor()


# Create table (if it does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS players (name TEXT, title TEXT, rating REAL)")


# Create def for get_name so that the player can enter in their ID number in the 
# database.
def get_name(cursor):
    cursor.execute("SELECT name FROM players")
    results = cursor.fetchall()

    # If there are no names in the database, display the no names message.
    if len(results) == 0:
        print("No names in the database")
        return None

    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")

    # Declare variable for choice
    choice = 0

    # While choice is less than 1 or is less than the length of the results, prompt
    # the user for their Player ID.
    while choice < 1 or choice > len(results):
        choice = int(input("Name ID#: "))
    return results[choice - 1][0]


choice = None

while choice != "5":

    print("1) Display Players")
    print("2) Add Player")
    print("3) Update Player Rating ")
    print("4) Delete Player")
    print("5) Quit")

    print()

    choice = input()

    # DISPLAY PLAYERS
    if choice == "1":
        cursor.execute("SELECT * FROM players ORDER BY rating DESC")
        print("{:>10} {:>10} {:>10}".format("Name", "Title", "Rating"))
        for record in cursor.fetchall():
            print("{:>10} {:>10} {:>10} ".format(record[0], record[1], record[2]))

    # ADD NEW PLAYER
    elif choice == "2":
        try:
            name = input("Your Name: ")
            title = input("Game Title: ")
            rating = input("Rating from 1-10: ")
            profile = (name, title, rating)
            cursor.execute("INSERT INTO players VALUES (?,?,?)", profile)
            connection.commit() 
        except ValueError:
            print("Invalid profile!")

    # UPDATE PLAYER RATING
    elif choice == "3":
        try:
            name = input("Name: ")
            rating = input("Rating: ")
            profile = (rating, name) # The order is important!

            cursor.execute("UPDATE players SET rating = ? WHERE name = ?", profile)
            connection.commit()

            if cursor.rowcount == 0:
                print("Invalid name!")

        except ValueError:
            print("Invalid rating!")

    # DELETE PLAYER
    elif choice == "4":

        name = get_name(cursor)

        if name == None:
            continue
        profile = (name, )
        cursor.execute("DELETE FROM players WHERE name = ?", profile)

        connection.commit()

        print()

# Close the database connection before exiting
connection.close()


##################################################################################
# NOTES: 
# Try using SQLite and hook up VS Code (python) to communicate with it. Make sure 
# that you download the SQL library on VS Code so that python can know how to use 
# SQL commands.
#
# You don't need the SQL file to be on Github, but just make sure that the python 
# file has some of the functions to do them.
#
# When using SQLite Studio, make sure that you are using the right path in order for 
# the software to run the correct .db file when running it.
#
# ex: 
##################################################################################
