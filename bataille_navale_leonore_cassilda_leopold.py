# Créé par CASSILDA.LESNE, le 21/01/2025 en Python 3.7

# Fonctions nécessaires au fonctionnement du programme

from time import sleep#on importe la fonction sleep depuis time
from os import system #on importe system depuis os


def choix_joueur(entier,couleurs):#définition de choix_joueu
    """
    rôle : assigner un nom et une couleur d'affichage pour le joueur
    entrée : un entier qui sert a afficher "Joueur X" de type int, un
    dictionnaire avec le nom des couleurs pour clef et le code ANSI assigné
    à chacune de ses couleurs pour valeur de type dict[str : str]
    sortie : un tuple pour le nom du joueur 
    et la couleur choisie par le joueur
    """
    #on définit une fonction pour la personalisation du gameplay
    couleur_joueur=0#on déclare la variable
    print("Joueur",entier) #quel est le joueur (1 ou 2)
    nom_joueur=input("insérez votre nom d'utilisateur: ")
    #on demande le nom d'utilisateur
    print("Joueur",entier)#on affiche le numéro du joueur
    while couleur_joueur not in couleurs:#tant que la couleur rentrée
        #n'est pas valide
        couleur_joueur=input("insérez votre couleur d'affichage\
(bleu, jaune, vert, violet, blanc, cyan): ")
        #on demande la couleur 
    return (nom_joueur, couleurs[couleur_joueur]) 
#on renvoit un tuple, 1 pour chaque joueur


def valide_entree_joueur_int(saisie_joueur_nb, liste_entrees_valides_nb):
    #on définit une fonction qui valide
    '''
    entree : str
    rôle : valider ou non l'entrée du joueur
    sortie : str
    '''
    # on définit une variable valeur_nb qui demande au joueur d'entrer un
    # nombre entre 1 et 10
    valeur_nb = input(saisie_joueur_nb)
    # tant que la valeur entrée par le joueur n'est pas dans
    #  liste_entrees_valides
    while valeur_nb not in liste_entrees_valides_nb :
        # on affiche un message d'erreur
        print("Entrée invalide. Réessayez.")
        # la variable valeur_nb demande au joueur d'entrer un nombre entre
        # 0 et 10
        valeur_nb = input(saisie_joueur_nb)
    # on retourne la variable valeur_nb
    return valeur_nb

def valide_entree_joueur_str(saisie_joueur_caractere,
 liste_entrees_valides_caractere) :
    '''
    entrée : saisie_joueur_caractere qui est le texte qu'on affiche afin de
    dermander d'entrer le nom du bateau au joueur, de type str, et
    liste_entrees_valides_caracteres de type list(str) qui permet 
    de vérfier si
    l'entrée du joueur est bien comprise dans cette liste, et donc valide
    rôle : vérifier si le joueur entre bien une entrée valide concernant les
    chaînes de caractère comme les bateaux ou les directions
    sortie : le nom de l'entrée, de type str
    '''
    # on initialise valeur_caractere en demandant au joueur 
    # d'entrer une chaîne
    # de caractères
    valeur_caractere = input(saisie_joueur_caractere)
    # tant que valeur_caracteres n'est pas dans la liste des caractères
    while valeur_caractere not in liste_entrees_valides_caractere :
        # on affiche un message d'erreur
        print("Entrée invalide. Réessayez.")
        # on initialise valeur_caractere en demandant au joueur d'entrer
        # une chaîne de caractères
        valeur_caractere = input(saisie_joueur_caractere)
    # on retourne valeur_caractere
    return valeur_caractere


