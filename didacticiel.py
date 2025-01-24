from os import *#on importe le module OS
system('cls')#on clear le terminale
#affichage du début
print("Bienvenue dans le didacticiel de la bataille navale !")
print("Nous allons t'expliquer les règles et te montrer comment jouer.")
print("Appuie sur Entrée pour continuer.")
input()#attendre l'entrée du joueur
system('cls')#clear le terminale
#affichage affichage des règles du jeu
print("Règles du jeu :")
print("1. Chaque joueur dispose d'une grille pour placer ses bateaux.")
print("2. L'objectif est de couler tous les \
bateaux de l'adversaire en lançant des missiles.")
print("3. Les bateaux doivent être placés horizontalement\
 ou verticalement sans sortir de la grille et sans qu'ils se croisent")
print("4. Une case 'Touché' signale un impact \
sur un bateau, 'Coulé' lorsque le bateau est entièrement détruit.")
#attendre l'entrée du joueur
input("Appuie sur Entrée pour continuer.")
system('cls')#clear le cmd
#afficher les différents bateaux
print("Voici les bateaux disponibles :")
print("- Porte-avion (5 cases)")
print("- Croiseur (4 cases)")
print("- Contre-torpilleur (3 cases)")
print("- Sous-marin (3 cases)")
print("- Torpilleur (2 cases)")
input("Appuie sur Entrée pour continuer.")# attendre l'entrée du joueur
system('cls')#clear le terminale
#montrer comment est fait une grille
print("Chaque grille est composée de \
10 lignes (1-10) et de 10 colonnes (1-10).")
print("Exemple : La case '4-2' correspond à \
la 2ème colonne et la 4ème ligne.")
input("Appuie sur Entrée pour continuer.")#attendre l'entrée du joueur
system('cls')#clear le treminale
#afficher les différentes possibilités
print("voici les différentes possibilitées:")
print("bateau uniquement: █")
print("bateau et missile: X")
print("bateau coulé: O")
print("missile uniquement qui a touché sa cible: *")
print("missile qui a manqué sa cible: ≈")
print("")
print("il y a également un code couleur:")
print("vert: case non touchée")
print("rouge: case adverse touchée")
print("gris: missile manqué ou bateau coulé")
print("")
print("il peut arriver qu'une de tes cases comporte:")
print("un bateau, avec un missile et qui est coulé")
print("tu auras donc un O qui sera affiché, pas\
de panique, le nombre de cases que tu as coulées sera affiché :)")
input("Appuie sur Entrée pour continuer.")#éttendre l'entrée du joueur
system('cls')#clear le terminale
choix = input("veut-tu commencer une partie ?(O/N)")#demander si il 
#veut commencer une partie
if choix == "O":#si son choix est O
    system('python bataille_navale_v8.py')#lancer le fichier principale
    exit()#fermer le progralle
else:#winon
    exit()#juste fermer le programme