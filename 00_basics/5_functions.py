'''
Eine Funktion ist ein Block mit Code der nur ausgeführt wird,
wenn er aufgerufen wurde. 
In Python werden für den Code in der Funktion keine 
geschwungenen Klammern verwendet, stattdessen Einrückungen. 
'''

# Function erstellen
# function name: say_hello
# 2 Parameter: name, last_name 
# Parameter: um Informationen beim Aufruf in die Funktion hineinzubekommen
from cgitb import reset


def say_hello(name, last_name='Mustermann'):
    print(f'Hallo {name} {last_name}!')

# Function aufrufen (call function)
# 2 Argumente: 'Marc', 'Fenz'
say_hello('Marc', 'Fenz')
say_hello('Celina', 'Gumpold')
say_hello('Maurice')

# Function mit Rückgabewert
# 2 Parameter: a, b (Werte die beim Aufruf in die Funktion hineinkommen)
def addition(a, b):
    ergebnis = a + b 
    # nur return: beende die Funktion

    # beende die Funktion und gebe den Wert der Variable
    # ergebnis zurück
    return ergebnis 

# Aufruf der Funktion, speichere den Rückgabewert der 
# Funktion in der Variable result
result = addition(5, 3)
print('Ergebnis der Addition: ', result)

result = addition(addition(1, 2), 4)
print('Ergebnis der Addition:', result)



def multiplikation(a, b, c=1, d=1, e=1, f=1):
    ergebnis = a * b * c * d * e * f 
    return ergebnis 


print(multiplikation(2, 3, 4))
print(multiplikation(2, 3, 4, 5, 6, 7))
print(multiplikation(2, 3))


'''
Rückgabewerte einer Funktion
Eine Funktion kann immer nur einen Wert zurückgeben
-- entweder z. B. eine Zahl, ein String, ein bool, ...
-- oder eben ein Array, eine Liste, ein Tuple, ... 
'''