def choix_joueur_X(stock):
    '''
    entrée : le stock de bateau de chaque joueur
    rôle : permettre au joueur de choisir son bateau
    sortie : le nom du bateau, le poin d'application puis le sens
    '''
      
    retour_liste=[]#on définit une liste vide
    print("Liste des bateaux disponibles :", liste_bateau)
    #on affiche les bateaux
    choix_bateau = \
        input("Veuillez choisir un bateau parmi la liste ci-dessus : ")
        #on demande au joueur de choisir
    while choix_bateau not in liste_bateau or stock[choix_bateau] < 1:
        #tant que le bateau est invalide ou inutilisable
        if choix_bateau not in liste_bateau:#si il n'existe pas
            print("Erreur : ce bateau n'existe pas.")#afficher une erreur
        else:#sinon
            print(f"Vous n'avez plus de {choix_bateau}.")#dire qu'il n'y 
            #a plus de tel bateau
        choix_bateau = \
        input("Veuillez choisir un autre bateau parmi la liste ci-dessus : ")
        #on redemande le bateau
    stock[choix_bateau] -= 1#une fois que c'est validé: on décrémente de 1

    ligne = int(input("Veuillez choisir une ligne (1-10) : "))
    #on demande la ligne
    while ligne <= 0 or ligne > 10:#tant qu'elle est inférieure à 0 ou 10
        print("Erreur : numéro de ligne invalide.")#afficher l'erreur
        ligne = int(input("Veuillez choisir une ligne (1-10) : "))
        #redemander la ligne

    colonne = int(input("Veuillez choisir une colonne (1-10) : "))
    #on demande ensuite la colonne
    while colonne <= 0 or colonne > 10:#tant qu'elle est inférieure à 0
        #ou supérieure à 10 
        print("Erreur : numéro de colonne invalide.")#affiche l'erreur
        colonne = int(input("Veuillez choisir une colonne (1-10) : "))
        #redemander 

    direction = \
        input("Veuillez choisir une direction (haut, bas, gauche, droite) : ")
        #on demande la directoion
    while direction not in liste_direction:#tant qu'elle n'est pas valide
        print("Erreur : direction invalide.")#afficher l'erreur
        direction = \
        input("Veuillez choisir une direction (haut, bas, gauche, droite) : ")
        #redemander
    retour_liste=[choix_bateau, ligne, colonne, direction]
    #on return une liste et non un tuple car si le joueur 
    # se trompe, on doit pouvoir modifier les valeurs
    return retour_liste


def choix_missile_j(grille_joueur, grille_joueur_adverse, pieces):
    '''
    Entrée : grille_joueur (list), grille_joueur_adverse (list), pieces (dict)
    Rôle : Permet au joueur de choisir où placer un missile sur la grille.
    Sortie : bool (True si un bateau a été touché, False sinon)
    '''
    # Initialisation de la variable "touche"
    touche = False

    # Demande à l'utilisateur de choisir une ligne pour placer le missile
    ligne_missile = valide_entree_joueur_int\
        ("Veuillez choisir une ligne (1-10) : ", liste_colonne_ligne)
        #demander la ligne du missile
    ligne_missile = int(ligne_missile)  # Conversion en entier

    # Demande à l'utilisateur de choisir une colonne pour placer le missile
    colonne_missile = valide_entree_joueur_int\
        ("Veuillez choisir une colonne (1-10) : ", liste_colonne_ligne)
        #demander la ligne du missile
    colonne_missile = int(colonne_missile)  # Conversion en entier

    # Vérifie si un missile a déjà été placé sur les coordonnées choisies
    verif_deja_missile\
        (grille_joueur, grille_joueur_adverse,\
          ligne_missile, colonne_missile, pieces)

    # Vérification des cas possibles en fonction du contenu des grilles
    case_adverse = grille_joueur_adverse[ligne_missile][colonne_missile]
    case_joueur = grille_joueur[ligne_missile][colonne_missile]

    # Si un bateau adverse est touché et que le joueur
    #  n'a pas de bateau à cette position
    if case_adverse == pieces["caractere_bateau"] and case_joueur != \
        pieces["caractere_bateau"]:
        grille_joueur[ligne_missile][colonne_missile] = \
            pieces["caractere_missile"]
        grille_joueur_adverse[ligne_missile][colonne_missile] = \
            pieces["caractere_bateau_coule"]
        touche = True

    # Si un bateau adverse est touché à un endroit où le 
    # joueur a aussi un bateau
    elif case_adverse == pieces["caractere_bateau"] and \
        case_joueur == pieces["caractere_bateau"]:
        grille_joueur[ligne_missile][colonne_missile] = \
            pieces["caractere_bateau_plus_missile"]
        grille_joueur_adverse[ligne_missile][colonne_missile] =\
            pieces["caractere_bateau_coule"]
        touche = True

    # Si un bateau déjà touché avec un missile est retouché
    elif case_adverse == pieces["caractere_bateau_plus_missile"] \
        and case_joueur not in [
        pieces["caractere_bateau_plus_missile"],
        pieces["caractere_missile"],
        pieces["caractere_missile_manque"]
    ]:
        grille_joueur[ligne_missile][colonne_missile] = (
            pieces["caractere_bateau_plus_missile"] if case_joueur == \
                pieces["caractere_bateau"]
            else pieces["caractere_missile"]
        )
        touche = True#on réasigne touche

    # Si la case adverse n'a pas de bateau mais que le joueur en a un
    elif case_adverse != pieces["caractere_bateau"] and case_joueur == \
        pieces["caractere_bateau"]:
        grille_joueur[ligne_missile][colonne_missile] = \
            pieces["caractere_bateau_plus_missile"]

    # Si aucun bateau n'est touché
    else:
        grille_joueur[ligne_missile][colonne_missile] = \
            pieces["caractere_missile_manque"]

    return touche#on retourne touche


