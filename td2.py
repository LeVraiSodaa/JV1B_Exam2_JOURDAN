#1 Écrire la fonction permettant d’afficher la grille de jeu


liste = ["X","O","X","O","X","O",""]

def grille(liste):
    for i in range(1):
        for j in range(3):
            print("|", end = "")
            print(liste[j+1], end ="")
            print("|", end = "O")
            print("|", end = "X")
            print("|", end = "")
            print("\n")

print(grille(liste))


            
#2 Écrire la fonction permettant de jouer un O ou un X.
liste = ["1","2","3","4","5","6","7","8","9"]


def grille(liste,joueur):


    def grille(liste):
        for i in range(1):
            for j in range(3):
                print("|", end = "")
                print(liste[j+0], end ="")
                print("|", end = "")
                print(liste[j+3], end ="")
                print("|", end = "")
                print(liste[j+6], end ="")
                print("|", end = "")
            print("\n")

print(grille(liste))







