import sys
import pdfrw
import json

# Findet alle Formularfelder in einem PDF-Dokument
# und speichert sie in einem Dictionary
# das Name und Wert des Feldes enthält

# Wird nicht direkt verwendet, 
# hilft aber beim analysieren der PDF-Datei

# Konstantenvariablen für Dateinamen der Ausgabe
OUTPUT_JSON_PATH = 'allFields.json'

# Überprüfe, ob der richtige Anzahl von Argumenten übergeben wurde
if len(sys.argv) != 2:
    print("Bitte geben Sie den Pfad zur PDF-Datei als Argument an.")
    sys.exit(1)

# Extrahiere den Pfad zur PDF-Datei aus den Argumenten
pdf_path = sys.argv[1]

# Ein leeres Dictionary erstellen
data = {}

# Lade das PDF-Dokument
pdf_template = pdfrw.PdfReader(pdf_path)

# Rufe das erste Seitenobjekt
page = pdf_template.pages[0]

# Überprüfe , ob das Seitenobjekt Formularfelder enthält
if '/Annots' in page:
    annotations = page['/Annots']
    for annotation in annotations:
        if annotation['/Subtype'] == '/Widget':
            field_name = annotation['/T']
            field_value = annotation['/V']
            field_type = annotation['/FT']
            
            # Sollte der Wert nicht None sein, entferne die Klammern
            if field_value is not None:
                field_value = field_value.strip("()")
            
            # Füge Einträge zum Dictionary hinzu
            data.update({field_name.strip("()"): field_value})
else:
    print("Das Dokument enthält keine Formularfelder.")

# Speichere das Dictionary als JSON
with open(OUTPUT_JSON_PATH, "w") as file:
    json.dump(data, file, indent=4)