def verif_deja_missile\
(grille_joueur, grille_joueur_adverse, ligne_missile, colonne_missile, pieces):
#déclaration de la fonction
    """
    Vérifie si un missile a déjà été placé sur les coordonnées données.
    Si un missile est déjà présent, demande à 
    l'utilisateur de choisir une autre case.

    Entrées :
        - grille_joueur (list) : La grille du joueur.
        - grille_joueur_adverse (list) : La grille de l'adversaire.
        - ligne_missile (int) : La ligne choisie pour placer le missile.
        - colonne_missile (int) : La colonne choisie pour placer le missile.
        - pieces (dict) : Dictionnaire 
        des caractères utilisés pour les éléments du jeu.

    Sortie :
        - Retourne un appel à la fonction choix_missile_j
          avec des coordonnées valides.
    """
    # Boucle tant que la case choisie contient un missile 
    # #ou un élément interdit
    while grille_joueur[ligne_missile][colonne_missile] not in (
        " ",  # Case vide
        pieces["caractere_bateau"],  # Case avec un bateau
        pieces["caractere_bateau_coule"]  # Case où un bateau a déjà été coulé
    ):
        print("Il y a déjà un missile ici. Veuillez choisir une autre case.")
        #afficher message d'erreur
        return choix_missile_j(grille_joueur, grille_joueur_adverse, pieces)  
    # Re-demande un choix valide

    # Si la case est valide, continue l'exécution

def verif_bateau_joueur_X(tuple_joueur, grille_joueur, stock_bateaux_j_X):
    choix_bateau, ligne, colonne, direction = tuple_joueur
    taille_bateau = case_pour_chaque_bateau[choix_bateau]

    # Dictionnaire pour gérer les directions
    decalage = {
        "haut": (-1, 0),
        "bas": (1, 0),
        "gauche": (0, -1),
        "droite": (0, 1)
    }

    decalage_x, decalage_y = decalage.get(direction, (0, 0))
    #on assigne plusieurs variables en fonction de la direction

    for i in range(taille_bateau):#autant de boucle que de cases a placer
        nouvelle_ligne = ligne + i * decalage_x#on déclare une variable
        nouvelle_colonne = colonne + i * decalage_y#on déclare une variable

        # Vérifie si les coordonnées sont hors des limites
        if (
            nouvelle_ligne < 0 or nouvelle_ligne >= len(grille_joueur) or
            nouvelle_colonne < 0 or nouvelle_colonne >= len(grille_joueur[0])
        ):#si la ligne ou la colonne est invalide 
            print(f"Erreur : emplacement hors des limites \
({nouvelle_ligne}, {nouvelle_colonne}).")#afficher un message d'erreur
            stock_bateaux_j_X[choix_bateau] += 1#comme erreur, remettre
            #à disposition les bateaux
            return False#renvoyer false

        # Vérifie si la case est occupée
        if grille_joueur[nouvelle_ligne][nouvelle_colonne] != " ":#si 
            #ce n'est as un espace
            print\
(f"Erreur : case occupée à ({nouvelle_ligne}, {nouvelle_colonne}).")
#afficher le message d'erreur
            stock_bateaux_j_X[choix_bateau] += 1
            #comme erreur, remettre
            #à disposition les bateaux
            return False#retourner false

    return True#renvoyer true


