class Bingo:
    def __init__(self, tab):
        self.matrice = []
        for i in range(5):
            ligne = []
            for j in range(5):
                ligne.append([tab[5*i + j], 0])
            self.matrice.append(ligne)

    def __str__(self):
        stg = ""
        for i in range(5):
            for j in range(5):
                stg += str(self.matrice[i][j][0]) + " "
            stg += "\n"
        return stg[:-1]

    def __getitem__(self, indice):
        return self.matrice[indice]
        
def lecture_grille(nom_fichier):
     """lit un fichier de grille de bingo
     1 ligne fichier = 1 ligne bingo 
     les nombres sont séparés par des espaces
     """
    
    tableau = []
    
    with open(nom_fichier) as fh:
        for ligne in fh:
            ligne = ligne.rstrip()
            tb = ligne.split()
            tb = [int(c) for c in tb]
            tableau.append(tb)
    #
    return tableau

if __name__ == "__main__":
    la_grille = lecture_grille("grille.dat")
    b = Bingo(T)
    print(b)
    print(b[3][4][0])
