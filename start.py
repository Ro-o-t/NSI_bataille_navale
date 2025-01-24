from os import *#importer le module OS

def main():#déclaration de main
    system('cls')#clear le cmd
    print("\033[31mBonjour à toi, bienvenue sur notre jeu de bataille \
navale\033[0m")  # Texte en rouge
    print("Que veux-tu faire :")#depander ce qu'il veut faire
    print("1 : Commencer une partie")
    print("2 : Lancer le didacticiel")
    print("PS : \
si c'est ta première partie, choisis 2 pour comprendre le jeu ;)")

    choix = int(input("Ton choix : "))#demander de rentrer son choix
    if choix == 1:#si le choix est 1
        system("python bataille_navale_v8.py")  
        # Lancer le fichier Python du jeu
    elif choix == 2:#si il est 2
        system("python didacticiel.py")  
        # Lancer le fichier Python du didacticiel
    else:#sinon
        print("Choix invalide. Relance le programme et essaie à nouveau !")
        #dire que le choix est invalide

if __name__ == "__main__":#lancement de main
    main()#lancer main
