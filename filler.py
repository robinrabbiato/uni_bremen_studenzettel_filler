import argparse
import pdfrw
import json
from buildFieldValues import buildFields 

# Argument-Parser erstellen
parser = argparse.ArgumentParser(description='PDF-Formulardaten aktualisieren')

# Pfade zur PDF-Datei und zur JSON-Datei als Switches hinzufügen
parser.add_argument('-i', '--input', help='Pfad zur PDF-Datei', required=True)
parser.add_argument('-o', '--output', help='Pfad zur Ausgabedatei (PDF)', required=True)
parser.add_argument('-m', '--month', help='der Monat für den das Dokument ausgefüllt werden soll', required=True)
parser.add_argument('-y', '--year', help='das Jahr für den das Dokument ausgefüllt werden soll', required=True)
parser.add_argument('-l', '--lunchbreak', help='die Länge der Pause', required=True)

# Argumente parsen
args = parser.parse_args()

# Pfad zur PDF-Datei und zur JSON-Datei aus den Argumenten extrahieren
pdf_path = args.input
output_pdf_path = args.output
YEAR = args.year
MONTH = args.month
LUNCH = args.lunchbreak

# Bau das Dictionary zum befüllen der Felder
data = buildFields(YEAR, MONTH, LUNCH)

# Lade das PDF-Dokument
pdf_template = pdfrw.PdfReader(pdf_path)

# Rufe das erste Seitenobjekt ab
page = pdf_template.pages[0]
    
# Überprüfe, ob das Seitenobjekt Formularfelder enthält
if '/Annots' in page:
    annotations = page['/Annots']
    for annotation in annotations:
        # Überprüfe, ob das Formularfeld ein Widget ist
        if annotation['/Subtype'] == '/Widget':
            field_name = annotation['/T']
            field_value = annotation['/V']
            field_type = annotation['/FT']

            # Überprüfe, ob das Formularfeld im Dictionary enthalten ist und der Wert nicht None ist
            if field_name in data and data[field_name] != None:
                print("Found key: \t" + field_name)
                # Setze den Wert des Formularfelds auf den Wert aus dem Dictionary
                annotation.update(
                        pdfrw.PdfDict(
                            V=pdfrw.objects.pdfstring.PdfString.encode(
                                data[field_name])))
   
   # Speichere das geänderte PDF-Dokument in einer neuen Datei
    pdfrw.PdfWriter().write(output_pdf_path, pdf_template)
else:
    print("Das Dokument enthält keine Formularfelder.")
