import subprocess
from collections import Counter

import matplotlib.pyplot as plt
from dateutil import parser as dt
from matplotlib import ticker


def parse_gitlogs():
    cmd = ['git', 'log', '--pretty=format:%aI']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    stdout, stderr = process.communicate()

    commit_dates = [dt.parse(date_str) for date_str in stdout.strip().split('\n')]
    return commit_dates


def drawplot(commit_dates):
    days = [commit_date.weekday() +1 for commit_date in commit_dates]
    hours = [commit_date.hour for commit_date in commit_dates]

    # Angenommen, commit_dates ist eine Liste von datetime-Objekten der Commits
    commit_times = [(d.weekday(), d.hour) for d in commit_dates]
    commit_count = Counter(commit_times)

    # Erstellen Sie eine Liste von Größen für die Scatter-Punkte, basierend auf der Anzahl der Commits
    sizes = [commit_count[(day, hour)] * 100 for day, hour in commit_times]

    plt.figure(figsize=(9, 6), dpi=80)
    plt.scatter(hours, days, sizes=sizes, alpha=0.5)

    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.tick_params(which='major', axis='x', direction='in', length=4, bottom=True, top=True)

    plt.title(fr'Karanbir Guron: {len(commit_count)} commits')
    plt.ylabel("Wochentage")
    plt.xlabel("Uhrzeit")

    plt.xlim(1, 23)
    plt.yticks([1, 2, 3, 4, 5, 6, 7],
               [r'mon', r'tue', r'wed', r'thu', r'fri', r'sat', r'sun'])

    plt.grid()

    plt.savefig("git_logs.png", dpi=80)
    plt.show()



if __name__ == "__main__":
    drawplot(parse_gitlogs())
