import argparse
import io
import pstats
import time

maps = [
    [
        "############",
        "#  #     # #",
        "## # ### # #",
        "#  # # # # #",
        "## ### # # #",
        "#        # #",
        "## ####### #",
        "#          #",
        "# ######## #",
        "# #   #    #",
        "#   #   # ##",
        "######A#####"
    ],
    [
        "################################",
        "#                              #",
        "# ############################ #",
        "# # ###       ##  #          # #",
        "# #     ##### ### # ########## #",
        "# #   ##### #     # #      ### #",
        "# # ##### #   ###   # # ## # # #",
        "# # ### # ## ######## # ##   # #",
        "# ##### #  # #   #    #    ### #",
        "# # ### ## # # # # ####### # # #",
        "# #        # #   #     #     # #",
        "# ######## # ######### # ### # #",
        "# ####     #  # #   #  # ##### #",
        "# # #### #### # # # # ## # ### #",
        "#                      # #     #",
        "###########################A####"
    ],
    [
        "###########################A####",
        "#   #      ## # # ###  #     # #",
        "# ###### #### # # #### ##### # #",
        "# # ###  ## # # # #          # #",
        "# # ### ### # # # # # #### # # #",
        "# #     ### # # # # # ## # # # #",
        "# # # # ### # # # # ######## # #",
        "# # # #     #          #     # #",
        "# ### ################ # # # # #",
        "# #   #             ## # #   # #",
        "# # #### ############# # #   # #",
        "# #                    #     # #",
        "# # #################### # # # #",
        "# # #### #           ###     # #",
        "# # ## # ### ### ### ### # ### #",
        "# #    #     ##  ##  # ###   # #",
        "# ####   ###### #### # ###  ## #",
        "###########################A####"
    ], [
        "#############",
        "#           #",
        "#           #",
        "#           #",
        "###########A#"
    ]
]


def readMaze(file):
    """
    Reading Maze from txt File

    :param file: txt-File
    :return: lines of String
    """
    with open(file, 'r') as datei:
        lines = datei.readlines()
    return [line.strip() for line in lines]



def fromStrings(mapsItem):
    """
    Converting String maze to List

    :param mapsItem: String of Maze
    :return: list
    """
    return [list(row) for row in mapsItem]


def printLabyrinth(lab):
    """
    Print the Labyrinth

    :param lab:  Labyrinth
    :return: print Maze
    """
    for row in lab:
        print("".join(row))


def suche(zeile, spalte, lab):
    """
    Suche Ausgang

    :param zeile: Start-Pos X
    :param spalte: Start-Pos Y
    :param lab: Labyrinth
    :return: Boolean 1 or 0
    """
    if zeile < 0 or zeile >= len(lab) or spalte < 0 or spalte >= len(lab[zeile]) or lab[zeile][spalte] == '#' or \
            lab[zeile][spalte] == '.' or lab[zeile][spalte] == 'X':
        return 0

    if lab[zeile][spalte] == 'A':
        return 1

    if args.delay:
        lab[zeile][spalte] = 'X'
    else:
        lab[zeile][spalte] = '.'


    if args.print:
        printLabyrinth(lab)
    if args.delay:
        lab[zeile][spalte] = '.'
        time.sleep(args.delay / 1000)

    if (suche(zeile + 1, spalte, lab) or
            suche(zeile - 1, spalte, lab) or
            suche(zeile, spalte + 1, lab) or
            suche(zeile, spalte - 1, lab)):
        return 1

    lab[zeile][spalte] = ' '

    return 0


def suchenAlle(zeile, spalte, lab):
    """
    Recursive searching and counting all possible ways

    :param zeile: Start-Pos X
    :param spalte: Start-Pos Y
    :param lab: Labyrinth
    :return: Boolean 1 or 0
    """
    counter = 0

    if zeile < 0 or zeile >= len(lab) or spalte < 0 or spalte >= len(lab[zeile]) or lab[zeile][spalte] == '#' or \
            lab[zeile][spalte] == 'X' or lab[zeile][spalte] == '.':
        return 0

    if lab[zeile][spalte] == 'A':
        return 1

    # Falls Delay dann wird es in einer Spielersicht angezeigt
    if args.delay:
        lab[zeile][spalte] = 'X'
    else:
        lab[zeile][spalte] = '.'


    if args.print:
        printLabyrinth(lab)
    if args.delay:
        lab[zeile][spalte] = '.'
        time.sleep(args.delay / 1000)

    counter += suchenAlle(zeile + 1, spalte, lab)
    counter += suchenAlle(zeile - 1, spalte, lab)
    counter += suchenAlle(zeile, spalte + 1, lab)
    counter += suchenAlle(zeile, spalte - 1, lab)

    lab[zeile][spalte] = ' '

    return counter


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--XSTART", type=int, help="x-coordinate to start")
    parser.add_argument("-y", "--YSTART", type=int, help="y-coordinate to start")
    parser.add_argument("-p", "--print", help="print output of every solution", action="store_true")
    parser.add_argument("-t", "--time", help="print total calculation time (in milliseconds)", action="store_true")
    parser.add_argument("-d", "--delay", type=int, help="delay after printing a solution (in milliseconds)")

    parser.add_argument("file", help="file with the userdata")

    args = parser.parse_args()

    labyrinth = fromStrings(readMaze(args.file))
    if args.print:
        printLabyrinth(labyrinth)

    if args.time:
        pr = cProfile.Profile()
        pr.enable()

        wegAnzahl = suchenAlle(args.XSTART, args.YSTART, labyrinth)

        pr.disable()

        print(f"Anzahl gefundener Wege: {wegAnzahl}")

        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        profile_results = s.getvalue()

        # Ergebnisse in einer Datei speichern
        with open('profile_results.txt', 'w') as file:
            file.write(s.getvalue())

        s.close()
        print("Profilergebnisse in 'profile_results.txt' gespeichert.")
    else:
        wegAnzahl = suchenAlle(args.XSTART, args.YSTART, labyrinth)
        print(f"Anzahl gefundener Wege: {wegAnzahl}")
