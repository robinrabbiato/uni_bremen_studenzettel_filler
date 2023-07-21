import json
import datetime
from weeks import getDates
from parseFixedDays import parseFixedDays

# Baut das Dictionary mit den Feldern für das PDF
# aus den persönlichen Daten,
# den Kalenderwochen
# und den festen Arbeitstagen

# Pfad zur Datei mit den persönlichen Daten
personal_data_path = "personalData.json"

# Anzahl der Wochen in diesem Monat
weekcount = 0

# Das noch leere Dictionary
dataToFill = {}

# Füllt das Dictionary mit den persönlichen Daten
def addPersonalData():
    with open(personal_data_path, 'r') as file:
        data = json.load(file)
        dataToFill.update(data)

# Fügt die Daten für die Kalenderwochen hinzu
def addDates(year, month):
    # Füge den Eintrag für den Monat hinzu
    dataToFill.update({"(f\u00fcr)": f"{month:02}.{year}"}) 
    # Hole die Kalenderwochen
    dates = getDates(year, month)
    index = 1
    for w in dates:
        # Füge den Eintrag für den Montag hinzu
        dataToFill.update({f"(vonKW{index})": w[0]})
        # Füge den Eintrag füür Sonntag hinzu}
        dataToFill.update({f"(bisKW{index})": w[1]})
        index += 1
    global weekcount
    weekcount =(len(dates))

# Fügt die festen Arbeitstage hinzu        
def addDays(LUNCH):
    days = parseFixedDays()
    for day in days:
        # Start und Ende des Arbeitstages
        start = days[day][:5]
        end = days[day][6:]
        for i in range(weekcount):
            # Erstelle die Keys für die Uhrzeiten und füge sie dem Dictionary hinzu
            # +1 weil das PDF bei 1 anfängt zu zählen
            dataToFill.update({f"(vonUhr{day+1})": start})
            dataToFill.update({f"(bisUhr{day+1})": end})
            # Erstelle DateTime Objekte aus den Uhrzeiten und addiere die Mittagspause
            startDT = datetime.datetime.strptime(start, "%H:%M")
            endDT = datetime.datetime.strptime(end, "%H:%M") 
            # Errechne die Diffenz zwischen Start und Ende
            diff = endDT - startDT
            # Subtrahiere die Mittagspause
            diff = diff - datetime.timedelta(minutes=LUNCH)
            # Errechne die Dezimalstunden auf zwei Nachkommastellen gerundet
            decimalHours = str(round(diff.seconds / 3600, 2)).replace(".", ",")
            # Füge die Dezimalstunden dem Dictionary hinzu
            dataToFill.update({f"(Total{day+1})": decimalHours})
            # Zähle 7 Tage weiter um alle spezifischen Wochentage zu füllen
            day = day +7

# Baut das Dictionary mit den Feldern für das PDF
def buildFields(YEAR, MONTH, LUNCH):
    addPersonalData()
    addDates(int(YEAR), int(MONTH))
    addDays(int(LUNCH))
    return dataToFill
