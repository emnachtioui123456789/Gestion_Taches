
# Liste des tâches
taches = []


# 1. Ajouter une tâche
def ajouter_tache():
    titre = input("Donner le titre de la tâche : ")
    description = input("Donner la description : ")

    identifiant = len(taches) + 1

    tache = {
        "id": identifiant,
        "titre": titre,
        "description": description,
        "statut": "En cours"
    }

    taches.append(tache)
    print("Tâche ajoutée avec succès !")


# 2. Afficher les tâches
def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche disponible.")
    else:
        for tache in taches:
            print("--------------------")
            print("ID :", tache["id"])
            print("Titre :", tache["titre"])
            print("Description :", tache["description"])
            print("Statut :", tache["statut"])


# 3. Rechercher une tâche
def rechercher_tache():
    try:
        id_recherche = int(input("Donner l'ID de la tâche : "))

        for tache in taches:
            if tache["id"] == id_recherche:
                print("Tâche trouvée :")
                print(tache)
                return

        print("Tâche introuvable.")

    except ValueError:
        print("Erreur : veuillez saisir un nombre.")


# 4. Modifier une tâche
def modifier_tache():
    try:
        id_modifie = int(input("Donner l'ID de la tâche à modifier : "))

        for tache in taches:
            if tache["id"] == id_modifie:
                nouveau_titre = input("Nouveau titre : ")
                nouvelle_description = input("Nouvelle description : ")

                tache["titre"] = nouveau_titre
                tache["description"] = nouvelle_description

                print("Tâche modifiée avec succès !")
                return

        print("Tâche introuvable.")

    except ValueError:
        print("Erreur : veuillez saisir un nombre.")


# 5. Menu principal
def menu():
    while True:
        print("\n==== GESTION DES TACHES ====")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Rechercher une tâche")
        print("4. Modifier une tâche")
        print("5. Quitter")

        try:
            choix = int(input("Votre choix : "))

            if choix == 1:
                ajouter_tache()
            elif choix == 2:
                afficher_taches()
            elif choix == 3:
                rechercher_tache()
            elif choix == 4:
                modifier_tache()
            elif choix == 5:
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")

        except ValueError:
            print("Erreur : veuillez saisir un nombre.")


# Exécution du programme
menu()
