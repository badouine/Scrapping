import re

def est_email_valide(email):
    """
    Vérifie si une chaîne de caractères est une adresse email valide.
    
    Args:
        email (str): La chaîne de caractères à vérifier
    
    Returns:
        bool: True si l'email est valide, False sinon
        
    Exemples:
        >>> est_email_valide("utilisateur@domaine.com")
        True
        >>> est_email_valide("invalide@.com")
        False
    """
    # Motif de validation d'email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not isinstance(email, str):
        return False
    
    # Vérification de la longueur
    if len(email) > 254:  # Longueur maximale standard pour un email
        return False
        
    # Vérification du format avec regex
    if re.match(pattern, email):
        # Vérifications supplémentaires
        local_part = email.split('@')[0]
        if len(local_part) > 64:  # Longueur maximale de la partie locale
            return False
        return True
    return False

# Tests de démonstration
if __name__ == "__main__":
    emails_test = [
        "test@example.com",
        "user.name@domain.com",
        "user+tag@example.com",
        "invalid.email@",
        "@invalid.com",
        "invalid@.com",
        "test@test..com",
        "a" * 65 + "@example.com",  # Partie locale trop longue
        "test@" + "a" * 255 + ".com",  # Email trop long
    ]
    
    for email in emails_test:
        resultat = est_email_valide(email)
        print(f"'{email}' est {'valide' if resultat else 'invalide'}")