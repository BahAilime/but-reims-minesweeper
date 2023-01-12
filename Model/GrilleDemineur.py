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
        print(grille)
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