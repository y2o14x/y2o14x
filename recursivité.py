# exercice 1

def affiche_tab(T):
    """
    >>> affiche_tab([0, 1, 2])
    0
    1
    2
    """
    if len(T) == 0: return
    #
    print(T[0])
    affiche_tab(T[1:])


def affiche_tab_v2(T, i=0):
    """
    >>> affiche_tab_v2([0, 1, 2])
    0
    1
    2
    """
    if i == len(T): return
    #
    print(T[i])
    affiche_tab_v2(T, i + 1)

# exercice 2

def inversion(T, inverse):
    """
    >>> T = inversion([0, 1, 2])
    >>> T
    [2, 1, 0]
    """
    if len(T) == 0: return inverse
    #
    return inversion(T[1:], [T[0]] + inverse)

def inversion_v2(T, i=0):
    """Inversion en place du tableau
    >>> T = [0, 1, 2, 3, 4]
    >>>inversion_v2(T)
    >>> T
    [4, 3, 2, 1, 0]
    >>> T = [0, 1, 2, 3]
    >>> T
    [3, 2, 1, 0]
    """
    if i == len(T) // 2: return
    #



if __name__ == "__main__":
    import doctest
    doctest.testmod()



