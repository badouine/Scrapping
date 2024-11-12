def verifier_entier_positif(valeur):
    """
    Vérifie si une valeur est un nombre entier positif.
    
    Args:
        valeur: La valeur à vérifier (string)
    Returns:
        bool: True si c'est un entier positif, False sinon
    """
    try:
        # Convertir la chaîne en nombre
        nombre = int(valeur)
        # Vérifier si le nombre est positif
        return nombre > 0
    except ValueError:
        return False

# Programme principal pour tester la fonction
if __name__ == "__main__":
    while True:
        # Demander une valeur à l'utilisateur
        entree = input("Entrez un nombre (ou 'q' pour quitter): ")
        
        # Vérifier si l'utilisateur veut quitter
        if entree.lower() == 'q':
            print("Au revoir!")
            break
        
        # Vérifier si c'est un entier positif
        if verifier_entier_positif(entree):
            print(f"{entree} est un entier positif ✓")
        else:
            print(f"{entree} n'est pas un entier positif ✗")