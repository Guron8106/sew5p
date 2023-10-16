import unicodedata

from openpyxl.reader.excel import load_workbook


def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    erg = unicodedata.normalize('NFC', shaved)
    return erg



if __name__ == '__main__':
    wb = load_workbook("Namen.xlsx", read_only=True)
    ws = wb[wb.sheetnames[0]]
