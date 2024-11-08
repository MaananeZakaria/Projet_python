
#Code le plus cout possible #affichage simple 

def afficher_plateau(plateau):
    for row in plateau:
        print(" | ".join(row))
        print("-" * 9)

def verifier_victoire(plateau, joueur):
    return any(
        all(plateau[i][j] == joueur for j in range(3)) or
        all(plateau[j][i] == joueur for j in range(3))
        for i in range(3)
    ) or all(plateau[i][i] == joueur for i in range(3)) or all(plateau[i][2-i] == joueur for i in range(3))

def morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur = "X"
    for tour in range(9):
        afficher_plateau(plateau)
        ligne, col = map(int, input(f"Joueur {joueur}, entrez la ligne et la colonne (0-2) : ").split())
        if plateau[ligne][col] != " ":
            print("Case déjà prise ! Essayez à nouveau.")
            continue
        plateau[ligne][col] = joueur
        if verifier_victoire(plateau, joueur):
            afficher_plateau(plateau)
            print(f"Le joueur {joueur} gagne !")
            return
        joueur = "O" if joueur == "X" else "X"
    afficher_plateau(plateau)
    print("Match nul !")

morpion()
