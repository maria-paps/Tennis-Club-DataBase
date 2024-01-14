import sqlite3
from datetime import datetime, timedelta
import time
from tabulate import tabulate
from datetime import date
import edit_db
today = date.today()

try:
    with sqlite3.connect("tennis_club_db.db") as conn:
        cur = conn.cursor()


    def active_subscriptions():
        cur.execute("SELECT count(athID) FROM athlete WHERE pack_end_date >= CURRENT_DATE")
        num = cur.fetchone()[0]

        print("\nAt this moment, there are", num, "athletes with active subscriptions: \n")
        cur.execute("SELECT lastname, firstname, memberID FROM member WHERE memberID IN (SELECT athID FROM athlete WHERE pack_end_date >= CURRENT_DATE) ORDER BY lastname")
        athletes = cur.fetchall()

        for item in athletes:
            print(item[0], item[1], " ", item[2])

        input()
        conn.commit()
        main()


    def level_percentage():
        valid_levels = {"junior", "beginner", "intermediate", "advanced intermediate", "advanced", "professional"}
        while True:
            level = input("\nInput the level you want to see the percentage of athletes from all active subscriptions.\n(junior/beginner/intermediate/advanced intermediate/advanced/professional): ").lower()
            if level in valid_levels:
                break
            else:
                print("\nERROR: Please enter a valid athlete level.")

        cur.execute("SELECT count(athID) FROM athlete WHERE pack_end_date >= CURRENT_DATE")
        all_athletes = cur.fetchone()[0]

        cur.execute("SELECT COUNT(athID) FROM athlete WHERE level = '" + level + "' AND athID in (SELECT athID FROM athlete WHERE pack_end_date >= CURRENT_DATE)")
        level_athletes = cur.fetchone()[0]

        percentage = float((level_athletes/all_athletes)*100)

        print("\nThe percentage of", level, "athletes between all active subscriptions is: ", round(percentage, 2), "%")

        while True:
            choice = input("\nDo you want to see the percentage of a different level? (Y/N): ").upper()
            if choice == 'Y' or choice == 'N':
                break
            else:
                print("\nERROR: Please type 'Y' or 'N'.\n")

        if choice == 'Y':
            level_percentage()
        else:
            conn.commit()
            time.sleep(2)
            main()

    def available_courts():
        while True:
            date = input("\nInput date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("\nERROR: Invalid date format. Please enter in YYYY-MM-DD.\n")

        while True:
            time_ = input("Input time (HH:MM): ")
            try:
                datetime.strptime(time_, "%H:%M")
                break
            except ValueError:
                print("\nERROR: Invalid time format. Please enter in HH:MM.\n")

        cur.execute("SELECT courtID, surface FROM court WHERE courtID IN (SELECT courtID FROM reservation WHERE (date = '" + str(date.date()) + "' AND time "
            "= '" + time_ + "') OR (date = '" + str(date.date()) + "' "
            "AND time < '" + time_ + "' AND time + duration >= '" + time_ + "') UNION SELECT courtID FROM lesson WHERE (date = '" + str(date.date()) + "' AND time "
            "= '" + time_ + "') OR (date = '" + str(date.date()) + "' AND time < '" + time_ + "' AND time + duration >= '" + time_ + "') UNION SELECT courtID FROM "
            "match WHERE (date = '" + str(date.date()) + "' AND time = '" + time_ + "') OR (date = '" + str(date.date()) + "' AND time < '" + time_ + "' AND time + "
            "duration >= '" + time_ + "'))")

        courts = cur.fetchall()

        if not courts:
            print("\nThere are no courts available at this date and time.")
        else:
            print("\nAvailable courts at", str(date.date()), time_)
            for item in courts:
                print("ID:", item[0], " surface:", item[1])
        input()
        conn.commit()
        main()

    def equipment_types():
        cur.execute("SELECT COUNT(DISTINCT type) FROM equipment")
        num = cur.fetchone()[0]

        cur.execute("SELECT DISTINCT type FROM equipment ORDER BY type")
        equipment_types = cur.fetchall()

        print("\nThe Tennis Club has", num, "different types of equipment. These are:")
        for item in equipment_types:
            print(item[0])

        cur.execute("WITH TypeCounts AS (SELECT type, COUNT(athID) AS total_athletes FROM equipment GROUP BY type) SELECT type, "
                    "total_athletes FROM TypeCounts WHERE total_athletes = (SELECT MAX(total_athletes) FROM TypeCounts);")
        most_bought = cur.fetchall()

        print("\nThe most bought ones are: ")
        for item in most_bought:
            print(item[0])

        input()
        conn.commit()
        main()

    def average_age():
        cur.execute("SELECT AVG(date() - birthdate) AS average_age FROM member;")
        avg_age = cur.fetchone()[0]

        print("\nAverage athlete's age is", int(avg_age))

        input()
        conn.commit()
        main()


    def winner():
        cur.execute("WITH WinCounts AS (SELECT athID, COUNT(*) as total_wins FROM match_competitors WHERE winning = 1 GROUP BY athID) SELECT lastname,"
                    " firstname, athID, total_wins FROM WinCounts JOIN member WHERE total_wins = (SELECT MAX(total_wins) FROM WinCounts) AND memberID = athID;")
        winners = cur.fetchall()

        print("\nAthlete(s) with most wins: ")
        for item in winners:
            print(item[0], item[1], " ID:", item[2], " wins:", item[3])

        input()
        conn.commit()
        main()

    def pack_percentages():
        cur.execute("SELECT COUNT(athID) FROM athlete")
        athletes = cur.fetchone()[0]

        cur.execute("SELECT P.type, COUNT(A.athID) FROM athlete AS A JOIN package AS P WHERE P.packID = A.packID GROUP BY P.packID")
        packages = cur.fetchall()

        print("\nPackage percentages:\n")
        for item in packages:
            percentage = (float(item[1])/float(athletes))*100
            print(round(percentage, 2), "% of all athletes have a", item[0], "package.")

        input()
        conn.commit()
        main()

    def rescheduled_reservations():
        cur.execute("SELECT DISTINCT memberID FROM reservation WHERE cancellationID IS NOT NULL")
        members = cur.fetchall()

        if not members:
            print("\nNo reservations have been rescheduled up until now.")
        else:
            print("\nAmong the members that have made reservations:\n")
            for item in members:
                cur.execute("SELECT COUNT(DISTINCT reservationID) FROM reservation WHERE memberID = '" + str(item[0]) + "'")
                all = cur.fetchone()[0]
                cur.execute("SELECT COUNT(DISTINCT reservationID) FROM reservation WHERE memberID = '" + str(item[0]) + "' AND cancellationID NOT NULL")
                cancelled = cur.fetchone()[0]
                cur.execute("SELECT lastname FROM member WHERE memberID = '" + str(item[0]) + "'")
                l_name = cur.fetchall()[0]
                cur.execute("SELECT firstname FROM member WHERE memberID = '" + str(item[0]) + "'")
                f_name = cur.fetchall()[0]

                percentage = (float(cancelled)/float(all))*100

                print("Member", str(l_name)[2:-3], str(f_name)[2:-3], "has rescheduled", round(percentage, 2), "% of the reservations they have made.")
        input()
        conn.commit()
        main()

    def wrong_option(opt):
        print("Input: \"", opt, "\" is not an option. \n")
        time.sleep(2)
        main()

    def main():
        print("\n\n1 - Athletes with active subscriptions\n2 - From active subscriptions, percentage of athletes with specific level\n"
              "3 - Available courts for specific date and time\n4 - Different equipment types and most bought type\n"
              "5 - Average athlete's age\n6 - Athlete with most wins"
              "\n7 - Package percentages\n8 - Resceduled reservations\n9- Exit\n")
        mode = input("Choose query: ")

        if mode == '1':
            active_subscriptions()
        elif mode == '2':
            level_percentage()
        elif mode == '3':
            available_courts()
        elif mode == '4':
            equipment_types()
        elif mode == '5':
            average_age()
        elif mode == '6':
            winner()
        elif mode == '7':
            pack_percentages()
        elif mode == '8':
            rescheduled_reservations()
        elif mode == '9':
            print("\nBack to main menu.")
            time.sleep(2)
            edit_db.main()
        else:
            wrong_option(mode)


    if __name__ == "__main__":
        print("\n---TENNIS CLUB EXAMPLE QUERIES---")
        main()
        conn.close()

except sqlite3.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()
