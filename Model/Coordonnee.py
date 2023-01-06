# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(num_ligne: int, num_colonne: int) -> tuple:
    """
    Prends en paramètre les coordonées y puis x et renvoie un tuple de ses coordonées ce sont bien des entiers positifs

    :param num_ligne: Coordonée Y
    :param num_colonne: Coordonée X
    :return: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    """
    if type(num_ligne) == float or type(num_colonne) == float:
        raise TypeError(f"construireCoordonnee: Le numéro de ligne {type(num_ligne)} ou  "
                        f"le  numéro  decolonne {type(num_colonne)} ne  sont pas des entiers")
    elif num_ligne < 0 or num_colonne < 0:
        raise ValueError(f"construireCoordonnee: Le  numéro de ligne {num_ligne} "
                         f"ou de colonne {num_colonne} ne sont pas positifs")
    return (num_ligne, num_colonne)

def getLigneCoordonnee(coord: tuple) -> int:
    """
    Renvoie la valeur Y des coordonées donné en paramètre

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: Y
    """
    if not type_coordonnee(coord):
        raise TypeError("getLigneCoordonnee: Le paramètre n’est pas une coordonnée")

    return coord[0]

def getColonneCoordonnee(coord: tuple) -> int:
    """
    Renvoie la valeur X des coordonées donné en paramètre

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: X
    """
    if not type_coordonnee(coord):
        raise TypeError("getLigneCoordonnee: Le paramètre n’est pas une coordonnée")

    return coord[1]