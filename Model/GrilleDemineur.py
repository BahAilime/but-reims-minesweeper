# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(nb_lignes: int, nb_colonnes: int) -> list:
    """
    Crée une liste de listes construites avec des cellules et retourne cette liste

    :param nb_lignes: Nombre de lignes de la grille
    :param nb_colonnes: Nombre de colonnes de la grille
    :return: grille de nb_lignes * nb_colonnes cellules
    """
    if type(nb_lignes) != int or type(nb_colonnes) != int:
        raise TypeError(f"construireGrilleDemineur:  Le  nombre  de lignes  ({type(nb_lignes)})  ou  de  colonnes  ({type(nb_colonnes)})  n’est  pas  un entier.")
    elif nb_lignes <= 0 or nb_colonnes <= 0:
        raise ValueError(f"construireGrilleDemineur: Le nombre de lignes ({nb_lignes}) ou de colonnes ({nb_colonnes}) est négatif ou nul")

    grille = []
    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            ligne.append(construireCellule())
        grille.append(ligne)

    return grille

def getNbLignesGrilleDemineur(grille: list) -> int:
    """
    Renvoie ne nombre de lignes de la grille

    :param grille: liste de listes construites avec des cellules
    :return: int (nombre de lignes de la grille)
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur: Le paramètre n’est pas une grille")

    return len(grille)

def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    Renvoie ne nombre de collonnes de la grille

    :param grille: liste de listes construites avec des cellules
    :return: int (nombre de collonnes de la grille)
    """
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonnesGrilleDemineur: Le paramètre n’est pas une grille")

    return len(grille[0])

def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    """
    Renvoie un booléen représentant l'existance ou non d'une cellule aux coordonées données en paramètre

    :param grille: liste de listes construites avec des cellules
    :param coord: coordonées de la cellule
    :return: booléen représentant l'existance ou non d'une cellule aux coordonées données en paramètre
    """
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError("isCoordonneeCorrecte: un des paramètres n’est pas du bon type")

    index_max_grille = (getNbLignesGrilleDemineur(grille)-1, getNbColonnesGrilleDemineur(grille)-1)
    for i in range(2):
        if not coord[i] <= index_max_grille[i] or coord[i] < 0:
            return False

    return True

def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    """
    Renvoie la cellule correspondante aux coordonées "coord"

    :param grille: liste de listes construites avec des cellules
    :param coord: coordonées de la cellule
    :return: dictionnaire reprérentant la cellule
    """
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError("getCelluleGrilleDemineur: un des paramètres n’est pas du bon type")

    elif not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCelluleGrilleDemineur: coordonnée non contenue dans la grille")

    return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    """
    Renvoie le contenu de la cellule située aux coordonées "cord" d'une grille "grille"

    :param grille: Grille dans laquelle se trouve celule que l'on cherche pour extraire le contenu
    :param coord: Coordoées de la cellule dans la grille
    :return: contenu de la cellule (entier)
    """
    return getCelluleGrilleDemineur(grille, coord)["Contenu"]

def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    """
    Change le contenu de la cellule se trouvant aux coordonées "coord" de la grille "grille" par le contenu passé en param

    :param grille: Grille dans laquelle se trouve celule qui nous interesse
    :param coord: Coordoées de la cellule dans la grille
    :param contenu: Nouveau contenu pour la cellule
    """
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)

def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Booléen représentant si la cellule est visible ou non

    :param grille: Grille dans laquelle se trouve celule qui nous interesse
    :param coord: Coordoées de la cellule dans la grille
    :return:
    """
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))

def setVisibleGrilleDemineur(grille: list, coord: tuple, val: bool) -> None:
    """
    Change la valeur de la visibilité de la cellule et mets la valeur de val

    :param grille: Grille dans laquelle se trouve celule qui nous interesse
    :param coord: Coordoées de la cellule dans la grille
    :param val:
    :return:
    """
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), val)

def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Renvoie un booléen reprérentant la présence ou non d'une mine dans une cellule

    :param grille: Grille dans laquelle se trouve celule qui nous interesse
    :param coord: Coordoées de la cellule dans la grille
    :return: "True" si la cellule contient une mine, sinon "False"
    """
    return getContenuGrilleDemineur(grille, coord) == const.ID_MINE


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """
    Renvoie les voisins de la cellule dont les coordonées "coord" sont passé en paramètre

    :param grille: Grille dans laquelle se trouve celule qui nous interesse
    :param coord: Coordoées de la cellule dans la grille
    :return: liste des coordonéesdes des voisins de la cellule
    """
    if not type_grille_demineur(grille) or not type_coordonnee(coord):
        raise TypeError("getCoordonneeVoisinsGrilleDemineur: un des paramètres n’est pas du bon type")
    elif not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCoordonneeVoisinsGrilleDemineur: la coordonnée n’est pas dans la grille")

    coords = [
        (coord[0]-1, coord[1]-1), (coord[0]-1, coord[1]), (coord[0]-1, coord[1]+1),
        (coord[0], coord[1]-1),                           (coord[0], coord[1]+1),
        (coord[0]+1, coord[1]-1), (coord[0]+1, coord[1]), (coord[0]+1, coord[1]+1)
    ]

    resultat = []
    for elt in coords:
        if type_coordonnee(elt) and isCoordonneeCorrecte(grille, elt):
            resultat.append(elt)
    return resultat


