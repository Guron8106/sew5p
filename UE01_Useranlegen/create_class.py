import random
import unicodedata

from openpyxl.reader.excel import load_workbook


def shave_marks(txt: str):
    """
    Remove all diacritic marks
    """
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)


def generate_password(user: tuple):
    """
    Generates Password for a user
    """
    special_chars = "!%&(),._-=^#!%&(),._-=^#"
    return f'{user[0]}{random.choice(special_chars)}{user[1]}' \
           f'{random.choice(special_chars)}{user[2]}{random.choice(special_chars)}'


def get_user():
    """
    Generator for user
    min_row = 2, damit die erste Row mit den Übrschriften übersprungen wird
    to use user as a tuple
    """
    for row in ws.iter_rows(min_row=2):
        klasse = str(row[0].value).lower()
        raum = str(row[1].value)
        kv = str(row[2].value)
        yield klasse, raum, kv


if __name__ == "__main__":
    wb = load_workbook("Klassenraeume_2023.xlsx", read_only=True)
    ws = wb[wb.sheetnames[0]]
