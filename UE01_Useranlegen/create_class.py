import random
import string
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


def generate_scripts():
    """
    Generates scripts and iterates through the users
    set -e = errexit
    set -x = xtrace debugging
    for _ in range(10): This part creates a loop that repeats 10 times (range(10)). During each iteration, a random letter is chosen.
    ''.join(...): This part joins the random letters generated in each iteration together into a single string. ''
    """
    with open("res/create_class.sh", "w") as file:
        print("set -e", file=file)
    with open("res/delete_class.sh", "w") as file:
        print("set -x", file=file)
    open("res/passwords_class.txt", "w").close()
    create_user_entry(("lehrer",), ''.join(random.choice(string.ascii_letters) for _ in range(10)))
    create_user_entry(("seminar",), ''.join(random.choice(string.ascii_letters) for _ in range(10)))
    for user in get_user():
        pw = generate_password(user)
        create_user_entry(user, pw)

def create_user_entry(user, pw):
    """
    Creates a line in the create, delete script and in the password file for the given user
    """
    useradd(user, pw)
    userdel(user)
    addpasswd(user, pw)

def userdel(user):
    """
    Writes userdel command in  File
    """
    delete = f'userdel {user[0]} && rm -rf /home/klassen/k{user[0]}'
    with open("res/delete_class.sh", "a") as file:
        print(delete, file=file)




def useradd(user, pw):
    """
    Writes useradd command in respective File
    user[0][0] accesses the first character of the first element in the user tuple.
    user[0] = klasse
    """
    create = f'useradd -d /home/klassen/{"k" if user[0][0].isdigit() else ""}{user[0]} -c "{user[0]}" -m ' \
             f'-g cdrom,plugdev,sambashare -s /bin/bash {user[0]} && ' \
             f'echo {user[0]}:\"{pw}\" | chpasswd'
    with open("res/create_class.sh", "a") as file:
        print(create, file=file)


def addpasswd(user, pw):
    """
    Writes user with their password in respective File
    """
    with open("res/passwords_class.txt", "a") as file:
        print(user[0], pw, file=file, sep=":")


if __name__ == "__main__":
    wb = load_workbook("Klassenraeume_2023.xlsx", read_only=True)
    ws = wb[wb.sheetnames[0]]
