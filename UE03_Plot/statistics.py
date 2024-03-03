import subprocess

import matplotlib.pyplot as plt
import numpy
import math
import subprocess
import numpy as np


def parse_gitlogs():
    cmd = ['git', 'log', '--pretty=format:%H|%an|%ad|%s', '--date=short']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    date = []
    # Parsen der Ausgabe
    for line in stdout.decode('utf-8').split('\n'):
        commit_hash, author_name, commit_date, commit_message = line.split('|')
        #print(f"Commit: {commit_hash}")
        #print(f"Autor: {author_name}")
        #print(f"Datum: {commit_date}")
        date.append(commit_date)
        #print(f"Nachricht: {commit_message}\n")
    print(date)

def drawplot():
    logs = parse_gitlogs()
    print(logs)
    return



if __name__ == "__main__":

    drawplot()
