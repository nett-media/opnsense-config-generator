import csv
from xml.sax.saxutils import escape

def escape_string(s):
    #return escape(s, {"ä": "& #xE4;", "ö": "& #xF6;", "ü": "& #xFC;", "ß": "& #xDF;", "Ä": "& #xC4;", "Ö": "& #xD6;", "Ü": "& #xDC;", " ": "","-":"_"})
    return escape(s, {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "Ä": "AE", "Ö": "OE;", "Ü": "UE", " ": "","-":"_","/": "_"})

def process_csv(file_name):
    data = []
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Liest den Header
        #headers.append("SaveName")  # Fügt einen neuen Header für das "SaveName" Feld hinzu
        data.append(headers)

        for row in reader:
            #description = row[-1]  # Nimmt das letzte Feld (Beschreibung)
            #row.append(escape_string(description))  # Fügt das geänderte Feld als neuen Eintrag hinzu
            row[-1] = escape_string(row[-1])  # Überschreibt das letzte Feld (Beschreibung) mit dem geänderten Wert
            data.append(row)

    new_file = file_name.replace(".csv", "Sanitized.csv")
    with open(new_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == "__main__":
    csv_file = "config.csv"
    process_csv(csv_file)