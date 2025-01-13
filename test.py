def somme_valeurs_etalon(nom_fichier):
    somme_totale = 0

    try:
        with open(nom_fichier, "r") as fichier:
            for i, ligne in enumerate(fichier):
                ligne = ligne.strip()  # Supprimer les espaces autour
                if not ligne:
                    print(f"Ligne {i + 1}: Ligne vide ignorée")
                    continue  # Ignorer les lignes vides

                chiffres = [c for c in ligne if c.isdigit()]  # Extraire tous les chiffres

                if len(chiffres) == 1:
                    # Si la ligne contient un seul chiffre, dupliquer ce chiffre
                    premier_chiffre = chiffres[0]
                    dernier_chiffre = chiffres[0]  # Le premier et le dernier chiffre sont identiques
                    print(f"Ligne {i + 1}: '{ligne}' -> Chiffre unique {premier_chiffre}, doublé en {premier_chiffre + dernier_chiffre}")
                elif len(chiffres) > 1:
                    # Sinon, utiliser le premier et le dernier chiffre
                    premier_chiffre = chiffres[0]
                    dernier_chiffre = chiffres[-1]
                    print(f"Ligne {i + 1}: '{ligne}' -> Premier: {premier_chiffre}, Dernier: {dernier_chiffre}")
                else:
                    print(f"Ligne {i + 1}: '{ligne}' -> Pas de chiffres détectés")
                    continue  # Ignorer si aucune chiffre trouvé

                # Combiner les deux chiffres et ajouter à la somme
                valeur_etalon = int(premier_chiffre + dernier_chiffre)
                somme_totale += valeur_etalon
                print(f"Ajouté {valeur_etalon} à la somme totale.")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

    print(f"Somme totale : {somme_totale}")
    return somme_totale


# Exemple d'utilisation avec un fichier de test
nom_fichier = "test.txt"
resultat = somme_valeurs_etalon(nom_fichier)
print(f"Résultat final : {resultat}")