def place_bateau_joueur_X(tuple_joueur, grille_joueur, data, grille_adverse):
    """
    Place un bateau sur la grille du joueur en fonction des 
    coordonnées et de la direction fournies.

    Entrées :
        - tuple_joueur (tuple) : Contient (choix_bateau, 
        ligne, colonne, direction).
        - grille_joueur (list) : Grille actuelle du joueur.
        - data (dict) : Données supplémentaires pour 
        l'affichage (paramètres divers).
        - grille_adverse (list) : Grille de l'adversaire
          (utile pour l'affichage).

    Sortie :
        - bool : Retourne True après avoir placé le bateau.
    """
    choix_bateau, ligne, colonne, direction = tuple_joueur#assignaiton de 
    #plusieurs variables en fonction du tuple
    taille_bateau = case_pour_chaque_bateau[choix_bateau]
    #assigner la taille du bateau

    # Récupère le caractère représentant un bateau
    caractere_bateau = dico_pieces["caractere_bateau"]

    # Dictionnaire des décalages en fonction de la direction
    decalage = {
        "haut": (-1, 0),
        "bas": (1, 0),
        "gauche": (0, -1),
        "droite": (0, 1)
    }

    # Vérifie que la direction est valide
    if direction not in decalage:
        print("Direction invalide !")
        return False

    # Déplacement à appliquer pour chaque itération
    decalage_x, decalage_y = decalage[direction]

    # Placement du bateau sur la grille
    for i in range(taille_bateau):
        nouvelle_ligne = ligne + i * decalage_x#chaque ligne en fonction de dx
        nouvelle_colonne = colonne + i * decalage_y#idem pour du
        grille_joueur[nouvelle_ligne][nouvelle_colonne] = caractere_bateau
        #modification de la grille

    # Affichage de la grille après le placement
    affiche(grille_joueur, data, grille_adverse)#affichage de la grille
    print("Bateau placé avec succès.")#message de confirmation
    return True#on renvoi true



def change_joueur(data):
    """
    Change de joueur en affichant le nom du joueur actuel et en 
    attendant une entrée de l'utilisateur.

    Entrée :
        - data (tuple) : Contient des informations sur le joueur 
        actuel, dont le nom à afficher.

    Sortie :
        - Retourne 0 après avoir affiché le nom 
        du joueur et attendu une entrée.
    """
    # Change la couleur de texte dans le terminal (vert ici)
    system("color a")

    # Efface le texte précédent du terminal
    system('cls')

    # Affiche le nom du joueur actuel
    print(data[0])

    # Demande à l'utilisateur de presser une touche pour continuer
    input("Appuyez sur 'Entrée' pour jouer...")

    # Retourne 0 pour marquer la fin de la fonction
    return 0


def anim_manque_touche_ou_coule():
    """
    Affiche une animation de temporisation avant d'annoncer 
    la réussite ou l'échec.
    L'animation consiste en l'affichage d'un "_" 
    qui clignote à l'écran pendant quelques secondes.
    """
    # On répète l'animation 3 fois
    for _ in range(3):
        # Efface le terminal et affiche "_"
        system('cls')#on efface tout
        print("_")#on affiche "_"
        sleep(0.3)#on attend 0.3 sec

        # Efface à nouveau et montre "_"
        system('cls')
        print("_")
        sleep(0.3)

    return 0#on renvoir un résultat nul (sans importance)








