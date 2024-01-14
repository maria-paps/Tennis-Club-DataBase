import sqlite3
print("\tFile: tennis_club.py")
try:
    from tennis_club import TennisClubDatabase
except:
    print("Database is already created")
from tennis_club_fill import fill_database
from edit_db import main

try:
    print("\tFile: tennis_club_fill.py")
    try:
        fill_database()
    except:
        print("Data have already been uploaded")
    print("\tFile: edit_db.py")
    print("\n\n---TENNIS CLUB APP---\n")
    main()

except Exception as e:
    print("An error occured {e}")

