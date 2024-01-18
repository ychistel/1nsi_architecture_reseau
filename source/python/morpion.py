# --------------------------------------
# Fonctions
# --------------------------------------

def saisir(j):
    print(f"Joueur {j} joue")
    c = int(input("Quelle case joues-tu ? "))
    if 1 <= c <= 9:
        return c
    else:
        return 0

def completer_grille(grille,j,c):
    if j == 1 and grille[c-1] != 'O':
        grille[c-1] = 'X'
    elif j == 2 and grille[c-1] != 'X':
        grille[c-1] = 'O'
    return grille
        
def gagner_partie(grille):
    if (grille[0] == grille[1] == grille[2]) or\
       (grille[3] == grille[4] == grille[5]) or\
       (grille[6] == grille[7] == grille[8]) or\
       (grille[0] == grille[3] == grille[6]) or\
       (grille[1] == grille[4] == grille[7]) or\
       (grille[2] == grille[5] == grille[8]) or\
       (grille[0] == grille[4] == grille[8]) or\
       (grille[2] == grille[4] == grille[6]):
        return True
    else:
        return False
    
def fin_partie(grille):
    coups_a_jouer = 0
    for i in range(len(grille)):
        if grille[i] != 'X' and grille[i] != 'O':
            coups_a_jouer = coups_a_jouer + 1
    if coups_a_jouer < 1:
        return True
    else:
        return False

def changer(j):
    if j == 1:
        return 2
    else:
        return 1
    
def afficher_grille(grille,joueur,gagnant,fin):
    print("on affiche la grille ",grille)
    aff = f"+---+---+---+\n"
    if grille[6] == 'X' or grille[6] == 'O':
        aff += f"| {grille[6]} "
    else:
        aff += f"|   "
    if grille[7] == 'X' or grille[7] == 'O':
        aff += f"| {grille[7]} "
    else:
        aff += f"|   "
    if grille[8] == 'X' or grille[8] == 'O':
        aff += f"| {grille[8]} |\n"
    else:
        aff += f"|   |\n"
    aff += "+---+---+---+\n"
    if grille[3] == 'X' or grille[3] == 'O':
        aff += f"| {grille[3]} "
    else:
        aff += f"|   "
    if grille[4] == 'X' or grille[4] == 'O':
        aff += f"| {grille[4]} "
    else:
        aff += f"|   "
    if grille[5] == 'X' or grille[5] == 'O':
        aff +=f"| {grille[5]} |\n"
    else:
        aff +=f"|   |\n"
    aff += "+---+---+---+\n"
    if grille[0] == 'X' or grille[0] == 'O':
        aff += f"| {grille[0]} "
    else:
        aff += f"|   "
    if grille[1] == 'X' or grille[1] == 'O':
        aff +=f"| {grille[1]} "
    else:
        aff += f"|   "
    if grille[2] == 'X' or grille[2] == 'O':
        aff += f"| {grille[2]} |\n"
    else:
        aff += f"|   |\n"
    aff += "+---+---+---+\n"
    return aff

def jeu():
    # --------------------------------------
    # Variables
    # --------------------------------------
    grille = [1,2,3,4,5,6,7,8,9]
    joueur = 1
    fin = False
    gagnant = False


    # --------------------------------------
    # Programme principal
    # --------------------------------------

    print("Début de partie")
    print(afficher_grille(grille,joueur,gagnant,fin))

    while not(fin) and not(gagnant):
        choix = saisir(joueur)
        if choix in grille and not(gagnant) and not(fin):
            grille = completer_grille(grille,joueur,choix)
            gagnant = gagner_partie(grille)
            fin = fin_partie(grille)
            if not(gagnant):
                joueur = changer(joueur)
            else:
                print(f"Le joueur {joueur} a gagné !")
            if fin:
                print(f"Fin de partie, pas de gagnant !")
            print(afficher_grille(grille,joueur,gagnant,fin))


if __name__ == '__main__':
    jeu()