# Fonction pour afficher la grille de jeu
def affiche(grille, data, grille_adverse):#une fonction qui affiche 
    #la grille avec la couleur récupérée dans le tuple
    system("cls")#on efface le texte de l'invite de commande
    couleur_grille=data[1]#on initialise une couleur par 
    #défaut pour l'affichage, la couleur est modifiée pendant le programme 
    pieces=dico_pieces#copie du dictionnaire pieces
    couleurs=dico_couleur#copie du dictionnaire couleurs
    for rang_i, ligne in enumerate(grille):#on parcours la matrice
         ligne_a_afficher = '|'  # Séparateur des colonnes
         for rang_j, pion in enumerate(ligne):#on parcours la matrice
            if pion ==  pieces["caractere_bateau"]:#si c'est un bateau
                    ligne_a_afficher += f"{couleurs["vert"]}{pion}\
{couleur_grille}|"  #on affiche en vert le bateau

            elif pion == pieces["caractere_missile"] :
                    #si le missile touche un bateau
                    ligne_a_afficher += f"{couleurs["rouge"]}\
{pion}{couleur_grille}|" #on l'affiche en rouge

            elif (pion == pieces["caractere_bateau_plus_missile"] 
            #si c'est un "X"
                  and grille_adverse[rang_i][rang_j]\
                    ==pieces["caractere_bateau_coule"]):
                    #et que case coulée pour l'adversaire
                    ligne_a_afficher += f"{couleurs["rouge"]}\
{pion}{couleur_grille}|"#on affiche en rouge

            elif (pion == pieces["caractere_bateau_plus_missile"] and
                   grille_adverse[rang_i][rang_j]!=pieces["caractere_bateau"]):
                    #si missile sur bateau et pas touché
                    ligne_a_afficher += f"{couleurs["gris"]}\
{pion}{couleur_grille}|" #affichage en gris

            elif pion == pieces["caractere_missile_manque"]:
                    #si le missile est manqué
                    ligne_a_afficher += f"{couleurs["gris"]}\
{pion}{couleur_grille}|"#affichage en gris

            elif (pion == pieces["caractere_bateau_coule"] and 
                  grille_adverse[rang_i][rang_j]==\
                    pieces["caractere_bateau_coule"]):
                    #si 2 cases coulées (joueur et adversaire)
                     ligne_a_afficher += f"{couleurs["rouge"]}\
{pion}{couleur_grille}|"#afficher en rouge

            elif (pion == pieces["caractere_bateau_coule"] and 
                  grille_adverse[rang_i][rang_j]!=\
                    pieces["caractere_bateau_coule"]):
                  #si bateau coule que pour jouer
                     ligne_a_afficher += f"{couleurs["gris"]}\
{pion}{couleur_grille}|"  #afficher en gris

            else:#sinon
                 ligne_a_afficher += f"{pion}{couleur_grille}|"#afficher carac
         print(ligne_a_afficher)#afficher la ligne finale
 
    print("\nJoueur actuel:", data[0])#afficher le nom du joueur
    return 0#renvoyer 0

# Fonction pour changer de joueur
def change_joueur(data):#fonction pour changer de joueur
    """
    Affiche le nom du joueur et attend qu'il appuie sur 
    une touche pour continuer.

    Args:
        data (tuple): Les données du joueur, incluant son nom et ses couleurs.

    Returns:
        int: Retourne 0 après l'attente de l'entrée de l'utilisateur.
    """
    system("color a")#mettre la couleur du texte en vert
    system('cls')#clear le terminal
    print(data[0])  # Affiche le nom du joueur
    input("Appuyez sur une touche puis Entrée pour jouer:")#confirmer
    return 0#rnevoyer 0





# Programme principal (en réalité une fonction) ----------------------------

# Cette fonction principale gère le déroulement du jeu, dep
# uis l'initialisation des grilles des joueurs
# jusqu'à la boucle de jeu, alternant entre les joueurs et mettant à 
# jour les grilles à chaque tour.
# Elle inclut les étapes suivantes :
# 1. Initialisation des grilles de jeu pour les joueurs 1 et 2.
# 2. Choix des joueurs pour définir leur nom et couleur.
# 3. Placement des bateaux pour chaque joueur avec affichage du nombre 
# de bateaux restants.
# 4. Alternance entre les joueurs pour tirer des missiles et tenter de 
# couler les bateaux de l'adversaire.
# 5. Affichage du gagnant lorsqu'un joueur a coulé 17 cases.

def prog_principal():

      """
    Fonction principale du jeu 
    qui orchestre l'ensemble du déroulement de la partie.
    - Initialise les grilles des joueurs.
    - Permet aux joueurs de choisir leur nom et couleur.
    - Place les bateaux sur la grille pour chaque joueur.
    - Gère les tours de jeu où les joueurs tirent des missiles
      pour couler les bateaux adverses.
    - Affiche les scores et le gagnant lorsqu'un joueur a coulé 
    tous les bateaux de l'autre.
        """
system('cls')#commencer par effacer tout texte
    # Initialisation des grilles des joueurs
grille_joueur_1 = [["  ","1","2","3","4","5","6","7","8","9","10"],   
        ["1 "," "," "," "," "," "," "," "," "," "," "],
        ["2 "," "," "," "," "," "," "," "," "," "," "],
        ["3 "," "," "," "," "," "," "," "," "," "," "],
        ["4 "," "," "," "," "," "," "," "," "," "," "],
        ["5 "," "," "," "," "," "," "," "," "," "," "],
        ["6 "," "," "," "," "," "," "," "," "," "," "],
        ["7 "," "," "," "," "," "," "," "," "," "," "],
        ["8 "," "," "," "," "," "," "," "," "," "," "],
        ["9 "," "," "," "," "," "," "," "," "," "," "],
        ["10"," "," "," "," "," "," "," "," "," "," "]]

