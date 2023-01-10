# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(nb: int) -> bool:
    """
    Vérifie que nb est bien un entier et qu'il est bien une valeure possible pour une cell

    :param nb: La valeure qu'on test
    :return: "True" si nb est une valeure possible, sinon "False"
    """
    if type(nb) != int:
        return False
    return nb == const.ID_MINE or (nb >= 0 and nb <= 8)

def construireCellule(contenu: int = 0, visible: bool = False) -> dict:
    """
    Contruit une cellule à partir des deux paramètres

    :param contenu: entier entre 0 et 8 ou const.ID_MINE représentant le nombre de mines dans le voisinage
    :param visible: booléen qui  vaut "True" si  la  cellule est «découverte» (ou visible), "False" sinon.
    :return: Cellule
    """
    if not isContenuCorrect(contenu):
        raise ValueError(f"construireCellule: le contenu {contenu} n’est pas correct")

    if not type(visible) == bool:
        raise TypeError(f"construireCellule: le  second paramètre ({type(visible)}) n’est pas un booléen")

    return {
        const.CONTENU: contenu,
        const.VISIBLE: visible
    }

def getContenuCellule(cell: dict) -> int:
    if not type_cellule(cell):
        raise TypeError("getContenuCellule: Le paramètre n’est pas une cellule.")

    return cell["Contenu"]

def isVisibleCellule(cell: dict) -> int:
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule: Le paramètre n’est pas une cellule.")

    return cell["Visible"]

def setContenuCellule(cell: dict, contenu: int) -> dict:
    if not type_cellule(cell):
        raise TypeError("setContenuCellule: Le premier paramètre n’est pas une cellule.")

    elif type(contenu) != int:
        # Le pdf dit que c'est une ValueError mais le script de test souhaite un TypeError
        raise TypeError(f"setContenuCellule: la valeur du contenu ({contenu}) n’est pas correcte.")

    elif not isContenuCorrect(contenu):
        print(cell)
        raise ValueError(f"setContenuCellule: le contenu {contenu} n’est pas correct")

    cell["Contenu"] = contenu
    return cell


def setVisibleCellule(cell: dict, val: bool) -> dict:
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule: Le premier paramètre n’est pas une cellule")

    elif type(val) != bool:
        raise TypeError(f"setContenuCellule: la valeur du contenu ({val}) n’est pas correcte.")

    cell["Visible"] = val
    return cell

def contientMineCellule(cell: dict) -> bool:
    if not type_cellule(cell):
        raise TypeError("contientMineCellule: Le paramètre n’est pas une cellule.")

    return cell["Contenu"] == const.ID_MINE

print(getContenuCellule(construireCellule(7, False)))
