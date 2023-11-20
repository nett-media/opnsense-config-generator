from xml.sax.saxutils import escape
import sys

def escape_string(s):
    return escape(s, {"ä": "&#xE4;", "ö": "&#xF6;", "ü": "&#xFC;", "ß": "&#xDF;", "Ä": "&#xC4;", "Ö": "&#xD6;", "Ü": "&#xDC;"})

if __name__ == "__main__":
    # Prüfen, ob ein Argument angegeben wurde
    if len(sys.argv) < 2:
        print("Bitte geben Sie einen String als Argument an.")
        sys.exit(1)

    input_string = sys.argv[1]
    escaped = escape_string(input_string)
    print(escaped)