#initialisation grille joueur 2
grille_joueur_2 = [["  ","1","2","3","4","5","6","7","8","9","10"],    
        ["1 "," "," "," "," "," "," "," "," "," "," "],
        ["2 "," "," "," "," "," "," "," "," "," "," "],
        ["3 "," "," "," "," "," "," "," "," "," "," "],
        ["4 "," "," "," "," "," "," "," "," "," "," "],
        ["5 "," "," "," "," "," "," "," "," "," "," "],
        ["6 "," "," "," "," "," "," "," "," "," "," "],
        ["7 "," "," "," "," "," "," "," "," "," "," "],
        ["8 "," "," "," "," "," "," "," "," "," "," "],
        ["9 "," "," "," "," "," "," "," "," "," "," "],
        ["10"," "," "," "," "," "," "," "," "," "," "]]

    # victoire (1 variable par joueur), si e=une vaut 17, alors victoire
victoire_1 = 0
victoire_2 = 0
nom_gagnant = ""#déclaration de nom gagnant
# Dictionnaires et variables de configuration

case_pour_chaque_bateau = {#dictionnaire du nombre de cases par bateau
    "porte-avion": 5, "croiseur": 4,
    "contre-torpilleur": 3, "sous-marin": 3, "torpilleur": 2
}

#nombre de bateaux en stock par joueur
stock_bateaux_j1 = {"porte-avion" : 1, "croiseur" : 1, \
    "contre-torpilleur" : 1, "sous-marin" : 1, "torpilleur" : 1}
stock_bateaux_j2 = {"porte-avion" : 1, "croiseur" : 1, \
    "contre-torpilleur" : 1, "sous-marin" : 1, "torpilleur" : 1}

#liste des bateaux disponibles
liste_bateau = ["porte-avion", "croiseur",\
     "contre-torpilleur", "sous-marin", "torpilleur"]

liste_colonne_ligne = []#déclaration d'une liste vide
for nombre in range(10):#chaque nombre de 1 à 10 (voire suite du code)
    liste_colonne_ligne.append(nombre+1)#on ajoute tel nombre

liste_direction = ["haut", "bas", "gauche", "droite"]#liste des directions

dico_pieces = {}#dictionnaire sur toutes les pièces disponibles
dico_pieces["caractere_bateau"] = "█"
dico_pieces["caractere_bateau_plus_missile"] = "X"
dico_pieces["caractere_bateau_coule"] = "O"
dico_pieces["caractere_missile"] = "*"
dico_pieces["caractere_missile_manque"] = "≈"

# Dictionnaire des couleurs ANSI pour l'affichage
dico_couleur = {
    "noir": "\033[30m", "rouge": "\033[31m", "vert": "\033[32m",
    "jaune": "\033[33m", "bleu": "\033[34m", "violet": "\033[35m",
    "cyan": "\033[36m", "blanc": "\033[37m", "gris": "\033[38;5;240m",
    "reset": "\033[0m"
}
    # Choix des joueurs
data_joueur_1 = choix_joueur(1, dico_couleur)
data_joueur_2 = choix_joueur(2, dico_couleur)


    # Placement des bateaux pour le joueur 1
bateau_restant = True#on initialise a true
while bateau_restant:#tant que c'est vrai 
    for placement in liste_bateau:#placement bateau joueur 1
        if stock_bateaux_j1[placement] == 1:#si il y a toujours des bateaux
             bateau_restant = True#alors true
        else: #sinon
             bateau_restant = False#alors false
    if bateau_restant :#si c'est true:
        affiche(grille_joueur_1, data_joueur_1, grille_joueur_2)
        #afficher la grille
        bateau_joueur_1 = choix_joueur_X(stock_bateaux_j1)
        #demander au joueur
        if verif_bateau_joueur_X\
            (bateau_joueur_1, grille_joueur_1, stock_bateaux_j1)==True:
            #vérifier si c'est bon 
        #bateau_joueur_2=choix_joueur_X(grille_joueur_2)
            place_bateau_joueur_X(bateau_joueur_1, grille_joueur_1, \
                data_joueur_1, grille_joueur_2)
                #placer le bateau

