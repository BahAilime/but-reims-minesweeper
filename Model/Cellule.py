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

def construireCellule(contenu: int = 0, visible: bool = False, annotation: str = None) -> dict:
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
        const.VISIBLE: visible,
        const.ANNOTATION: annotation
    }

def getContenuCellule(cell: dict) -> int:
    """
    Renvoie le contenu d'une cellule

    :param cell: dictionnaire représentant une cellule
    :return: int entre 0 et 8 ou const.ID_MINE
    """
    if not type_cellule(cell):
        raise TypeError("getContenuCellule: Le paramètre n’est pas une cellule.")

    return cell[const.CONTENU]

def isVisibleCellule(cell: dict) -> bool:
    """
    Renvoie un booléen reprérentant la visibilité de la cellule "cell"

    :param cell: dictionnaire représentant une cellule
    :return: bool
    """
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule: Le paramètre n’est pas une cellule.")

    return cell[const.VISIBLE]

def setContenuCellule(cell: dict, contenu: int) -> dict:
    """
    Modifie le contenu de la cellule "cell" avec le contenu "contenu" passé en paramètre

    :param cell: dictionnaire représentant une cellule
    :param contenu: nombre entre 0 et 8 ou const.ID_MINE
    :return: dictionnaire représentant la cellule mise à jour
    """
    if not type_cellule(cell):
        raise TypeError("setContenuCellule: Le premier paramètre n’est pas une cellule.")

    elif type(contenu) != int:
        # Le pdf dit que c'est une ValueError mais le script de test souhaite un TypeError
        raise TypeError(f"setContenuCellule: la valeur du contenu ({contenu}) n’est pas correcte.")

    elif not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule: le contenu {contenu} n’est pas correct")

    cell[const.CONTENU] = contenu
    return cell


def setVisibleCellule(cell: dict, val: bool) -> dict:
    """
    Modifie la visibilité de la cellule "cell" avec la valeur "val" passé en paramètre

    :param cell: dictionnaire représentant une cellule
    :param val: booléen correspondant à la visibilité et qui  modifie  la  visibilité  de  la  cellule "cell"
    :return: dictionnaire représentant la cellule mise à jour
    """
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule: Le premier paramètre n’est pas une cellule")

    elif type(val) != bool:
        raise TypeError(f"setContenuCellule: la valeur du contenu ({val}) n’est pas correcte.")

    cell[const.VISIBLE] = val
    return cell

def contientMineCellule(cell: dict) -> bool:
    """
    Renvoie si la cellule contient une mine ou non

    :param cell: dictionnaire représentant une cellule
    :return: booléen spécifiant si la cellule contient une mine ou non
    """
    if not type_cellule(cell):
        raise TypeError("contientMineCellule: Le paramètre n’est pas une cellule.")

    return cell[const.CONTENU] == const.ID_MINE


def isAnnotationCorrecte(annotation: str) -> bool:
    """
    Verifie si une annotation est valide ou non

    :param annotation: string de l'annotation souhaitée
    :return: bool représentant si l'annotation est valide (True) ou non (False)
    """
    return annotation in (None, const.DOUTE, const.FLAG)


def getAnnotationCellule(cell: dict) -> str:
    """
    Renvoie l'annotation d'une cellule

    :param cell: dictionnaire représentant une cellule
    :return: str (annotation)
    """
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule: Le paramètre {cell} n’est pas une cellule.")

    print(cell)
    if const.ANNOTATION in cell.keys():
        return cell[const.ANNOTATION]
    else:
        return None


def changeAnnotationCellule(cell: dict):
    if not type_cellule(cell):
        raise TypeError("changeAnnotationCellule: le paramètre n’est pas une cellule")

    ordre = (None, const.FLAG, const.DOUTE)
    cell[const.ANNOTATION] = ordre[(ordre.index(cell[const.ANNOTATION])+1)%len(ordre)]

    # Détails:
    #  - ordre.index(cell[const.ANNOTATION] récupère l'index de la position de l'annotation actuelle dans la séquence
    #  - on ajoute 1 pour avoir le suivant
    #  - %len(ordre) sert a éviter les IndexError en fin de séquence