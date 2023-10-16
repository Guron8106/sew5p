import random
import string
import unicodedata

from openpyxl.reader.excel import load_workbook


def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    erg = unicodedata.normalize('NFC', shaved)
    return erg

def generate_password():
    """Generates Password for a user
    for _ in range(10): This part creates a loop that repeats 10 times (range(10)). During each iteration,
     a random letter is chosen.

    """
    password_chars = string.ascii_letters + "!%&(),._-=^#!%&(),._-=^#"
    return ''.join(random.choice(password_chars) for _ in range(10))


if __name__ == '__main__':
    wb = load_workbook("Namen.xlsx", read_only=True)
    ws = wb[wb.sheetnames[0]]
