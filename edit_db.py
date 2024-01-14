import sqlite3
import re
from datetime import datetime, timedelta
import time
import random
from tabulate import tabulate
from datetime import date
import calendar
import tennis_club_queries

today = date.today()

with sqlite3.connect("tennis_club_db.db") as conn:
    cur = conn.cursor()


    def increase(id_):
        id_ = str(id_[0])
        idnum = str(int(id_[1:]) + 1).zfill(len(id_[1:]))
        id_ = f"{id_[0]}{idnum}"

        return id_


    def new_member(m):
        if m == 'A':
            print("--Athlete's details-- \n\n")
        if m == 'C':
            print("--Coach's details-- \n\n")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        registration_date = today
        # Check for valid phone number
        while True:
            phonenumber = input("Tel: ")
            if len(phonenumber) == 10 and phonenumber.isdigit():
                break
            else:
                print("\nERROR: Please enter a valid 10-digit phone number.\n")
        # Check for valid email address
        while True:
            email = input("Email: ")
            if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                break
            else:
                print("\nERROR: Please enter a valid email address.\n")
        # Check for valid birth date
        while True:
            birthdate_str = input("Birthdate (YYYY-MM-DD): ")
            try:
                birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
                age = today.year - birthdate.year
                if birthdate.date() <= today:
                    break
                else:
                    print("\nERROR: Birthdate cannot be in the future.\n")
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")
        address = input("Address: ")
        memberid = ''
        pack_end = ''
        packid = ''

        if m == 'A':
            if age > 14:
                # Check for valid level
                valid_levels = {"beginner", "intermediate", "advanced intermediate", "advanced", "professional", "special needs"}
                while True:
                    level = input("Level (beginner/intermediate/advanced intermediate/advanced/professional/special needs): ").lower()
                    if level in valid_levels:
                        break
                    else:
                        print("\nERROR: Please enter a valid athlete level.")
            else:
                level = 'junior'

            pack_date = today

            # Check for valid package
            valid_packs = {"day", "month", "year"}
            while True:
                packtype = input("Type of package (day/month/year): ").lower()
                if packtype in valid_packs:
                    break
                else:
                    print("\nERROR: Please enter a valid package. \n")

            # Check for valid start day
            while True:
                pack_start = input("Package starting date (YYYY-MM-DD): ")
                try:
                    pack_start = datetime.strptime(pack_start, "%Y-%m-%d")
                    break
                except ValueError:
                    print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

            if packtype == "day":
                pack_end = pack_start + timedelta(days=1)
                packid = "P001"
            if packtype == "month":
                pack_end = pack_start + timedelta(days=30)
                packid = "P002"
            if packtype == "year":
                pack_end = pack_start + timedelta(days=365)
                packid = "P003"

            cur.execute("SELECT max(athID) FROM athlete;")
            memberid = cur.fetchone()
            memberid = increase(memberid)

            if packtype == "day" or packtype == "month" or packtype == "year":
                print("\nAvailable courses: \n")

            conn.execute(
                '''INSERT INTO athlete (athID,Level,packID,pack_selection_date, pack_start_date, pack_end_date) VALUES(?,?,?,?,?,?)''',
                (memberid, level, packid, pack_date, pack_start.strftime("%Y-%m-%d"), pack_end.strftime("%Y-%m-%d")))
            athlete_course(level, memberid)

        if m == 'C':
            # Check for valid coach specialization
            valid_coach_specializations = {"junior", "beginners", "advanced", "high-performance", "special needs"}
            while True:
                specialize = input("Specialization (junior/beginners/advanced/high-performance/special needs):").lower()
                if specialize in valid_coach_specializations:
                    break
                else:
                    print("\nERROR: Please enter a valid coach specialization. \n")

            cur.execute("SELECT max(coachID) FROM coach;")
            memberid = cur.fetchone()
            memberid = increase(memberid)
            conn.execute(
                '''INSERT INTO coach (coachID,specialization) VALUES(?,?)''', (memberid, specialize))

        conn.execute(
            '''INSERT INTO member (firstname,lastname,registrationdate,email,birthdate,phoneno,address,memberID)
            VALUES(?,?,?,?,?,?,?,?)''',
            (first_name, last_name, registration_date, email, birthdate.strftime("%Y-%m-%d"), phonenumber, address,
             memberid))

        conn.commit()
        print("\nNew member '", first_name, " ", last_name, "' with ID ", memberid, " inserted successfully.\n")

        time.sleep(3)
        main()


    def delete_member():
        # Check format for member ID
        while True:
            memberid = input("Enter Member's ID to delete: ").upper()

            if re.match(r'^[AC]\d{5}$', memberid):
                break
            else:
                print("\nERROR: Member ID should start with 'A' or 'C' followed by 5 digits.\n")

        conn.execute("PRAGMA foreign_keys = ON")

        cur.execute("SELECT firstname, lastname FROM member WHERE memberID = '" + memberid + "';")
        name = cur.fetchmany(2)
        name = name[0]
        first_name = name[0]
        last_name = name[1]

        if name == None:
            print("ERROR: This member does not exist.")
        else:
            conn.execute("DELETE FROM member WHERE memberID = '" + memberid + "';")
            conn.commit()
            print("\nMember '", first_name, " ", last_name, "' with ID ", memberid, " deleted successfully.\n")
        time.sleep(3)
        main()


    def edit_details(m):
        # Check format for member ID
        while True:
            memberid = input("Member's ID: ").upper()

            if re.match(r'^[AC]\d{5}$', memberid):
                break
            else:
                print("\nERROR: Member ID should start with 'A' or 'C' followed by 5 digits.\n")

        cur.execute("SELECT firstname, lastname FROM member WHERE memberID = '" + memberid + "';")
        name = cur.fetchmany(2)
        name = name[0]
        first_name = name[0]
        last_name = name[1]

        print("\n1-Update telephone number\n2-Update email")
        if m == 'A':
            print("3-Update level\n4-Update package")
        if m == 'C':
            print("3-Update specialization")
        mode = input("\nSelect: ")

        if mode == '1':
            # Check phone number format
            while True:
                newtel = input("\nNew telephone number: ")
                if len(newtel) == 10 and newtel.isdigit():
                    break
                else:
                    print("\nERROR: Please enter a valid 10-digit phone number.\n")

            conn.execute("UPDATE member SET phoneno = '" + newtel + "' WHERE memberID = '" + memberid + "';")
        if mode == '2':
            # Check email format
            while True:
                newemail = input("\nNew email address: ")
                if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", newemail):
                    break
                else:
                    print("\nERROR: Please enter a valid email address.\n")

            conn.execute("UPDATE member SET email = '" + newemail + "' WHERE memberID = '" + memberid + "';")
        if mode == '3' and m == 'A':
            # Check for correct level type
            valid_levels = {"junior", "beginner", "advanced intermediate", "advanced", "professional"}
            while True:
                newlevel = input("\nNew level: ").lower()
                if newlevel in valid_levels:
                    break
                else:
                    print(
                        "\nERROR: Please enter a valid athlete level (junior/beginner/intermediate/advanced intermediate/advanced/professional).")

            conn.execute("UPDATE athlete SET level = '" + newlevel + "' WHERE athID = '" + memberid + "' ;")
        if mode == '3' and m == 'C':
            newspec = input("\nNew specialization: ")
            conn.execute("UPDATE coach SET specialization = '" + newspec + "' WHERE coachID = '" + memberid + "' ;")
        if mode == '4' and m == 'A':
            # Check for valid package type
            valid_packs = {"day", "month", "year"}
            while True:
                newpack = input("Select package (day/month/year): ").lower()
                if newpack in valid_packs:
                    break
                else:
                    print("\nERROR: Please enter a valid package. \n")
            # Check for valid date format
            while True:
                pack_start = input("\nPackage starting date (YYYY-MM-DD): ")
                try:
                    pack_start = datetime.strptime(pack_start, "%Y-%m-%d")
                    break
                except ValueError:
                    print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

            pack_sel_date = str(today)
            packid = ''
            pack_end = ''
            if newpack == "day":
                pack_end = pack_start + timedelta(days=1)
                packid = "P001"
            if newpack == "month":
                pack_end = pack_start + timedelta(days=30)
                packid = "P002"
            if newpack == "year":
                pack_end = pack_start + timedelta(days=365)
                packid = "P003"
            conn.execute(
                "UPDATE athlete SET packID = '" + packid + "' AND pack_selection_date = '" + pack_sel_date + "' AND "
                                                                                                             "pack_start_date = '" + str(
                    pack_start) + "' AND pack_end_date = '" + str(pack_end) + "' "
                                                                              "WHERE athID = '" + memberid + "' ;")
        conn.commit()
        print("Change for '", first_name, " ", last_name, "' applied successfully.")

        time.sleep(3)
        main()


    def new(mode, member):
        # Check date format
        while True:
            scheduled_date = input("Date (YYYY-MM-DD): ")
            try:
                scheduled_date = datetime.strptime(scheduled_date, "%Y-%m-%d")
                if scheduled_date.date() >= today:
                    break
                else:
                    print("\nERROR: Reservations cannot be in the past.\n")
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        # Check time format
        while True:
            time_r = input("Time (HH:MM): ")
            try:
                datetime.strptime(time_r, "%H:%M")
                break
            except ValueError:
                print("\nERROR: Invalid time format. Please enter in HH:MM.\n")

        # Check for valid duration
        while True:
            duration = input("Duration (hours): ")
            try:
                duration_float = float(duration)
                if 0 <= duration_float <= 10 and duration_float % 0.5 == 0:
                    break
                else:
                    print("\nERROR: Please enter a valid duration (Example: 1.5 hours).\n")
            except ValueError:
                print("\nERROR: Please enter a valid numeric duration.\n")

        while True:
            # Check for correct court type
            valid_courts = {"clay", "hard", "grass"}
            while True:
                surface = input("Court surface (clay/grass/hard): ")
                if surface in valid_courts:
                    break
                else:
                    print("\nERROR: Please enter a valid court surface.")

            courtid = ''
            cur.execute("SELECT courtID FROM reservation WHERE (date = '" + scheduled_date.strftime(
                "%Y-%m-%d") + "' AND time = '" + time_r + "') OR (date "
                                                          "= '" + scheduled_date.strftime(
                "%Y-%m-%d") + "' AND time > '" + time_r + "' AND  time <= '" + time_r + "' + " + duration + ") OR (date = "
                                                                                                            "'" + scheduled_date.strftime(
                "%Y-%m-%d") + "' AND time < '" + time_r + "' AND time + duration >= '" + time_r + "') UNION SELECT courtID "
                                                                                                  "FROM lesson WHERE (date = '" + scheduled_date.strftime(
                "%Y-%m-%d") + "' AND time = '" + time_r + "') OR (date = '" + scheduled_date.strftime("%Y-%m-%d") + "' "
                                                                                                                    "AND time > '" + time_r + "' AND  time <= '" + time_r + "' + " + duration + ") OR (date = '" + scheduled_date.strftime(
                "%Y-%m-%d") + "' AND "
                              "time < '" + time_r + "' AND time + duration >= '" + time_r + "') UNION SELECT courtID FROM match WHERE (date = '" + scheduled_date.strftime(
                "%Y-%m-%d") + "' "
                              "AND time = '" + time_r + "') OR (date = '" + scheduled_date.strftime(
                "%Y-%m-%d") + "' AND time > '" + time_r + "' AND  time <= '" + time_r + "' "
                                                                                        "+ " + duration + ") OR (date = '" + scheduled_date.strftime(
                "%Y-%m-%d") + "' AND time < '" + time_r + "' AND time + duration >= '" + time_r + "')")

            occupied = cur.fetchall()
            occupied_courts = [court[0] for court in occupied]
            available_courts = ''
            if surface == "clay":
                available_courts = ["CR01", "CR02", "CR03"]
            elif surface == "grass":
                available_courts = ["CR04", "CR05"]
            elif surface == "hard":
                available_courts = ["CR06", "CR07"]

            available_courts = [court for court in available_courts if court not in occupied_courts]

            if available_courts:
                courtid = random.choice(available_courts)
                print("Selected court ID:", courtid)
                break
            else:
                print("\nNo available courts for the given surface and time. Choose a different surface:")

        if mode == 'reservation' or mode == 'rescheduled_reservation':

            date_of_r = today
            memberid = member
            sel = "Y"
            first_name = ''
            last_name = ''

            cur.execute("SELECT max(reservationID) FROM reservation;")
            reservationid = cur.fetchone()
            if mode == 'rescheduled_reservation':
                reservationid = reservationid[0]
            if mode == 'reservation':
                reservationid = increase(reservationid)

                while True:
                    sel = input("Member? (Y/N): ")
                    if sel.upper() == 'Y' or sel.upper() == 'N':
                        break
                    else:
                        print("\nERROR: Please type 'Y' or 'N'.\n")

            if sel == "N" or sel == "n":
                first_name = input("First name: ")
                last_name = input("Last name: ")
                # Check for valid phone number
                while True:
                    phonenumber = input("Tel.: ")
                    if len(phonenumber) == 10 and phonenumber.isdigit():
                        break
                    else:
                        print("\nERROR: Please enter a valid 10-digit phone number.\n")

                memberid = reservationid
                conn.execute(
                    '''INSERT INTO member (firstname,lastname,registrationdate, phoneno, memberID)
                    VALUES(?,?,?,?,?)''',
                    (first_name, last_name, date_of_r, phonenumber, memberid))
            if sel == "Y" or sel == "y":
                if mode == 'reservation':

                    # Check format for member ID
                    while True:
                        memberid = input("ID: ").upper()

                        if re.match(r'^[AC]\d{5}$', memberid):
                            break
                        else:
                            print("\nERROR: Member ID should start with 'A' or 'C' followed by 5 digits.\n")

                cur.execute("SELECT firstname, lastname FROM member WHERE memberID = '" + memberid + "';")
                name = cur.fetchmany(2)
                name = name[0]
                first_name = name[0]
                last_name = name[1]

            if mode == 'reservation':
                conn.execute(
                    '''INSERT INTO reservation (reservationID, date, time, duration, date_reserve, memberID,courtID) VALUES(?,?,?,?,?,?,?)''',
                    (
                    reservationid, scheduled_date.strftime("%Y-%m-%d"), time_r, duration, date_of_r, memberid, courtid))
            if mode == 'rescheduled_reservation':
                conn.execute(
                    '''UPDATE reservation SET date=?, time = ?, duration = ? , date_reserve = ?, courtID = ?
                            WHERE reservationID = ? ;''',
                    (scheduled_date.strftime("%Y-%m-%d"), time_r, duration, date_of_r, courtid, reservationid))
            print("Reservation name: ", first_name, " ", last_name, ", reservation ID: ", reservationid)

        if mode == 'lesson' or mode == 'rescheduled_lesson':

            lessonid = member
            courseid = ''

            if mode == 'rescheduled_lesson':
                cur.execute("SELECT cancellationID FROM lesson WHERE lessonID = '" + lessonid + "';")
                cancellationid = cur.fetchone()[0]
                cur.execute("SELECT courseID FROM lesson WHERE lessonID = '" + cancellationid + "';")
                courseid = cur.fetchone()[0]
                conn.execute(
                    "UPDATE lesson SET date = '" + scheduled_date.strftime("%Y-%m-%d") + "', time = '" + time_r + "', "
                                                                                                                  "courseID = '" + courseid + "', duration = '" + duration + "', courtID = '" + courtid + "' WHERE lessonID = '" + lessonid + "';")

            if mode == 'lesson':
                while True:
                    courseid = input("Course ID: ")
                    if re.match(r'^[A-Z]\d{1,2}_\d$', courseid):
                        cur.execute("SELECT courseID FROM course WHERE courseID = '" + courseid + "' LIMIT 1")
                        courseid = cur.fetchone()
                        if courseid == None:
                            print("This course ID does not exist.\n")
                            continue
                        courseid = courseid[0]
                        break
                    else:
                        print(
                            "\nERROR: Course ID should have the pattern 'Lm_n' where 'L' is the first letter if the \n"
                            "course's level (Junior, Special needs, Beginner, Advanced, Professional), \n'm' is the "
                            "number of the class and 'n' is '1' or '2' representing the first or the second lesson of the week.\n")

                cur.execute("SELECT max(lessonID) FROM lesson;")
                lessonid = cur.fetchone()
                lessonid = increase(lessonid)

                conn.execute(
                    '''INSERT INTO lesson VALUES(?,?,?,?,?,?,?)''',
                    (lessonid, courseid, scheduled_date.strftime("%Y-%m-%d"), time_r, duration, courtid, None))

        if mode == 'match':
            cur.execute("SELECT max(matchID) FROM match;")
            matchid = cur.fetchone()
            matchid = increase(matchid)
            athletes = []

            while True:
                ath1 = input("Athlete's no.1 ID:")
                if re.match(r'^[AC]\d{5}$', ath1):
                    if check_if_athlete_exists(ath1):
                        break
                    print("This ID does not exist")
                    continue
                print("Invalid ID for athlete. ID should start with 'A' followed by 5 digits")

            while True:
                ath2 = input("Athlete's no.2 ID:")
                if re.match(r'^[AC]\d{5}$', ath2):
                    if check_if_athlete_exists(ath2):
                        break
                    print("This ID does not exist")
                    continue
                print("Invalid ID for athlete. ID should start with 'A' followed by 5 digits")

            while ath1 == ath2:
                ath2 = input("This athlete is already registered.\nAthlete's no.2 ID: ")

            while True:
                sel = input("Add 2 more players? (Y/N): ")
                if sel.upper() == 'N':
                    athletes = [ath1, ath2]
                    break
                elif sel.upper() == 'Y':

                    while True:
                        ath3 = input("Athlete's no.3 ID:")
                        if re.match(r'^[AC]\d{5}$', ath3):
                            if check_if_athlete_exists(ath3):
                                break
                            print("This ID does not exist")
                            continue
                        print("Invalid ID for athlete. ID should start with 'A' followed by 5 digits")

                    while ath3 == ath1 or ath3 == ath2:
                        ath3 = input("This athlete is already registered.\nAthlete's no.3 ID: ")

                    while True:
                        ath4 = input("Athlete's no.4 ID:")
                        if re.match(r'^[AC]\d{5}$', ath4):
                            if check_if_athlete_exists(ath4):
                                break
                            print("This ID does not exist")
                            continue
                        print("Invalid ID for athlete. ID should start with 'A' followed by 5 digits")

                    while ath4 == ath3 or ath4 == ath2 or ath4 == ath1:
                        ath4 = input("This athlete is already registered.\nAthlete's no.4 ID: ")

                    athletes = [ath1, ath2, ath3, ath4]
                    break

                else:
                    print("\nERROR: Please type 'Y' or 'N'.\n")

            participants = len(athletes)
            conn.execute(
                '''INSERT INTO match (matchID, no_of_participants, date, time, courtID) VALUES(?,?,?,?,?)''',
                (matchid, participants, scheduled_date.strftime("%Y-%m-%d"), time_r, courtid))
            if participants == '4':
                conn.execute(
                    '''INSERT INTO match (matchID, no_of_participants, date, time, courtID) VALUES(?,?,?,?,?)''',
                    (matchid, participants, scheduled_date.strftime("%Y-%m-%d"), time_r, courtid))
            conn.execute("INSERT INTO score (matchID) VALUES('" + matchid + "');")
            for i in athletes:
                conn.execute('''INSERT INTO match_competitors VALUES(?,?,?)''', (i, matchid, ''))

            print("Match: ", matchid, "\nTeam 1: ", athletes[:int(len(athletes) / 2)], "\nTeam 2: ",
                  athletes[int(len(athletes) / 2):])

        conn.commit()
        print("\nNew ", mode, " inserted successfully.\n")
        time.sleep(3)
        main()


    def cancel_reservation():
        # Check format for member ID
        while True:
            memberid = input("Member's ID: ").upper()

            if re.match(r'^[ACR]\d{5}$', memberid):
                break
            else:
                print("\nERROR: Member ID should start with 'A' or 'C' followed by 5 digits.\n")

        date_of_c = today
        cur.execute("SELECT firstname, lastname FROM member WHERE memberID = '" + memberid + "';")
        name = cur.fetchmany(2)
        name = name[0]
        first_name = name[0]
        last_name = name[1]

        cur.execute("SELECT R.date FROM reservation AS R "
                    "LEFT JOIN reservation AS C ON R.reservationID = C.cancellationID WHERE R.memberID = '" + memberid + "' "
                                                                                                                         "AND R.date IS NOT NULL AND C.reservationID IS NULL ;")
        reservations = cur.fetchall()

        if name == None or reservations == []:
            print("ERROR: This member does not exist or does not have a reservation.")
        else:
            print("\nReservations: ")
            for reservation in reservations:
                print(reservation[0])
            # Check date format
            while True:
                sel = input("Which reservation would you like to cancel? (YYYY-MM-DD)")
                try:
                    sel = datetime.strptime(sel, "%Y-%m-%d")
                    break
                except ValueError:
                    print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

            cur.execute(
                "SELECT reservationID FROM reservation WHERE memberID = '" + memberid + "' AND date = '" + sel.strftime(
                    "%Y-%m-%d") + "';")
            cancellationid = cur.fetchone()
            cancellationid = cancellationid[0]

            cur.execute("SELECT max(reservationID) FROM reservation;")
            reservationid = cur.fetchone()
            reservationid = increase(reservationid)

            conn.execute(
                '''INSERT INTO reservation (reservationID, date_reserve, memberID, cancellationID) VALUES(?,?,?,?)''',
                (reservationid, date_of_c, memberid, cancellationid))

            print("\nReservation ", cancellationid, " for ", first_name, " ", last_name, " cancelled successfully. ")

            while True:
                sel = input("Would you like to reschedule? (Y/N): ")
                if sel.upper() == 'Y' or sel.upper() == 'N':
                    break
                else:
                    print("\nERROR: Please type 'Y' or 'N'.\n")

            if sel == 'Y' or sel == 'y':
                conn.commit()
                new('rescheduled_reservation', memberid)

        conn.commit()
        time.sleep(3)
        main()


    def cancel_lesson():
        while True:
            courseid = input("Course ID to cancel lesson: ")
            if re.match(r'^[A-Z]\d{1,2}_\d$', courseid):
                cur.execute("SELECT courseID FROM course WHERE courseID = '" + courseid + "' LIMIT 1")
                courseid = cur.fetchone()
                if courseid == None:
                    print("This course ID does not exist.\n")
                    continue
                courseid = courseid[0]
                break
            else:
                print("\nERROR: Course ID should have the pattern 'Lm_n' where 'L' is the first letter if the \n"
                      "course's level (Junior, Special needs, Beginner, Advanced, Professional), \n'm' is the "
                      "number of the class and 'n' is '1' or '2' representing the first or the second lesson of the week.\n")

        cur.execute("SELECT L.lessonID, L.courseID, L.date, L.time, L.duration, L.courtID "
                    "FROM lesson AS L LEFT JOIN lesson AS C ON L.lessonID = C.cancellationID "
                    "WHERE L.courseID = '" + courseid + "' AND C.lessonID IS NULL ORDER BY L.date;")
        lessons = cur.fetchall()

        columns = [description[0] for description in cur.description]
        print(tabulate(lessons, headers=columns, tablefmt="pretty"))
        #print("\t" + str(lessons) + "\t\n")

        # Check format for lesson ID
        while True:
            lessonid = input("Lesson's ID to cancel: ").upper()

            if re.match(r'^[L]\d{3}$', lessonid):
                cur.execute("SELECT * FROM lesson WHERE lessonID = '" + lessonid + "'")
                lesson = cur.fetchall()
                lesson = lesson[0]
                lessonid = lesson[0]
                if lessonid == None:
                    print("ERROR: This lesson does not exist.")
                    continue
                else:
                    break
            else:
                print("\nERROR: Lesson ID should start with 'L' followed by 3 digits.\n")

        l_date = lesson[2]
        l_time = lesson[3]
        l_court = lesson[5]

        cancellationid = lessonid

        cur.execute("SELECT max(lessonID) FROM lesson;")
        lessonid = cur.fetchone()
        lessonid = increase(lessonid)

        conn.execute(
            '''INSERT INTO lesson (lessonID, cancellationID) VALUES(?,?)''',
            (lessonid, cancellationid))

        print("\nLesson ", cancellationid, " for ", l_date, " ", l_time, " in court ", l_court,
              " cancelled successfully. ")
        while True:
            sel = input("Would you like to reschedule? (Y/N): ")
            if sel.upper() == 'Y' or sel.upper() == 'N':
                break
            else:
                print("\nERROR: Please type 'Y' or 'N'.\n")

        if sel == 'Y' or sel == 'y':
            conn.commit()
            new('rescheduled_lesson', lessonid)

        conn.commit()
        time.sleep(3)
        main()


    def cancel_match():
        # Check format for match ID
        while True:
            matchid = input("Match's ID: ").upper()

            if re.match(r'^[M]\d{3}$', matchid):
                break
            else:
                print("\nERROR: Match ID should start with 'M' followed by 3 digits.\n")

        cur.execute("SELECT * FROM match WHERE matchID = '" + matchid + "'")
        match = cur.fetchall()
        match = match[0]
        matchid = match[0]
        m_date = match[2]
        m_time = match[3]
        m_court = match[5]

        if matchid == None:
            print("ERROR: This match does not exist.")
        else:
            conn.execute(
                "DELETE FROM match WHERE matchID = '" + matchid + "' ; ")
            conn.execute(
                "DELETE FROM match_competitors WHERE matchID = '" + matchid + "' ; ")

            print("\nMatch ", matchid, " for ", m_date, " ", m_time, " in court ", m_court,
                  " cancelled successfully. ")

        conn.commit()
        time.sleep(3)
        main()


    def reservation_list():
        print("\nSelect dates to view reservation-list:\n")

        while True:
            start = input("From (YYYY-MM-DD):")
            try:
                start = datetime.strptime(start, "%Y-%m-%d")
                break
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        while True:
            end = input("Until (YYYY-MM-DD): ")
            try:
                end = datetime.strptime(end, "%Y-%m-%d")
                break
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        cur.execute("SELECT R.reservationID, R.date, R.time, R.duration, R.date_reserve, R.memberID, R.courtID "
                    "FROM reservation AS R LEFT JOIN reservation AS C ON R.reservationID = C.cancellationID "
                    "WHERE R.date BETWEEN '" + start.strftime("%Y-%m-%d") + "' AND '" + end.strftime(
            "%Y-%m-%d") + "' AND C.reservationID IS NULL ORDER BY R.date;")
        reservations = cur.fetchall()

        columns = [description[0] for description in cur.description]
        print(tabulate(reservations, headers=columns, tablefmt="pretty"))
        #print("\t" + str(reservations) + "\t\n")

        conn.commit()
        time.sleep(3)
        main()


    def lesson_list():
        print("\nSelect dates to view scheduled lessons:\n")

        while True:
            start = input("From (YYYY-MM-DD):")
            try:
                start = datetime.strptime(start, "%Y-%m-%d")
                break
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        while True:
            end = input("Until (YYYY-MM-DD): ")
            try:
                end = datetime.strptime(end, "%Y-%m-%d")
                break
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        cur.execute("SELECT L.lessonID, L.courseID, L.date, L.time, L.duration, L.courtID "
                    "FROM lesson AS L LEFT JOIN lesson AS C ON L.lessonID = C.cancellationID "
                    "WHERE L.date BETWEEN '" + start.strftime("%Y-%m-%d") + "' AND '" + end.strftime(
            "%Y-%m-%d") + "' AND C.lessonID IS NULL ORDER BY L.date;")
        lessons = cur.fetchall()

        columns = [description[0] for description in cur.description]
        print(tabulate(lessons, headers=columns, tablefmt="pretty"))
        #print("\t" + str(lessons) + "\t\n")
        conn.commit()
        time.sleep(3)
        main()


    def match_list():
        print("\nSelect dates to view scheduled matches:\n")

        while True:
            start = input("From (YYYY-MM-DD):")
            try:
                start = datetime.strptime(start, "%Y-%m-%d")
                break
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        while True:
            end = input("Until (YYYY-MM-DD): ")
            try:
                end = datetime.strptime(end, "%Y-%m-%d")
                break
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        cur.execute("SELECT * FROM match "
                    "WHERE date BETWEEN '" + start.strftime("%Y-%m-%d") + "' AND '" + end.strftime(
            "%Y-%m-%d") + "' ORDER BY date;")
        matches = cur.fetchall()

        columns = [description[0] for description in cur.description]
        print(tabulate(matches, headers=columns, tablefmt="pretty"))
        #print("\t" + str(matches) + "\t\n")

        conn.commit()
        time.sleep(3)
        main()


    def athlete_course(level, athleteID):
        courses = ''
        if level == "advanced intermediate" or level == "advanced":
            cur.execute("SELECT * FROM course WHERE courseID LIKE 'A%' ")
            courses = cur.fetchall()
        if level == "intermediate" or level == "beginner":
            cur.execute("SELECT * FROM course WHERE courseID LIKE 'B%' ")
            courses = cur.fetchall()
        if level == "junior":
            cur.execute("SELECT * FROM course WHERE courseID LIKE 'J%' ")
            courses = cur.fetchall()
        if level == "professional":
            cur.execute("SELECT * FROM course WHERE courseID LIKE 'P%' ")
            courses = cur.fetchall()
        if level == "special needs":
            cur.execute("SELECT * FROM course WHERE courseID LIKE 'S%' ")
            courses = cur.fetchall()

        availablecourses = []
        for course in courses:
            cur.execute(
                "SELECT COUNT(athID) FROM athlete_course GROUP BY courseID HAVING courseID = '" + course[0] + "';")
            num_athletes = cur.fetchone()
            if num_athletes == None:
                num_athletes = (0,)
            cur.execute("SELECT no_of_participants FROM course WHERE courseID = '" + course[0] + "';")
            max_participants = cur.fetchone()
            if num_athletes[0] < max_participants[0]:
                courseid = course[0]
                # Get course number (ex. J2):
                coursenum = courseid[:2]
                if coursenum not in availablecourses:
                    availablecourses.append(coursenum)
                day = course[1]
                time = course[2]
                cur.execute("SELECT courtID FROM lesson WHERE courseID = '" + courseid + "';")
                courtid = cur.fetchone()[0]
                if courseid.endswith('1'):
                    print(coursenum, ":", day, time, ", court:", courtid, ", availability:", max_participants[0]-num_athletes[0], "spots")
                else:
                    print("\t", day, time, ", court:", courtid)

        while True:
            print("Select course (", availablecourses, ") : ")
            selCourse = input().upper()
            if selCourse not in availablecourses:
                print("This is not a valid course.")
                continue
            else:
                break

        course_1 = f"{selCourse}{'_1'}"
        course_2 = f"{selCourse}{'_2'}"

        conn.execute('''INSERT INTO athlete_course VALUES(?,?)''', (athleteID, course_1))
        conn.execute('''INSERT INTO athlete_course VALUES(?,?)''', (athleteID, course_2))

        conn.commit()


    def generate_schedule():
        print("Course:\n")
        # Check for valid level
        valid_levels = {"junior", "beginners", "advanced", "high-performance", "special needs"}
        while True:
            level = input("Course level: ").lower()
            if level in valid_levels:
                break
            else:
                print(
                    "\nERROR: Please enter a valid course level (junior/beginners/advanced/high-performance/special needs).\n")

        for i in range(2):
            while True:
                print("\nLesson", i+1, "\n")
                # Check for valid day
                valid_days = {"monday", "tuesday", "wednesday", "thursday", "friday"}
                while True:
                    day = input("Day: ").lower()
                    if day in valid_days:
                        break
                    else:
                        print("\nERROR: Please enter a valid day. \n")
                # Check time format
                while True:
                    time_ = input("Time (HH:MM): ")
                    try:
                        datetime.strptime(time_, "%H:%M")
                        break
                    except ValueError:
                        print("\nERROR: Invalid time format. Please enter in HH:MM.\n")
                # Check for valid duration
                while True:
                    duration = input("Duration (Hours): ")
                    try:
                        duration_float = float(duration)
                        if 0 <= duration_float <= 10 and duration_float % 0.5 == 0:
                            break
                        else:
                            print("\nERROR: Please enter a valid duration (Example: 1.5 hours).\n")
                    except ValueError:
                        print("\nERROR: Please enter a valid numeric duration.\n")
                # Check for valid participants
                while True:
                    no_of_participants = input("Max participants: ")
                    if no_of_participants.isdigit():
                        break
                    else:
                        print("\nERROR: Please provide a valid number.\n")
                cur.execute(
                    "SELECT coachID FROM coach WHERE specialization = '" + level + "' AND coachID NOT IN (SELECT coachID FROM course "
                    "WHERE (day = '" + str(day) + "' AND time = '" + time_ + "') OR (day = '" + str(day) + "' AND time < '" + time_ + "' AND time + "
                    "duration > '" + time_ + "') OR (day = '" + str(day) + "' AND time > '" + time_ + "' AND time < '" + time_ + "' + " + duration + "))")

                available = cur.fetchall()
                available_coaches = [coach[0] for coach in available]

                if available_coaches:
                    coachID = random.choice(available_coaches)
                    print("Selected coach ID:", coachID)
                    break
                else:
                    print("\nNo available coaches with", level,
                          "for this day and time. Choose different day / time / specialization.\n")


            cur.execute(
                "SELECT courtID FROM court WHERE courtID NOT IN (SELECT L.courtID FROM lesson AS L JOIN course AS C WHERE L.courseID = C.courseID "
                "AND C.day = '" + str(day) + "' AND C.time = '" + time_ + "')")
            available = cur.fetchall()
            available_courts = [court[0] for court in available]

            if available_courts:
                print("\nAvailable courts:\n")
                for item in available_courts:
                    cur.execute("SELECT surface FROM court where courtID = '" + item + "'")
                    surf = cur.fetchone()[0]
                    print(item, ":", surf)

                # Check format for court ID
                while True:
                    courtID = input("\nChoose one of the available courts. CourtID: ").upper()

                    if re.match(r'^CR\d{2}$', courtID):
                        if courtID in available_courts:
                            break
                        else:
                            print("\nERROR: Choose one of the available courts.\n")
                    else:
                        print("\nERROR: Court ID should start with 'CR' followed by 2 digits.\n")

            courseID = ''
            pref = level[0].upper()
            cur.execute("SELECT max(courseID) FROM course WHERE courseID LIKE '" + str(pref) + "%'")
            courseID = cur.fetchone()[0]

            if not courseID:
                courseID = level[0].upper() + '1_1'
            else:
                courseID_num = int(courseID[1:-2])
                if i+1 < 2:
                    courseID_num += 1
                courseID = courseID[0] +  str(courseID_num) + '_' + str(i+1)

            cur.execute("SELECT MAX(lessonID) FROM lesson")
            lessonID = cur.fetchone()[0]

            if not lessonID:
                lessonID = 'L' + '001'
            else:
                lessonID_num = int(lessonID[1:])
                lessonID_num += 1
                lessonID = lessonID[0] + str(lessonID_num).zfill(3)

            current_day = today.weekday()
            target_day_i = list(calendar.day_name).index(day.capitalize())
            days_until_target_day = (target_day_i - current_day) % 7
            target_day = today + timedelta(days=days_until_target_day)

            try:
                conn.execute(
                    '''INSERT INTO course (courseID, day, time, duration, no_of_participants, coachID) VALUES(?,?,?,?,?,?)''',
                    (courseID, day, time_, duration, no_of_participants, coachID))

                conn.execute(
                    '''INSERT INTO lesson (lessonID, courseID, date, time, duration, courtID, cancellationID) VALUES(?,?,?,?,?,?,?)''',
                    (lessonID, courseID, target_day.strftime('%Y-%m-%d'), time_, duration, courtID, None))
                print("\nCourse", courseID, "successfully generated with first lesson", lessonID, "on", day,
                      target_day.strftime('%Y-%m-%d'), "at", time_, "\n")
            except Exception as e:
                print("\nAn error occured with the lesson's generation:", e, "\nYou are going back to main.\n")
                time.sleep(2)
                main()

        while True:
            choice = input("Do you want to generate another course? (Y/N): ").upper()
            if choice == 'Y' or choice == 'N':
                break
            else:
                print("\nERROR: Please type 'Y' or 'N'.\n")
        if choice == 'N':
            conn.commit()
            time.sleep(2)
            main()
        else:
            generate_schedule()


    def run_schedule_generator():
        while True:
            choice = input(
                "\nTo generate new weekly schedule, the former one will be deleted. Continue? (Y/N): ").upper()
            if choice == 'Y' or choice == 'N':
                break
            else:
                print("\nERROR: Please type 'Y' or 'N'.\n")
        if choice == 'N':
            print("\nYou are going back to the main menu.")
            time.sleep(2)
            main()
        else:
            try:
                conn.execute("DELETE FROM course")
                conn.execute("DELETE FROM lesson")
                print("\nFormer schedule succesfully deleted.\nNew schedule:\n")
            except:
                print("\nAn error occured.\n")
                time.sleep(2)
                main()

        generate_schedule()


    def record_equipment():
        print("\nRecord equipment purchase:\n")

        while True:
            athleteID = input("Athlete ID: ").upper()

            if re.match(r'^[AC]\d{5}$', athleteID):
                break
            else:
                print("\nERROR: Athlete ID should start with 'A' followed by 5 digits.\n")

        while True:
            date = input("Date of buy (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        type = input("Type of equipment: ")

        while True:
            quantity = input("Quantity: ")
            if quantity.isdigit():
                break
            else:
                print("\nERROR: Please provide a valid number.\n")

        equipmentID = ''

        cur.execute("SELECT max(eqID) FROM equipment;")
        equipmentID = cur.fetchone()
        equipmentID = increase(equipmentID)

        conn.execute(
            '''INSERT INTO equipment (eqID,type,quantity,buy_date, athID) VALUES(?,?,?,?,?)''',
            (equipmentID, type, quantity, date.strftime("%Y-%m-%d"), athleteID))

        print("\nEquipment purchase successfully recorded. ID:", equipmentID)

        conn.commit()
        time.sleep(3)
        main()


    def wrong_option(opt):
        print("Input: \"", opt, "\" is not an option. You are going back to the main menu.\n")
        time.sleep(2)
        main()


    def check_if_athlete_exists(athid):
        cur.execute("SELECT athID FROM athlete WHERE athID = '" + athid + "' LIMIT 1")
        athid = cur.fetchone()
        if athid == None:
            exist = 0
        else:
            exist = 1

        return exist


    def score():
        cur.execute(
            "SELECT m.matchID, m.no_of_participants, m.date, m.time FROM match as m LEFT JOIN match_competitors as c ON c.matchID = m.matchID "
            "WHERE date <= '" + today.strftime("%Y-%m-%d") + "' AND c.winning = '' GROUP BY m.matchID;")
        matches = cur.fetchall()

        columns = [description[0] for description in cur.description]
        print(tabulate(matches, headers=columns, tablefmt="pretty"))
        #print("\t" + str(matches) + "\t\n")

        matchid = input("Choose match ID to edit score: ")
        cur.execute("SELECT matchID FROM match_competitors WHERE matchID = '" + matchid + "' AND winning = '' LIMIT 1")
        matchid = cur.fetchone()
        while matchid == None:
            matchid = input("Invalid match ID.\nChoose match ID to edit score: ")
            cur.execute("SELECT matchID FROM match WHERE matchID = '" + matchid + "' LIMIT 1")
            matchid = cur.fetchone()

        matchid = matchid[0]
        cur.execute("SELECT athID FROM match_competitors WHERE matchID = '" + matchid + "';")
        athlIDs = cur.fetchall()
        athletes = []
        for i in athlIDs:
            athletes.append(i[0])

        team1 = [athletes[:int(len(athletes) / 2)]]
        team2 = [athletes[int(len(athletes) / 2):]]

        print("Team 1: ", team1[0], "\nTeam2: ", team2[0])
        score1 = input("Team 1 score: ")
        score2 = input("Team 2 score: ")
        winnersID = []

        cur.execute("SELECT no_of_participants FROM match WHERE matchID = '" + matchid + "';")
        participants = cur.fetchone()[0]

        if score1 > score2:
            winnersID.append(athletes[int(len(athletes) / 2 - 1)])
            if participants == 4:
                winnersID.append(athletes[int(len(athletes) / 2 - 2)])
        if score1 < score2:
            winnersID.append(athletes[int(len(athletes) / 2)])
            if participants == 4:
                winnersID.append(athletes[int(len(athletes) / 2 + 1)])
        winning = max(score1, score2)
        losing = min(score1, score2)

        conn.execute(
            "UPDATE score SET winning = '" + winning + "', losing = '" + losing + "' WHERE matchID = '" + matchid + "';")
        conn.execute("UPDATE match_competitors SET winning = '0' WHERE matchID = '" + matchid + "';")
        for winner in winnersID:
            conn.execute(
                "UPDATE match_competitors SET winning = '1' WHERE matchID = '" + matchid + "' AND athID = '" + winner + "';")

        print("Match ", matchid, " won by ", winnersID, ". Score edited successfully.")
        conn.commit()
        time.sleep(3)
        main()


    def main():
        print("\n1- Members\n2- Reservations\n3- Lessons\n4- Matches\n5- Equipment\n6- Frequently asked questions\n7- Exit")
        mode = input("\nChoose mode: ")

        if mode == '1':
            mode = input("\n1-Athletes\n2-Coaches\n\nSelect : ")
            if mode == '1':
                mode = input("\n1-New member\n2-Delete member\n3-Edit details\n\nSelect: ")
                if mode == '1':
                    new_member('A')
                elif mode == '2':
                    delete_member()
                elif mode == '3':
                    edit_details('A')
                else:
                    wrong_option(mode)
            elif mode == '2':
                mode = input("\n1-New coach\n2-Delete coach\n3-Edit details\n\nSelect: ")
                if mode == '1':
                    new_member('C')
                elif mode == '2':
                    delete_member()
                elif mode == '3':
                    edit_details('C')
                else:
                    wrong_option(mode)
            else:
                wrong_option(mode)
        elif mode == '2':
            mode = input(
                "\n1-New reservation\n2-Cancel reservation\n3-View reservation-list\n\nSelect: ")
            if mode == '1':
                new('reservation', '')
            elif mode == '2':
                cancel_reservation()
            elif mode == '3':
                reservation_list()
            else:
                wrong_option(mode)
        elif mode == '3':
            mode = input(
                "\n1-New lesson\n2-Cancel lesson\n3-View scheduled lessons\n4-Create weekly schedule\n\nSelect: ")
            if mode == '1':
                new('lesson', '')
            elif mode == '2':
                cancel_lesson()
            elif mode == '3':
                lesson_list()
            elif mode == '4':
                run_schedule_generator()
            else:
                wrong_option(mode)
        elif mode == '4':
            mode = input("\n1-New match\n2-Cancel match\n3-Insert match results\n4-View match list\n\nSelect: ")
            if mode == '1':
                new('match', '')
            elif mode == '2':
                cancel_match()
            elif mode == '3':
                score()
            elif mode == '4':
                match_list()
            else:
                wrong_option(mode)
        elif mode == '5':
            record_equipment()
        elif mode == '6':
            tennis_club_queries.main()
        elif mode == '7':
            print("\nBye!")
            exit()
        else:
            wrong_option(mode)


    if __name__ == "__main__":
        print("---TENNIS CLUB APP---\n")
        main()
        conn.close()