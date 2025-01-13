# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 12:06:18 2025

@author: LENOVO
"""

def somme_valeurs_etalon(nom_fichier):
    somme_totale = 0

    try:
        # Ouvrir le fichier en lecture
        with open(nom_fichier, "r") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()  # Enlever les espaces inutiles au début/fin de la ligne
                premier_chiffre = None
                dernier_chiffre = None

                # Parcourir chaque caractère pour identifier les chiffres
                for caractere in ligne:
                    if caractere.isdigit():
                        if premier_chiffre is None:
                            premier_chiffre = caractere  # Trouver le premier chiffre
                        dernier_chiffre = caractere  # Mettre à jour le dernier chiffre

                # Si on a trouvé les deux chiffres, former le nombre et l'ajouter
                if premier_chiffre is not None and dernier_chiffre is not None:
                    valeur_etalon = int(premier_chiffre + dernier_chiffre)
                    somme_totale += valeur_etalon

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

    return somme_totale


# Exemple d'utilisation avec un fichier
nom_fichier = "document.txt"

# Assurez-vous que le fichier 'calibration.txt' existe dans le même répertoire que le script
resultat = somme_valeurs_etalon(nom_fichier)
print(f"La somme des valeurs d'étalonnage est : {resultat}")
