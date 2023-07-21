

# PDF-Formulardaten aktualisieren


Diese Skript ermöglicht das automatische Ausfüllen des Formulars [Stundennachweis für studentische Hilfskräfte](https://www.uni-bremen.de/fileadmin/user_upload/fachbereiche/fb3/fb3/Bilder/Service/Downloads/Studentische_Hilfskraefte/Stundenzettel_timesheet_2019_Blanko.pdf)


## Installation


1.  Installiere die erforderlichen Abhängigkeiten: `pip install pdfrw argparse datetime json `
2.  Lade die Dateien aus dem Repository herunter oder klone das Repository auf deinen lokalen Computer.
3.  Anpassen von `personalData.json`
    ```json
    {
    "(Projekt)": "X",
    "(NameVorname)": "Doe, John",
    "(Sprecher)": "Martin Max",
    "(Geboren am)": "04.05.1904",
    "(BereichProjektleiterin)": "Mr. X",
    "(VertragsNr)": "62271",
    "(vertrag_von)": "01.01",
    "(vertrag_bis)": "30.07",
    "( Urlaubsstd)": null
    }
    ```
4. Optional: Anpassung von fixen Arbeitstagen in `fixedDays.json`:
    ```json
    {
    "Monday": null,
    "Tuesday": "09:00-17:30",
    "Wednesday": "09:00-17:30",
    "Thursday": null,
    "Friday": null,
    "Saturday": null,
    "Sunday": null
    }
    ```
    **Achtung:** Uhrzeit muss mit führender 0 beginnen. 



## Verwendung

1. Navigiere in das Verzeichnis des Skripts.
2. Passe die Befehlszeilenargumente entsprechend an:
    - `-i` oder `--input`: Pfad zur Eingabe Formular das befüllt werden soll.
    - `-o` oder `--output`: Pfad zur Ausgabe-PDF-Datei, in der die aktualisierten Daten gespeichert werden sollen.
    - `-m` oder `--month`: Der Monat(1-12), für den das Dokument ausgefüllt werden soll.
    - `-y` oder `--year`: Das Jahr, für das das Dokument ausgefüllt werden soll.
    - `-l` oder `--lunch`: die Länge der Pause in Minunten.

Die Pause wird von den geleisteten Stunden abgezogen.
Wir beispielsweise von 09:00 Uhr bis 17:30 Uhr gearbeitet und eine Pause von 30 Minuten angegeben, beträgt die ausgewiesene Arbeitszeit 8 Stunden. 

```bash
python3 script.py -i input.pdf -o output.pdf -m 7 -y 2023 -l 30
```

## Öffnen der Ausgabe 
Aktuell stellt nur `firefox` das ausgefüllte Formular richtig dar. Um die *selbstrechnenden* Felder, welche die Wochenarbeitsstunden summieren zu aktivieren, muss in ein beliebiges Tages geklickt und mit *Enter* bestätigt werden.
