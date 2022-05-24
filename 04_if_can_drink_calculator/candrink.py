# Frage den User "Wie alt bist du?" und speichere die Antwort
#   in der Variable alter.
alter = input('Wie alt bist du? ')

# Wandle alter in einen int um und speichere es in alter.
# alter = int(input('Wie alt bist du? '))
alter = int(alter)

# Falls das alter kleiner ist als 16:
if alter < 16:
    # -- Gebe den Text "No" aus. 
    print('No')

# Falls das alter größer als 15 und kleiner als 21 ist:
elif alter < 21:
    # -- Frage den User "Woher bist du?" und speichere es in ort. 
    ort = input('Woher bist du? ')

    # -- Falls ort "USA" ist:
    if ort == 'USA':
        # -- -- Gebe den Text "No" aus.
        print('No')
    # -- Falls ort nicht "USA" ist:
    else:
        # -- -- Gebe den Text "Yes" aus. 
        print('Yes')

# Falls alter größer als 20 ist:
else:
    # -- gebe den Text "Yes, welcome" aus. 
    print('Yes, welcome')