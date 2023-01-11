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

def construireGrilleDemineur9(nb_lignes: int, nb_colonnes: int) -> list:
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

    return [[[construireCellule()] * nb_colonnes] * nb_lignes]

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