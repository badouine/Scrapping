# allexercice.py

from test_scraping import exercice1
import pandas as pd

def run_all_exercises():
    print("=== Exécution de tous les exercices ===\n")
    
    # Exercice 1
    print("=== Exercice 1: Extraction des titres et liens ===")
    try:
        df_ex1 = exercice1(None)
        print("Résultats:")
        print(df_ex1)
    except Exception as e:
        print(f"Erreur dans l'exercice 1: {e}")
    
    # Ajouter les autres exercices de la même manière
    # Exercice 2
    """
    print("\n=== Exercice 2: Extraction des produits ===")
    try:
        df_ex2 = exercice2(None)
        print("Résultats:")
        print(df_ex2)
    except Exception as e:
        print(f"Erreur dans l'exercice 2: {e}")
    """
    
    print("\n=== Fin de l'exécution de tous les exercices ===")

if __name__ == "__main__":
    run_all_exercises()