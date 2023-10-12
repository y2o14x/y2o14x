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
    n = len(T)
    if i == n // 2: return
    #
    T[i], T[n - 1 - i] = T[n - 1 - i], T[i]
    inversion_v2(T, i + 1)

# exercice 3

def mediane(T):
    """
    >>> T = [0, 1, 2, 3]
    >>> mediane(T)
    1.5
    >>> T = [0, 1, 2, 3, 4]
    >>> mediane(T)
    2 
    """
    n = len(T)
    if n <= 2 : return (T[0] + T[n - 1]) / 2 
    #
    return mediane(T[1:n - 1])
    
# exercice 4

def bin_s(T, e):
    if len(T) == 1: return T[0] == e 
    #
    indice_milieu = len(T) // 2
    milieu = T[indice_milieu]
    if T[milieu] == e: return True
    if T[milieu] < e:
        nv_tab = T[indice_milieu:]
    else:
        nv_tab = T[0:indice_milieu]
    return bin_s(nv_tab, e)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testmod()



