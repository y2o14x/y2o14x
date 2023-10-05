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


if __name__ == "__main__":
    T = [i**2 for i in range(25)]
    b = b = Bingo(T)
    print(b[0][2][0])
