import time
import random
import terminal  # ton projet externe

# ---- AFFICHAGE LOGO ----
def affichage_logo():
    print("  _____ _    _          ____   _____ ")
    print(" / ____| |  | |   /\   / __ \ / ____|")
    print("| |    | |__| |  /  \ | |  | | (___  ")
    print("| |    |  __  | / /\ \| |  | |\___ \ ")
    print("| |____| |  | |/ ____ \ |__| |____) |")
    print(" \_____|_|  |_/_/    \_\____/|_____/ ")
    print("démarrage ...........................")

# ---- ANIMATION DE CHARGEMENT ----
def barre_chargement():
    print("\nInstallation en cours :")
    for i in range(21):
        time.sleep(0.1)
        print("[" + "#" * i + " " * (20 - i) + "]")
    print("Installation terminée !\n")

# ---- MINI JEU ----
def mini_jeu():
    print("\n--- MINI JEU : Devine le nombre ---")
    nombre = random.randint(1, 10)
    essais = 3
    while essais > 0:
        choix = input("Devine un nombre entre 1 et 10 : ")
        if not choix.isdigit():
            print("Entre un vrai nombre !")
            continue
        choix = int(choix)
        if choix == nombre:
            print("Bravo ! Tu as gagné ! 🎉")
            return
        else:
            essais -= 1
            print("Raté ! Essais restants :", essais)
    print("Perdu ! Le nombre était :", nombre)

# ---- TERMINAL LOCAL POUR CHAOS.OS ----
def terminal_local():
    fichiers = []
    dossier_actuel = "/home"
    print("\nBienvenue dans le terminal de chaos.os")

    while True:
        commande = input(f"{dossier_actuel}> ").lower().strip()

        if commande == "help":
            print("\n---- COMMANDES DISPONIBLES ----")
            print("help      = afficher l’aide")
            print("site      = voir le site github")
            print("version   = afficher la version")
            print("clear     = effacer l’écran")
            print("ascii     = afficher le logo")
            print("info      = infos système")
            print("date      = afficher la date")
            print("echo      = répéter un texte")
            print("calc      = calcul simple")
            print("jeu       = lancer un mini-jeu")
            print("ls        = voir fichiers")
            print("mkdir     = créer dossier")
            print("touch     = créer fichier")
            print("pwd       = dossier actuel")
            print("quitter   = quitter le terminal")
            print("-------------------------------\n")

        elif commande == "site":
            print("Site officiel : https://mahegiogetiluciani-stack.github.io/site.io/")

        elif commande == "version":
            print("chaos.os version améliorée")

        elif commande == "ascii":
            affichage_logo()

        elif commande == "info":
            print("Système : chaos.os")
            print("Créateur : mahe giorgettiluciani")

        elif commande == "date":
            print("Date actuelle :", time.ctime())

        elif commande.startswith("echo"):
            print(commande[5:])

        elif commande == "calc":
            calcul = input("Calcul (ex: 5+5) : ")
            try:
                print("Résultat :", eval(calcul))
            except:
                print("Erreur de calcul")

        elif commande == "jeu":
            mini_jeu()

        elif commande == "ls":
            if fichiers:
                for f in fichiers:
                    print("-", f)
            else:
                print("Aucun fichier")

        elif commande.startswith("mkdir"):
            nom = commande[6:]
            if nom:
                fichiers.append("[DIR] " + nom)
                print("Dossier créé :", nom)
            else:
                print("Nom manquant")

        elif commande.startswith("touch"):
            nom = commande[6:]
            if nom:
                fichiers.append(nom)
                print("Fichier créé :", nom)
            else:
                print("Nom manquant")

        elif commande == "pwd":
            print("Dossier actuel :", dossier_actuel)

        elif commande == "clear":
            print("\n" * 50)

        elif commande == "quitter":
            print("Fermeture du terminal...")
            break

        else:
            print("Commande inconnue. Tape 'help'.")

# ---- INSTALLATION ----
def install():
    print("Quel version pour chaos 1.0 ou 1.1 ou quitter ?")
    version = input()

    if version == "1.0":
        print("Installation de chaos 1.0")
        barre_chargement()
        time.sleep(1)
        # Appel de ton projet terminal externe
        terminal.terminal_installation_chaos()  

    elif version == "1.1":
        print("Installation de chaos 1.1")
        affichage_logo()
        barre_chargement()
        # Terminal local pour version 1.1
        terminal_local()  

    elif version == "quitter":
        print("Installation annulée.")

    else:
        print("Version inconnue")

# ---- LANCEMENT ----
install()
