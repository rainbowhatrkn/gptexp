import random

# Fonction pour mélanger les lignes de deux fichiers texte
def melanger_fichiers(liste1_path, liste2_path, resultat_path):
    # Lire les lignes du premier fichier
    with open(liste1_path, 'r') as file:
        liste1 = file.readlines()

    # Lire les lignes du deuxième fichier
    with open(liste2_path, 'r') as file:
        liste2 = file.readlines()

    # Mélanger les deux listes de lignes
    random.shuffle(liste1)
    random.shuffle(liste2)

    # Fusionner les deux listes mélangées
    liste_melangee = liste1 + liste2

    # Mélanger à nouveau la liste fusionnée pour mélanger davantage les lignes
    random.shuffle(liste_melangee)

    # Écrire les lignes mélangées dans un nouveau fichier
    with open(resultat_path, 'w') as file:
        file.writelines(liste_melangee)

# Chemin vers les fichiers texte à mélanger
liste1_path = 'shos.txt'
liste2_path = 'shot.txt'

# Chemin vers le fichier où enregistrer le résultat
resultat_path = 'shots.txt'

# Appel de la fonction pour mélanger les fichiers
melanger_fichiers(liste1_path, liste2_path, resultat_path)

print("Les fichiers ont été mélangés avec succès.")