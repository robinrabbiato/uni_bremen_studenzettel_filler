import datetime 
import json

# Liest die festen Arbeitstage aus der JSON-Datei aus
# und fügt sie dem Dictionary hinzu

# Dictionary um  Wochentage in Zahlen zuzuordnen
dayToInt = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

# Tage in Zahlen mit Uhrzeiten
daysTime = {}

# Die festen Arbeitstage und Uhrzeiten
fixed_days_path = "fixedDays.json"

# Liest die festen Arbeitstage aus der JSON-Datei aus
# und fügt sie dem Dictionary hinzu
def parseFixedDays():
    # Öffne die JSON-Datei mit den festen Arbeitstagen
    with open(fixed_days_path, 'r') as file:
        # Lade die Daten aus der Datei
        data = json.load(file)
        # Iteriere über die Tage
        for day in data:
            # Wenn der Tag nicht None ist, füge ihn dem Dictionary hinzu
            if data[day] != None:
                # Füge den Tag mit der Uhrzeit dem Dictionary hinzu
                daysTime.update({dayToInt[day]: data[day]})
    return daysTime

