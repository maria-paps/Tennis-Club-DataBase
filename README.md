# Tennis-Club-DataBase

This Tennis Club Database Application is designed to manage and organize data for a tennis club. It consists of five Python files working together to provide functionality for handling lessons, courses, reservations, equipment, athletes, and coaches.

Contributors: Papadopoulou Maria, Verykokkou Nektaria


-- Files --
1. tennis_club_data_base.py: This is the main program to run. It calls tennis_club.py, tennis_club_fill.py and edit_db.py. 
To run the application:
```Bash
python tennis_club_data_base.py
```

3. tennis_club.py: Creates the tables in the database file "tennis_club_db.db" .

4. tennis_club_fill: Inserts data to the database's tables.

5. edit_db.py: Here is the main menu. The user can edit the database's data or get useful information. This program also calls tennis_club_queries.py.

6. tennis_club_queries.py: Holds a menu for possible frequently asked questions such as statistics.


-- Requirements --
```Bash
pip install sqlite3
```
```Bash
pip install tabulate
```
