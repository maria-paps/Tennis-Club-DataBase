# Tennis-Club-DataBase

This Tennis Club Database Application is designed to manage and organize data for a tennis club. It consists of five Python files working together to provide functionality for handling lessons, courses, reservations, athletes, and coaches.

Contributors: Papadopoulou Maria, Verykokkou Nektaria


-- Files --
1. tennis_club_data_base.py: This is the main program to run. It calls tennis_club.py, tennis_club_fill.py and edit_db.py. 
To run the application: python tennis_club_data_base.py

2. tennis_club.py: Creates the tables in the database file "tennis_club_db.db" .

3. tennis_club_fill: Inserts data to the database's tables.

4. edit_db.py: Here is the main menu. The user can edit the database's data or get useful information. This program also calls tennis_club_queries.py.

5. tennis_club_queries.py: Holds a menu for possible frequently asked questions such as statistics.


-- Requirements --
sqlite3
tabulate