bateau_restant = True#reinitialiser bateau restant 
while bateau_restant:#tant que c'est vrai 
    for placement in liste_bateau:#placement bateau joueur 1
        if stock_bateaux_j2[placement] == 1:#si il reste au moin 1 bateau
             bateau_restant = True#alors true
        else: #sinon 
             bateau_restant = False#alors false
    if bateau_restant:#si il reste un bateau(au moin)
        affiche(grille_joueur_2, data_joueur_2, grille_joueur_1)#afficher 
        #la grille
        bateau_joueur_2 = choix_joueur_X(stock_bateaux_j2)
        #demander au joueur de placer son bateau
        if verif_bateau_joueur_X\
            (bateau_joueur_2, grille_joueur_2, stock_bateaux_j2)==True:
            #si verif = true
            place_bateau_joueur_X(bateau_joueur_2, grille_joueur_2,\
                 data_joueur_2, grille_joueur_1)
            #placer le bateau
# Boucle de jeu : alternance entre les joueurs jusqu'à victoire
while victoire_1 < 17 and victoire_2 < 17:
        # Tour du joueur 1
        change_joueur(data_joueur_1)#on change de joueur
        affiche(grille_joueur_1, data_joueur_1, grille_joueur_2)#on affiche 
        #sa grille
        print(f"{victoire_1} cases coulées sur 17")
        #on affiche le nombre de cases coulées

        if choix_missile_j(grille_joueur_1, grille_joueur_2, dico_pieces):
            #si il a touché une case adverse
            victoire_1 += 1#s'incrémente de 1
            print("Touché, bien joué !")#complimenter joueur
        else:#sinon 
            print("Manqué, dommage...")#l'encourage
        sleep(2)#attenrdre 2 sec

        anim_manque_touche_ou_coule()  
        # Animation avant de passer au joueur suivant

        # Tour du joueur 2
        change_joueur(data_joueur_2)#on change de joueur
        affiche(grille_joueur_2, data_joueur_2, grille_joueur_1)#on affiche 
        #sa grille
        print(f"{victoire_2} cases coulées sur 17")
    #on affiche le nombre de cases coulées
        if choix_missile_j(grille_joueur_2, grille_joueur_1, dico_pieces):
            #si il a touché une case adverse
            victoire_2 += 1#s'incrémente de 1
            print("Touché, bien joué !")#complimenter joueur
        else:#sinon 
            print("Manqué, dommage...")#l'encourage
        sleep(2)#attenrdre 2 sec

        anim_manque_touche_ou_coule()  
        # Animation avant de passer au joueur suivant

     # Fin de la partie : annonce du gagnant
        if victoire_1 == 17 or victoire_2 == 17:#si un joueur a gagné
            if victoire_1 > victoire_2:#hyp 1: c'est la joueur 1
                nom_gagnant = data_joueur_1[0]#assignation nom gagnant
            elif victoire_2 > victoire_1:#hyp 2: c'est le joueur 2
                nom_gagnant = data_joueur_2[0]#assignation nom gagnant 
            print("GAGNANT:")#afficher
            print("#" * (len(nom_gagnant) * 3))#des "#"
            print(" " * (len(nom_gagnant)) + nom_gagnant)#puis le nom 
            print("#" * (len(nom_gagnant) * 3))#puis des "#""
            print("Félicitations à toi, veux-tu refaire une partie ?(O/N)")
            #demander si il veut refaire une partie
            choix = input()#prendre son choix
            if choix == "O":#si il le veut
                system('python bataille_navale_v8.py')#relancer le script
            # Demander à l'utilisateur s'il veut recommencer
            
# Lancer le jeu si ce script est exécuté directement.
# Cela permet d'exécuter la fonction prog_principal() 
# uniquement lorsque ce fichier est le programme principal.
# Si ce fichier est importé comme module dans un autre 
# programme, cette ligne ne sera pas exécutée.

if __name__ == "__prog_principal__":
    prog_principal()#appel du programme  principale

# NB : séparer les fonctions du fichier principal + 
# faire une documentation sur l'utilisation du "jeu" de bataille navale -----
# + faire en sorte de respecter la PEP8 
# (au niveau de la taille des différentes lignes)
# + faire un test de l'ensemble du programme
