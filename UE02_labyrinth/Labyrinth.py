
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

    lab[zeile][spalte] = '.'


    printLabyrinth(lab)


    if (suche(zeile + 1, spalte, lab) or
            suche(zeile - 1, spalte, lab) or
            suche(zeile, spalte + 1, lab) or
            suche(zeile, spalte - 1, lab)):
        return 1

    lab[zeile][spalte] = ' '

    return 0

if __name__ == "__main__":
    print(suche(5, 5, fromStrings(maps[2])))



