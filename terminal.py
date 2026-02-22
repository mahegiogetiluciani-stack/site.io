def afficher_ascii():
    print("  /       \\  ")
    print(" /         \\ ")
    print("/  chaos.os  \\ ")
    print("\\ version1.0 /")
    print(" \\           / ")
    print("  \\         /  ")
    print("   \\       /   ")
    print("    \\     /    ")
    print("     \\   /     ")
    print("      \\ /      ")
    print("       V       ")


def terminal():
    print("\nBienvenue dans le terminal de chaos.os")
    afficher_ascii()

    while True:
        commande = input("chaos.os> ").lower()

        if commande == "help":
            print("\n---- LISTE DES COMMANDES ----")
            print("site    = voir le site github")
            print("version = afficher la version")
            print("clear   = effacer l’écran")
            print("ascii   = afficher le logo chaos.os")
            print("redémarrage    = quitter le terminal")
            print("quitter  = quitter le terminal")
            print("info    = informations système")
            print("-----------------------------\n")

        elif commande == "site":
            print("Site officiel : https://mahegiogetiluciani-stack.github.io/site.io/")

        elif commande == "version":
            print("chaos.os version 1.0")

        elif commande == "ascii":
            afficher_ascii()

        elif commande == "info":
            print("Système : chaos.os")
            print("Créateur : mahe giorgettiluciani")
            print("Mode simulation terminal")

        elif commande == "clear":
            print("\n" * 50)

        elif commande == "quitter":
            print("Fermeture du terminal...")
            break

        elif commande == "redémarrage":
            print("Redémarrage du terminal...")
            terminal()

        else:
            print("Commande inconnue. Tape 'helpe' pour voir les commandes.")


def terminal_installation_chaos():
    print("version facile ou difficile ?")
    print("   /       \\  ")
    print(" /         \\ ")
    print("/  chaos.os  \\ ")
    print("\\ version1.0 /")
    print(" \\           / ")
    print("  \\         /  ")
    print("   \\       /   ")
    print("    \\     /    ")
    print("     \\   /     ")
    print("      \\ /      ")
    print("       V       ")
    a = input().lower()

    if a == "facile":
        print("\nMode FACILE activé !")
        print("Visitez le site : https://mahegiogetiluciani-stack.github.io/site.io/")
        print("\nInstallation de chaos.os...\n")

        afficher_ascii()

        print("\nInstallation terminée en mode facile !")
        print("Accès direct au terminal...\n")

        terminal()


    elif a == "difficile":
        print("Mode difficile sélectionné")
        mot_de_passe = input("Mot de passe requis : ")

        if mot_de_passe == "tryimminrosse*//":
            print("Mot de passe correct !")
            terminal()
        else:
            print("Mot de passe incorrect. Accès refusé.")

    else:
        print("Choix invalide : tape 'facile' ou 'difficile'")
