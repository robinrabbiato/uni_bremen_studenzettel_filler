import calendar
import datetime

# Liefert eine Liste von Paaren von Montagen und Sonntagen
# Anfang der Liste ist der erste Montag des Monats
# Je nach Monat hat die Liste 4 oder 5 Paaren

def getMondays (year, month):
    # liefert die Wochen des Monats beispiel: 
    # [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], ...]
    # 0 steht für Tage die nicht zum Monat gehören
    # 1-31 steht für die Tage des Monats
    weeks = calendar.monthcalendar(year, month)

    # liefert eine Liste mit den Montage die 
    # in dem Monat vorkommen. 
    # Ein Tag kommt nicht vor wenn er mit 0 gekennzeichnet ist
    mondays = [week[calendar.MONDAY] for week in weeks 
               if week[calendar.MONDAY] != 0]

    #liefert eine Liste mit den Montagen als Datumsobjekte
    return [datetime.date(year, month, day) for day in mondays]

# liefert die jeweils nächsten Sonntage für eine Liste von Tagen
def getSundays(startDays):
    next_sundays = []
    for startDay in startDays:
        #print("startDay: (", startDay.strftime("%A"),")", startDay)
        days_ahead = (6 - startDay.weekday() + 7) % 7  
        # 6 is Sunday, weekday() returns 0 for Monday
        next_sunday = startDay + datetime.timedelta(days=days_ahead)
        #print(next_sunday.strftime("%A"), next_sunday)
        next_sundays.append(next_sunday)
    return next_sundays

# Liefert eine Liste mit Tupeln.
# Jedes Tupel enthält ein Datumspaar bestehend aus
# Montag und Sonntag
def getDates (year, month):
    mondays = getMondays(year, month)
    sundays = getSundays(mondays)
    dates = []
    for monday, sunday in zip(mondays, sundays):
        dates.append((monday.strftime("%d.%m.%Y"), sunday.strftime("%d.%m.%Y")))
    return dates

