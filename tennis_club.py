import sqlite3


class TennisClubDatabase:
    def __init__(self, db_name='tennis_club_db.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def disconnect(self):
        if self.conn:
            try:
                self.conn.commit()
                self.conn.close()
                print("Disconnected from the database")
            except sqlite3.Error as e:
                print(f"Error disconnecting from the database: {e}")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise

    def create_tables(self):
        try:
            self.connect()

            # Create athlete table
            self.execute_query('''
            CREATE TABLE "athlete" (
                "athID"    varchar(6) NOT NULL DEFAULT '',
                "Level"     varchar(6)  DEFAULT '',
                "packID"    varchar(6) DEFAULT '',
                "pack_selection_date"    date DEFAULT '0000-00-00',
                "pack_start_date"    date DEFAULT '0000-00-00',
                "pack_end_date"    date DEFAULT '0000-00-00',
                CONSTRAINT "member_FK" FOREIGN KEY("athID") REFERENCES "member"("memberID") ON DELETE CASCADE ON UPDATE CASCADE,
                PRIMARY KEY("athID"),
                CONSTRAINT "pack_FK" FOREIGN KEY("packID") REFERENCES "package"("packID") ON DELETE CASCADE ON UPDATE CASCADE
            )
            ''')

            # Create athlete-course table
            self.execute_query('''
                CREATE TABLE "athlete_course" (
                    "athID"	varchar(6) DEFAULT '',
                    "courseID"	varchar(6) DEFAULT '',
                    CONSTRAINT "athlete_FK" FOREIGN KEY("athID") REFERENCES "athlete"("athID") ON DELETE CASCADE ON UPDATE CASCADE,
                    CONSTRAINT "course_FK" FOREIGN KEY("courseID") REFERENCES "course"("courseID") ON DELETE CASCADE ON UPDATE CASCADE
                )
                ''')

            # Create reservation table
            self.execute_query('''
            CREATE TABLE "reservation" (
                "reservationID"	NUMERIC NOT NULL DEFAULT NULL,
                "date"	date DEFAULT NULL,
                "time"	time DEFAULT NULL,
                "duration"	time DEFAULT NULL,
                "date_reserve"	date DEFAULT NULL,
                "memberID"	varchar(6) DEFAULT '',
                "courtID"	varchar(6) DEFAULT '',
                "cancellationID"	varchar(6) DEFAULT NULL,
                FOREIGN KEY("cancellationID") REFERENCES "reservation"("reservationID") ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY("memberID") REFERENCES "member"("memberID") ON DELETE CASCADE ON UPDATE CASCADE,
                PRIMARY KEY("reservationID")
            )
            ''')

            # Create coach table
            self.execute_query('''
            CREATE TABLE "coach" (
                "coachID"	varchar(6) NOT NULL DEFAULT '',
                "specialization"	INTEGER DEFAULT 0,
                PRIMARY KEY("coachID"),
                FOREIGN KEY("coachID") REFERENCES "member"("memberID") ON DELETE CASCADE ON UPDATE CASCADE
            )
            ''')

            # Create court table
            self.execute_query('''
            CREATE TABLE "court" (
                "courtID"	varchar(6) NOT NULL,
                "surface"	TEXT,
                PRIMARY KEY("courtID")
            )
            ''')

            # Create equipment table
            self.execute_query('''
            CREATE TABLE "equipment" (
                "eqID"	varchar(6) NOT NULL DEFAULT '',
                "type"	varchar(15) NOT NULL DEFAULT '',
                "quantity"	INTEGER DEFAULT 0,
                "buy_date"	date DEFAULT NULL,
                "athID"	varchar(6) DEFAULT '',
                CONSTRAINT "athlete_FK" FOREIGN KEY("athID") REFERENCES "athlete"("athID") ON DELETE CASCADE ON UPDATE CASCADE,
                PRIMARY KEY("eqID")
            )
            ''')

            # Create lesson table
            self.execute_query('''
            CREATE TABLE "lesson" (
                "lessonID"	varchar(6) NOT NULL DEFAULT '',
                "courseID"  varchar(6) NOT NULL DEFAULT '',
                "date"      date NOT NULL DEFAULT '0000-00-00',
                "time"	time NOT NULL DEFAULT '00:00',
                "duration"	time DEFAULT '00:00',
                "courtID"	varchar(6) NOT NULL DEFAULT '',
                "cancellationID"	varchar(6) DEFAULT '',
                FOREIGN KEY("cancellationID") REFERENCES "lesson"("lessonID") ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT "court_FK" FOREIGN KEY("courtID") REFERENCES "court"("courtID") ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT "course_FK" FOREIGN KEY("courseID") REFERENCES "course"("courseID") ON DELETE CASCADE ON UPDATE CASCADE,
                PRIMARY KEY("lessonID")
            )
            ''')

            #Create course table
            self.execute_query('''
            CREATE TABLE "course" (
                "courseID" varchar(6) NOT NULL DEFAULT '',
                "day"	varchar(10) NOT NULL DEFAULT '',
                "time"	time NOT NULL DEFAULT '00:00',
                "duration"	time DEFAULT '00:00',
                "no_of_participants"	INTEGER DEFAULT 0,
                "coachID"	varchar(6) NOT NULL DEFAULT '',
                CONSTRAINT "coach_FK" FOREIGN KEY("coachID") REFERENCES "coach"("coachID") ON DELETE CASCADE ON UPDATE CASCADE,
                PRIMARY KEY("courseID")
            )
            ''')

            # Create match table
            self.execute_query('''
                        CREATE TABLE "match" (
                            "matchID"	varchar(6) NOT NULL DEFAULT '',
                            "no_of_participants"	INTEGER DEFAULT 0,
                            "date"	date DEFAULT '0000-00-00',
                            "time"	time DEFAULT '00:00',
                            "duration"	time DEFAULT NULL,
                            "courtID"	varchar(6) NOT NULL DEFAULT '',
                            CONSTRAINT "court_FK" FOREIGN KEY("courtID") REFERENCES "court"("courtID") ON DELETE CASCADE ON UPDATE CASCADE,
                            PRIMARY KEY("matchID")
                        )
                        ''')

            # Create match_competitors table
            self.execute_query('''
                        CREATE TABLE "match_competitors" (
                            "athID"	varchar(6) DEFAULT '',
                            "matchID"	varchar(6) DEFAULT '',
                            "winning" boolean DEFAULT '',
                            CONSTRAINT "athlete_FK" FOREIGN KEY("athID") REFERENCES "athlete"("athID") ON DELETE CASCADE ON UPDATE CASCADE,
                            CONSTRAINT "match_FK" FOREIGN KEY("matchID") REFERENCES "match"("matchID") ON DELETE CASCADE ON UPDATE CASCADE
                        )
                        ''')

            # Create member table
            self.execute_query('''
            CREATE TABLE "member" (
                "firstname"	varchar(15) NOT NULL DEFAULT '',
                "lastname"	varchar(15) NOT NULL DEFAULT '',
                "registrationdate"	date DEFAULT NULL,
                "phoneno"	REAL DEFAULT NULL,
                "email"	varchar(20) DEFAULT '',
                "birthdate"	date DEFAULT NULL,
                "address"	varchar(20) DEFAULT '',
                "memberID"	varchar(6) NOT NULL DEFAULT '',
                PRIMARY KEY("memberID")
            )
            ''')

            # Create package table
            self.execute_query('''
            CREATE TABLE "package" (
                "packID"	varchar(6) NOT NULL DEFAULT '',
                "type"	varchar(15) DEFAULT '',
                PRIMARY KEY("packID")
            )
            ''')

            # Create score table
            self.execute_query('''
            CREATE TABLE "score" (
                "matchID"	varchar(6) DEFAULT '',
                "winning"	INTEGER DEFAULT 0,
                "losing"	INTEGER DEFAULT 0,
                FOREIGN KEY("matchID") REFERENCES "match"("matchID") ON DELETE CASCADE ON UPDATE CASCADE
            )
            ''')

            print("Tables created successfully")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            raise
        finally:
            self.disconnect()

try:
    tennis_db = TennisClubDatabase()
    tennis_db.create_tables()
except Exception as e:
    print(f"An error occurred: {e}")