def placerMinesGrilleDemineur(grille: list, nb:int, coord: tuple):
    """
    Place nb mine dans une grille "grille"

    :param grille: Grille dans laquelle on veut placer des mines
    :param nb: Nombre de mines à placer
    :param coord: Coordinées de l'emplacement ou il ne peut pas y avoir de mine
    """
    if nb > getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille) - 1 or nb < 0:
        raise ValueError("placerMinesGrilleDemineur: Nombre de bombes à placer incorrect")
    elif not isCoordonneeCorrecte(grille, coord):
        raise IndexError("placerMinesGrilleDemineur: la coordonnée n’est pas dans la grille")

    coord_mines = []
    while len(coord_mines) != nb:
        mine = (randint(0, getNbLignesGrilleDemineur(grille)), randint(0, getNbColonnesGrilleDemineur(grille)))
        if mine != coord and not mine in coord_mines and isCoordonneeCorrecte(grille, mine):
            coord_mines.append(mine)
            cell = getCelluleGrilleDemineur(grille, mine)
            setContenuCellule(cell, const.ID_MINE)

    compterMinesVoisinesGrilleDemineur(grille)



def compterMinesVoisinesGrilleDemineur(grille: list):
    """
    Change la les valeurs des cellules qui ne sont pas des mines par le nombre de mines dans leur voisinage

    :param grille: Liste de liste elle meme composée de cellules
    """
    for i, ligne in enumerate(grille):
        for j, elt in enumerate(ligne):
            if getContenuCellule(elt) != const.ID_MINE:
                nb_mine_voisin = 0
                for coo in getCoordonneeVoisinsGrilleDemineur(grille, (i, j)):
                    if getContenuCellule(getCelluleGrilleDemineur(grille, coo)) == const.ID_MINE:
                        nb_mine_voisin += 1
                setContenuCellule(elt, nb_mine_voisin)


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    Renvoie le nombre de mines dans une grille "grille"

    :param grille: Liste de listes contenant des cellules
    :return: int (nombre de mines)
    """
    if not type_grille_demineur(grille):
        raise ValueError("getNbMinesGrilleDemineur: le paramètre n’est pas une grille")

    mines = 0
    for ligne in grille:
        for elt in ligne:
            if getContenuCellule(elt) == const.ID_MINE:
                mines += 1

    return mines

def getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    """
    Renvoie l'annotation d'une cellule dans une grille "grille" aux coordonées "coord"

    :param grille: Liste de listes contenant des cellules
    :param coord: Coordoées de la cellule dans la grille
    :return: str (annotation)
    """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """
    Renvoie le nombre de mines restantes

    :param grille: Liste de listes contenant des cellules
    :return: int (nombre de mines restantes)
    """
    if not type_grille_demineur(grille):
        raise ValueError("getMinesRestantesGrilleDemineur: le paramètre n’est pas une grille")

    flag = 0
    for ligne in grille:
        for elt in ligne:
            if getAnnotationCellule(elt) == const.FLAG:
                flag += 1

    return getNbMinesGrilleDemineur(grille) - flag

def gagneGrilleDemineur(grille: list):
    """
    Renvoie un booléen qui est True si le joueur a gagné et False sinon

    :param grille: Liste de listes contenant des cellules
    :return:
    """

    if getMinesRestantesGrilleDemineur(grille) != 0:
        return False

    for ligne in grille:
        for elt in ligne:
            if (getContenuCellule(elt) == const.ID_MINE and isVisibleCellule(elt)) or (getContenuCellule(elt) != const.ID_MINE and not isVisibleCellule(elt)):
                return False

    return True

def perduGrilleDemineur(grille: list):
    """
    Renvoie un booléen qui est True si le joueur a perdu et False sinon

    :param grille: Liste de listes contenant des cellules
    :return:
    """

    for ligne in grille:
        for elt in ligne:
            if getContenuCellule(elt) == const.ID_MINE and isVisibleCellule(elt):
                return True

    return False