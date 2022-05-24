# Eine Variable ist ein Container für einen Wert
# dieser Wert hat immer einen bestimmten Datentyp

'''
Regelen für Variablen:
- Variablennamen sind Case-Senstive
- müssen mit einem Buchstaben oder Underscore starten
- Underscore am Anfang hat eine besondere Bedeutung (private)
- dürfen Zahlen enthalten, aber nicht mit einer Zahl beginnen
- besteht der Name aus mehreren Wörter, dann werden diese mit 
  einem Underscore verbunden last_name 
- Variablennamen sollten keine Umlaute oder Sonderzeichen enthalten
'''

x = 1           # int
y = 2.5         # float 
name = 'Hansi'  # str - entweder in einfachen od. dopp. Anführungszeichen
name = "Hansi"
is_cool = True  # boolean - großen Anfangsbuchstaben beachten!
is_cool = False 

print(x, y, name, is_cool)


# Variablen können überschrieben werden
# dabei kann auch Bezug auf den alten Wert genommen werden
x = x + 5 
# ist gleich wie 
x += 5 

# welchen Datentyp hat eine Variable?
print(x, type(x))
print(name, type(name))