taches = []

def ajouter(tache):
    taches.append(tache)

def afficher():
    for i, t in enumerate(taches, 1):
        print(i, "-", t)

ajouter("Apprendre Git")
afficher()