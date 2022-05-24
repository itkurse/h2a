# Beispiel für ein eigenes Modul
# kann irgendwo importiert werden

# gibt True zurück wenn Email korrekt ist, ansonsten False
def validate_email(email):
    # mind. 5 Zeichen
    if len(email) < 5:
        return False 

    # check @
    if '@' not in email:
        return False 

    return True 


def validate_password(password):
    if len(password) < 6:
        return False
    return True 